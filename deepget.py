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
>>> _find_val(config,'hair.style.color')
['red']
>>> _find_val(config,'people.age')
['5', '3']
>>> _find_val(config,'people.phone.number')
['mikecell', 'mikehome', 'bobcell', 'bobcell']
>>> _find_val(config,'peole.phone.number')
[]

'''

def deep_get(dic,val,default=None):
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

