
CISIS1660=$1
DB=$2
XML_FILENAME=$3

if [ "@$CISIS1660" == "@" ]
then
    echo Missing PARAM1: CISIS1660
else
    if [ "@$DB" == "@" ]
    then
        echo Missing PARAM2: DB
    else
        if [ "@$XML_FILENAME" == "@" ]
        then
            echo Missing PARAM3: XML_FILENAME
        else
            $CISIS1660/mx seq=gizmos/gent1.txt create=gizmos/gent1 now -all
            $CISIS1660/mx seq=gizmos/gent2.txt create=gizmos/gent2 now -all

            $CISIS1660/mx $DB gizmo=gizmos/gent1 gizmo=gizmos/gent2 "prolog=@pft/prolog.pft" "epilog=@pft/epilog.pft" "pft=@pft/i2xml.pft" -all now tell=1 > $XML_FILENAME
            
        fi
    fi
fi
