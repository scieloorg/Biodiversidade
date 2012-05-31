
if [ ! -d ../log ]
then
    mkdir -p ../log
fi
mylog=../log/r.`date '+%Y%m%d-%H%M%S'`.log
sh ./bhl2lilacs.sh download_incr YES YES 2>&1 $mylog
sh ./call_lilacs2iahx.sh 2>> $mylog
scp ../db/bhl.xml poseidon:/var/www/search_bhlscielo_org/proc/sci2iahx/scripts/
scp /var/www/lildbibio_scielo_org/bases/lildbi/dbcertif/lilacs/LILACS.??? poseidon:/var/www/lildbibio_scielo_org/bases/lildbi/dbcertif/lilacs