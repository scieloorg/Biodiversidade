

if [ ! -d ../log ]
then
    mkdir -p ../log
fi
mylog=../log/r.`date '+%Y%m%d-%H%M%S'`.log


# generate bhl db
cd ../bhl_lilacs
python3 bhl_db.py new  2>> $mylog
cd ../shs

# generate lilacs db (bhl + biota)
sh ./generate_lilacs_db.sh 2>> $mylog

# generate xml from lilacs db
sh ./generate_xml.sh 2>> $mylog

# Transference
. transf_config.ini
scp ../../bases/bhl/bhl.xml $DEST_XML
scp /var/www/lildbibio_scielo_org/bases/lildbi/dbcertif/lilacs/LILACS.??? $DEST_LILACS
