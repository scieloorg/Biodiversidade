op=$1
EXECUTE_DOWNLOAD=$2
GENERATE_DB=$3
START_DATE=$4
END_DATE=$5

APIKEY=b64e048b-e947-44c2-b5e3-b9ba4e47fce0


# paths
CISIS1660=../../bases/cisis1660
DB_PATH=../db
XML_PATH=../xml_path
DONE_PATH=../done/
TMP_PATH=../temp

# existing files
FST=../../bases/lildbi/dbcertif/lilacs/LILACS.fst

#
LILDB_PATH=../../bases/lildbi/dbcertif/lilacs/
LILDB_NAME=LILACS

LILDB=$LILDB_PATH/$LILDB_NAME



# to create
PROCESSED_ID_LIST=$DB_PATH/processed_id.seq
NEW_ID=$DB_PATH/new_id
NEW_ID_ISO=$DB_PATH/new_id_iso-8859-1
NEW_ID_UTF=$DB_PATH/new_id_utf-8

BHLDB=$DB_PATH/bhl

TMP_LILDB=$DB_PATH/new.`date '+%Y%m%d'`
NEW_LILDB=$DB_PATH/$LILDB_NAME
BIOTA_ID=$DB_PATH/biota_fapesp_lildbi_iso-8859-1

#
TODO_LIST=$DB_PATH/todolist

if [ ! -d $TMP_PATH ]
then
    mkdir -p $TMP_PATH
fi
if [ ! -d $DB_PATH ]
then
    mkdir -p $DB_PATH
fi
if [ ! -d $XML_PATH/i ]
then
    mkdir -p $XML_PATH/i
fi
if [ ! -d $XML_PATH/t ]
then
    mkdir -p $XML_PATH/t
fi

# create ../db/processed_ids which contains the processed title and its items id
if [ -f $LILDB.mst ]
then
    #$CISIS1660/mx $LILDB fst=@$FST fullinv=$LILDB
    #$CISIS1660/mx $LILDB btell=0 "DB_BHL$" lw=9999 "pft=v901^*,'|',v900^*/" now > $PROCESSED_ID_LIST
    $CISIS1660/mx $BHLDB lw=9999 "pft=mfn,'|',v901^*,'|',v965^d,'|',v965^*/" now | sort -u -r > last_id
    $CISIS1660/mx seq=last_id create=last_id now -all
    $CISIS1660/mx last_id count=1 "pft=v2" now> last_id
    $CISIS1660/mx last_id count=1 "pft=v3" now> last_date
else
    echo 0 > last_id
    echo 2009-03-29 > last_date

    echo > $PROCESSED_ID_LIST
fi

if [ -f $NEW_ID ]
then
rm $DB_PATH/new_id
fi
if [ -f $NEW_ID_ISO ]
then
    rm $NEW_ID_ISO
fi
if [ -f $NEW_ID_UTF ]
then
    rm $NEW_ID_UTF
fi

# download titles.xml
if [ "@$op" == "@download_all" ]
then
    PARAM3=$PROCESSED_ID_LIST
    PARAM4=$NEW_ID
    
    OP=$op
fi
if [ "@$op" == "@download_incr" ]
then
    if [ ! -f last_date ]
    then
        echo "2009-03-29" > last_date
    fi
    s_date=`cat last_date`
    $CISIS1660/mx null count=1 "pft=s(date)*0.4,'-',s(date)*4.2,'-',s(date)*6.2" now > curr_date
    e_date=`cat curr_date`

    PARAM3=$PROCESSED_ID_LIST
    PARAM4=$NEW_ID
    PARAM5=$s_date
    PARAM6=$e_date
    PARAM7=`cat last_id`
    if [ ! "@$START_DATE" == "@" ]
    then
        if [ ! "@$END_DATE" == "@" ]
        then
            PARAM5=$START_DATE
            PARAM6=$END_DATE
        fi
    fi
    
    OP=$op
fi

