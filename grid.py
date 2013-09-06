# -*- coding:utf-8 -*-

from itertools import product
from sys import float_info
 
_float_min = float_info.min
_epsilon = float_info.epsilon
 
def float_eq(a, b):
    """ floating point comparison from http://floating-point-gui.de/"""
    absA = abs(a)
    absB = abs(b)
    diff = abs(a - b)
    """
    if a == b:
        return True
    elif a == 0 or b == 0 or diff < _float_min:
        return diff < (_epsilon * _float_min)
    else:
        return diff / (absA + absB) < _epsilon
    """
    if a == 0 or b == 0 or diff < _float_min:
        return diff < (_epsilon * _float_min)
    else:
        return diff / (absA + absB) < _epsilon
 
def xxrange(start, stop, step=1):
    cur = start
    while cur < stop:
        yield cur
        cur += step
 
def write_log(locs, term):
    #f = open('grid_ca', 'w')
    f = open('grid_ca_'+term+'_over1000', 'a')
    
    for i, loc in enumerate(locs):                                                  
        print i, loc
        f.write(str(loc)+"\n")
        
    f.close() 

#lats = xxrange(18.0, 64.0, step)
#lngs = xxrange(-124.0, -66.0, step)

"""
CA
NE포인트 : 41.9,-114.4
SW포인트 : 32.2,-123.9

step = 0.1
lats = xxrange(32.2, 41.9, step)
lngs = xxrange(-123.9, -114.4, step)
locs = reversed([(round(lat, 1), round(lng, 1)) for lat, lng in product(lats, lngs) if not float_eq(lat, lng)])
"""

#1000개 넘는 것
step = 0.01
#term = "food"
term = "restaurant"
f = open('grid_ca_over1000_'+term)
for l in f:
    xy = l.split("|")
    xy1 = xy[0].split(",")
    xy2 = xy[1].split(",")
    #print xy2[0], xy1[0], xy2[1], xy1[1],

    lats = xxrange(float(xy2[0]), float(xy1[0]), step)
    lngs = xxrange(float(xy2[1]), float(xy1[1]), step)
    
    locs = reversed([(round(lat, 2), round(lng, 2)) for lat, lng in product(lats, lngs) if not float_eq(lat, lng)])
    
    write_log(locs, term)