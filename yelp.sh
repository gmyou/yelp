DATE_YYYYMMDD=`TZ=KST+39 date '+%Y%m%d'`

cd /usr/local/scheduler
python yelp.py > /data/yelp/store/store_$DATE_YYYYMMDD.log
