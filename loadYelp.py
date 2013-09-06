import json
#from pymongo import MongoClient

#client = MongoClient('localhost', 27017)
#db = client.napkin
#collection = db.yelp_store

"""
state = ('nv','ne','nd','nc','nm','ny','nj','nh','de','ri','la','ma','md','me','mt','mn','mi','ms','mo','vt','va','sd','sc','id','ia','ar','ak','az','al','or','ok','oh','wy','wa','wv','wi','ut','in','il','ga','ks','ca','ky','ct','co','tn','tx','pa','fl','hi')

for loc in state:                                                  
    #f = open('/data/yelp/store/'+loc+'.json','r')
    f = open('sample.json','r')
    j = f.read()
    data = json.loads(j)
"""

f = open('restaurant_nv_0.json','r')
j = f.read()
data = json.loads(j)
    
#print data

for k, v in data.iteritems():
    #if (k=="businesses"):
    #    print collection.insert(v)
    if (k=="total"):
        print "total : "+str(v)