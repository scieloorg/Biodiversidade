echo `date '+%Y%m%d-%H%M%S'`
. ../bhl_lilacs/configuration.ini

if [ ! -d $NEW_LILACS_DB_PATH ]
then
	mkdir -p $NEW_LILACS_DB_PATH 
fi 
$CISIS_PATH/mx null count=0 create=$NEW_LILACS_DB now -all
$CISIS_PATH/mx seq=lang.gzm.seq create=lang now -all

# check biota
if [ -f $BIOTA_ID ]
then
    echo LOADING BIOTA
    echo "   create $BIOTA_ID"
    $CISIS_PATH/id2i $BIOTA_ID create=$BIOTA_ID
    
    $CISIS_PATH/mx $BIOTA_ID gizmo=lang,40 "proc=@biota.prc" copy=$BIOTA_ID now -all
    
    $CISIS_PATH/mx $BIOTA_ID "proc='d13',if v13='*' then if v12[1]^i<>'en' then (if v12^i='en' then 'a13{',v12^*,'{' fi) fi fi" "proc='s'" copy=$BIOTA_ID now -all
    
    echo "   append $BIOTA_ID to $NEW_LILACS_DB"
    
    $CISIS_PATH/mx $BIOTA_ID +control now
    $CISIS_PATH/mx $NEW_LILACS_DB +control now
    
    $CISIS_PATH/mx $BIOTA_ID append=$NEW_LILACS_DB now -all
    $CISIS_PATH/mx $NEW_LILACS_DB +control now
fi



# check bhl
if [ -f $BHL_DB.mst ]
then
    echo $BHL_DB
    $CISIS_PATH/mx $BHL_DB +control now
    
    echo append $BHL_DB to $NEW_LILACS_DB
    $CISIS_PATH/mx $BHL_DB append=$NEW_LILACS_DB now -all
    echo $NEW_LILACS_DB
    $CISIS_PATH/mx $NEW_LILACS_DB +control now
fi



if [ -f $NEW_LILACS_DB.mst ]
then
    echo Inverting $NEW_LILACS_DB
    $CISIS_PATH/mx $NEW_LILACS_DB fst=@$FST fullinv=$NEW_LILACS_DB
    echo Copying $NEW_LILACS_DB
    cp $NEW_LILACS_DB.??? $LILDB_PATH
fi
    
cd ../shs

echo `date '+%Y%m%d-%H%M%S'`