if [ "@$OP" == "@" ]
then
    echo "Usage: $0 [ download_all | download_incr  ]"
    echo You tried to execute
    echo $0 $1 $2 $3 $4 $5 $6
else
    
    if [ "@$EXECUTE_DOWNLOAD" == "@YES" ]
    then 
       echo Executing python3 ../bhl2lilacs/call_bhl2lilacs.py $OP $XML_PATH $PARAM3 $PARAM4  $PARAM5 $PARAM6 $PARAM7
       python3 ../bhl2lilacs/call_bhl2lilacs.py $OP $XML_PATH $PARAM3 $PARAM4  $PARAM5 $PARAM6 $PARAM7
    fi
    if [ "@$GENERATE_DB" == "@YES" ]
    then 
        echo Generating DB
       
	    $CISIS1660/mx null count=0 create=$NEW_LILDB now -all
	    $CISIS1660/mx seq=lang.gzm.seq create=lang now -all
	
	    # check biota
	    if [ -f $BIOTA_ID ]
	    then
	        echo LOADING BIOTA
	        echo "   create $BIOTA_ID"
	        $CISIS1660/id2i $BIOTA_ID create=$BIOTA_ID
	        echo "   fix.prc"
	        $CISIS1660/mx $BIOTA_ID gizmo=lang,40 "proc=@fix.prc" copy=$BIOTA_ID now -all
	        echo "   fix v13"
	        $CISIS1660/mx $BIOTA_ID "proc='d13',if v13='*' then if v12[1]^i<>'en' then (if v12^i='en' then 'a13{',v12^*,'{' fi) fi fi" "proc='s'" copy=$BIOTA_ID now -all
	        echo "   append $BIOTA_ID to $NEW_LILDB"
	        
	        $CISIS1660/mx $BIOTA_ID +control now
	        $CISIS1660/mx $NEW_LILDB +control now
	        
	        $CISIS1660/mx $BIOTA_ID append=$NEW_LILDB now -all
	        $CISIS1660/mx $NEW_LILDB +control now
	    fi
	    
	    if [ -f $NEW_ID_ISO ]
	    then
	        echo LOADING NEW
	        echo "   create $TMP_LILDB"
	        $CISIS1660/id2i $NEW_ID_ISO create=$TMP_LILDB
	    
	        if [ -f $TMP_LILDB.mst ]
	        then
	            echo $TMP_LILDB append to $BHLDB
	            $CISIS1660/mx $TMP_LILDB +control now
	            $CISIS1660/mx $BHLDB +control now
	            $CISIS1660/mx $TMP_LILDB gizmo=lang,40 mfrl=99000 fmtl=99000 "proc=@add.prc"  copy=$TMP_LILDB now -all
	            $CISIS1660/mx $TMP_LILDB gizmo=lang,40 "proc=@fix.prc" "proc='s'" append=$BHLDB now -all
	            
	            $CISIS1660/mx $BHLDB +control now
	        fi
	    fi
	    
	    # check bhl
	    if [ -f $BHLDB.mst ]
	    then
	            
	        echo append $BHLDB to $NEW_LILDB
	        $CISIS1660/mx $BHLDB append=$NEW_LILDB now -all
	        echo $NEW_LILDB
	        $CISIS1660/mx $NEW_LILDB +control now
	    fi
	    
	
	    
	    if [ -f $NEW_LILDB.mst ]
	    then
	        $CISIS1660/mx $NEW_LILDB fst=@$FST fullinv=$NEW_LILDB
	        cp $NEW_LILDB.??? $LILDB_PATH
	        
	        echo backup $NEW_LILDB
	        if [ -f ../db/LILACS.bkp.tgz ]
	        then
	           mv ../db/LILACS.bkp.tgz ../db/LILACS.bkp.old.tgz
	        fi
	        tar cvfzp ../db/LILACS.bkp.tgz $NEW_LILDB.???
	        
	    fi
    fi
fi

