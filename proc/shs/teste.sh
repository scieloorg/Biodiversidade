op=$1
START_DATE=$2
END_DATE=$3


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

TMP_LILDB=$DB_PATH/temp_lilacs
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
    $CISIS1660/mx $LILDB btell=0 "DB_BHL$" lw=9999 "pft=v901^*,'|',v900^*/" now > $PROCESSED_ID_LIST
    $CISIS1660/mx $LILDB btell=0 "DB_BHL$" lw=9999 "pft=v965/" now | sort -u -r > dates
    $CISIS1660/mx seq=dates create=dates now -all
    $CISIS1660/mx dates count=1 "pft=v1" now> last_date
else
    $CISIS1660/mx null count=1 "proc='a333{',date,'{'" create=$LILDB now -all
    $CISIS1660/mx $LILDB fst=@$FST fullinv=$LILDB

    echo > $PROCESSED_ID_LIST
fi

if [ -f $NEW_ID ]
then
rm $DB_PATH/new_id
fi
if [ -f $NEW_ID_ISO ]
then
echo ...
fi
if [ -f $NEW_ID_UTF ]
then
    rm $NEW_ID_UTF
fi

    s_date=`cat last_date`
    $CISIS1660/mx null count=1 "pft=s(date)*0.4,'-',s(date)*4.2,'-',s(date)*6.2" now > curr_date
    e_date=`cat curr_date`


    ##python3 ../bhl2lilacs/call_bhl2lilacs.py $OP $XML_PATH $PARAM3 $PARAM4  $PARAM5 $PARAM6
    
    $CISIS1660/mx null count=0 create=$NEW_LILDB now -all
    $CISIS1660/mx seq=lang.gzm.seq create=lang now -all

    # check biota
    $CISIS1660/mx $LILDB btell=0 "DB_FAPESP-BIOTA" count=1 lw=9999 "pft=v4" now > biota
    EXIST_BIOTA=`cat biota`
    if [ "@$EXIST_BIOTA" == "@" ]
    then
        echo create BIOTA
        $CISIS1660/id2i $BIOTA_ID create=$BIOTA_ID
        $CISIS1660/mx $BIOTA_ID "proc='d13',if v13='*' then if v12[1]^i<>'en' then (if v12^i='en' then 'a13{',v12^*,'{' fi) fi fi" "proc='s'" append=$NEW_LILDB now -all
    fi

    if [ -f $LILDB.mst ]
    then
        echo backup LILACS
        if [ -f ../db/LILACS.bkp.tgz ]
        then
           mv ../db/LILACS.bkp.tgz ../db/LILACS.bkp.`date '+%Y%m%d-%H%M%S'`.tgz
        fi
        tar cvfzp ../db/LILACS.bkp.tgz $LILDB.*
        echo $LILDB append to $NEW_LILDB
        echo $CISIS1660/mx $LILDB gizmo=lang,40,940 "proc=@fix.prc"  append=$NEW_LILDB now -all
	#$CISIS1660/mx $LILDB gizmo=lang,40,940 "proc=@fix.prc"  append=$NEW_LILDB now -all
    fi

    if [ -f $NEW_ID_ISO ]
    then
        echo create $TMP_LILDB
	echo $CISIS1660/id2i $NEW_ID_ISO create=$TMP_LILDB

        #$CISIS1660/id2i $NEW_ID_ISO create=$TMP_LILDB
    fi
    if [ -f $TMP_LILDB.mst ]
    then
        echo $TMP_LILDB append to $NEW_LILDB
        echo $CISIS1660/mx $TMP_LILDB gizmo=lang,40,940 "proc=@add.prc" "proc='s'" append=$NEW_LILDB now -all
    fi

    if [ -f $NEW_LILDB.mst ]
    then
	    echo $CISIS1660/mx $NEW_LILDB fst=@$FST fullinv=$NEW_LILDB
	    echo cp $NEW_LILDB.* $LILDB_PATH
    fi


