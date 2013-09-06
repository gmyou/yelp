# -*- coding:utf-8 -*-
"""
1. 전체 주 0 total = {} 값 Dict로 구하여 저장 (50건)
2. 1 ~total/20 수만큼 Call 
3. 10,000건 초과시 익일로 넘기기
"""

import os, sys
import datetime
from multiprocessing import Process, Queue
from Queue import Empty
import time

curdate = str(datetime.datetime.now())
curdate = curdate[:10].replace("-", "")




state = ('ca',)        
#state = ['nv','ne','nd','nc','nm','ny','nj','nh','de','ri','la','ma','md','me','mt','mn','mi','ms','mo','vt','va','sd','sc','id','ia','ar','ak','az','al','or','ok','oh','wy','wa','wv','wi','ut','in','il','ga','ks','ca','ky','ct','co','tn','tx','pa','fl','hi']
#state.sort()

restaurant = {'ak':18,'al':43,'ar':29,'az':324 ,'ca':33 ,'co':100 ,'ct':23,'de':21,'fl':214 ,'ga':369 ,'hi':102 ,'ia':18,'id':24,'il':368 ,'in':87,'ks':25,'ky':61,'la':680 ,'ma':175 ,'md':67,'me':21,'mi':231 ,'mn':33,'mo':83,'ms':12,'mt':9,'nc':96,'nd':11,'ne':33,'nh':18,'nj':70,'nm':59,'nv':207 ,'ny':1122,'oh':110 ,'ok':61,'or':211 ,'pa':148 ,'ri':55,'sc':25,'sd':10,'tn':42,'tx':201 ,'ut':45,'va':46,'vt':15,'wa':173 ,'wi':44,'wv':9,'wy':7}
food = {'ak':26,'al':51,'ar':36,'az':522 ,'ca':1258,'co':180 ,'ct':28,'de':29,'fl':320 ,'ga':525 ,'hi':205 ,'ia':23,'id':34,'il':656 ,'in':124 ,'ks':29,'ky':81,'la':1258,'ma':329 ,'md':97,'me':33,'mi':319 ,'mn':54,'mo':125 ,'ms':12,'mt':11 ,'nc':144 ,'nd':14,'ne':45,'nh':25,'nj':90,'nm':81,'nv':349 ,'ny':1758,'oh':162 ,'ok':77,'or':382 ,'pa':232 ,'ri':85,'sc':29,'sd':14,'tn':55,'tx':290 ,'ut':68,'va':61,'vt':23,'wa':302 ,'wi':70,'wv':11 ,'wy':8}




def do_test(term, loc, idx=0):
    x=0
    logFile = '/data/yelp/logs/'+term+'_'+curdate+'.log'

    f = open(logFile, 'a')    
    
    #g = open('grid_ca', 'r')
    #g = open('grid_ca_'+term+'.1', 'r')
    #g = open('grid_ca_'+term+'.2', 'r')
    #g = open('grid_ca_'+term+'.'+idx, 'r')
    g = open('grid_ca_'+term+'_over1000', 'r')

    pos = []
    
    for p in g:                                                  
        s = p[1:-2].replace(' ', '')
        ne = s.split(',')
        pos.append(ne)
        
    
    for ne in pos:
        
        sw1 = float(ne[0])-0.1
        sw2 = float(ne[1])-0.1
        s = ne[0] + ',' + ne[1] + '|' + str(sw1) + ',' + str(sw2)
        
        print s

        #url_params = '-q="'+term+'" --bounds="'+s+'" --offset='+str(x)
        url_params = '-q="'+term+'" --bounds="'+s+'"'
        #Log
        f.write(loc+'\t'+str(x)+'\n')
        #Json
        o = '/data/yelp/json/'+term+'/'+loc+'/'+term+'_'+loc+'_'+str(x)+'.json'
        print o
        #print 'python yelp.py '+url_params
        os.system('python yelp.py '+url_params+' >> '+o)
        x+=1
        
        time.sleep(0.1)
        
        #break
      
    f.close()

            
def do_work(q, term, loc, x=0):
    
    #os.system('mkdir /data/yelp/json/'+term+'/'+loc+'/')
    
    if (term == "food"):
        y = food[loc]
    else:
        y = restaurant[loc]
        
    
    logFile = '/data/yelp/logs/'+term+'_'+curdate+'.log'
    
    while x<y:
        try:
            
            f = open(logFile, 'a')
    
            url_params = '-q="'+term+'" --bounds="37.619127,-122.312954|37.519127,-122.212954" --offset='+str(x)

            #Log                
            f.write(loc+'\t'+str(x)+'\n')
        
            #Json
            o = '/data/yelp/json/'+term+'/'+loc+'/'+term+'_'+loc+'_'+str(x)+'.json'
            #print o
            print '['+str(x)+'] python yelp.py '+url_params
            os.system('python yelp.py '+url_params+' >> '+o)
    
            x+=1
            time.sleep(1)
            
        except Empty:
            break
    
        finally:
            f.close()
            

def init_file(term):
    
    #os.system('mkdir /data/yelp/json/'+term+'/')
    
    
    
    for loc in state:
        
        f = '/data/yelp/json/'+term+'/'+loc+'/*.json'
        print f
        os.system('rm '+f)
        
        """
        try:
            os.system('rm /data/yelp/json/'+term+'_'+loc+'.json')
        except IOError:
            pass
        """
            
"""
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
"""   
   
if __name__ == '__main__':
    
    term = ""
    
    if len(sys.argv) == 1:
        print "Your must select option - 'restaurant' or 'food' ?"
        exit(0)
    
    term = sys.argv[1]
    
    """
    if len(sys.argv) == 2:
        print "Your must select option index - 1, 2, 3..."
        exit(0)
            
    idx = sys.argv[2]
    """
    
    
    #do_test(term, 'ca', idx)        
    do_test(term, 'ca')
    #init_file(term)


    
    
    """

    work_queue = Queue()
    
    for i in range(1,50):
        work_queue.put(i)
    
    processes = [Process(target=do_work, args=(work_queue, term, loc, )) for loc in state]
    
    for p in processes:
        p.start()
        
    for p in processes:    
        p.join()
    
    """