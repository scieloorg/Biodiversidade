debug=$1

if [ "@$debug" == "@" ]
then
    debug=yes
fi

mylog=r.`date '+%Y%m%d-%H%M%S'`.log
sh ./bhl2lilacs.sh download_incr $debug> $mylog
sh ./call_lilacs2iahx.sh >> $mylog