import os, sys

state = ('nv','ne','nd','nc','nm','ny','nj','nh','de','ri','la','ma','md','me','mt','mn','mi','ms','mo','vt','va','sd','sc','id','ia','ar','ak','az','al','or','ok','oh','wy','wa','wv','wi','ut','in','il','ga','ks','ca','ky','ct','co','tn','tx','pa','fl','hi')


def sep(term):
    for loc in state:
        os.system('mkdir /data/yelp/json/'+term+'/'+loc)
        os.system('mv /data/yelp/json/'+term+'/'+loc+'*.json /data/yelp/json/'+term+'/'+loc)

sep('restaurant')
sep('food')