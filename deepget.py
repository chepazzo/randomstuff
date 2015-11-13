# -*- coding: utf-8 -*-
'''
Provides deep_get function for getting data from dictionaries.

Returns a list of results, because if your deep path includes lists, 
you will have multiple results).

If any part of the path is an invalid key, then [] is returned.

e.g.
>>> config = {
...   'people': [
...     {
...      'name': 'Mike',
...      'phone': [
...         {'type':'cell','number':'mikecell'},
...         {'type':'home','number':'mikehome'},
...      ],
...      'age': '5',
...     },
...     {
...      'name': 'Bob',
...      'phone': [
...         {'type':'cell','number':'bobcell'},
...         {'type':'home','number':'bobcell'},
...      ],
...      'age': '3',
...     },
...   ],
...   'hair': {
...     'style': {
...         'color': 'red'
...     }
...   }
... }
>>> deep_get(config,'hair.style.color')
['red']
>>> deep_get(config,'people.age')
['5', '3']
>>> deep_get(config,'people.phone.number')
['mikecell', 'mikehome', 'bobcell', 'bobcell']
>>> deep_get(config,'peole.phone.number')
[]

'''

def deep_get(dic,val,default=None):
    '''
    Provides deep_get function for getting data from dictionaries.
    
    Returns a list of results, because if your deep path includes lists, 
    you will have multiple results).
    
    If any part of the path is an invalid key, then [] is returned.
    
    e.g.
      deep_get(config,'people.age')
        returns the equivalent of: [ c['age'] for c in config['people'] ]
      deep_get(config,'people.phone.number')
        returns the equivalent of:
         [ 
            config['people'][0]['phone'][0]['number'],
            config['people'][0]['phone'][1]['number'],
            config['people'][1]['phone'][0]['number'],
            config['people'][1]['phone'][1]['number'],
         ]
    '''
    path = val.split('.')
    currlevels = [ dic ]
    def _getval(dic,p):
        if dic is None:
            return []
        if 'keys' in dir(dic):
            if p not in dic:
                return []
            return [ dic.get(p,default) ]
        if '__iter__' in dir(dic):
            retval = []
            for x in dic:
                retval.extend(_getval(x,p))
            return retval
    return []
    for p in path:
        cl = []
        for currlevel in currlevels:
            cl.extend(_getval(currlevel,p))
        currlevels = cl
    return currlevels

