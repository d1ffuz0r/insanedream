# -*- coding: utf-8 -*-
class System(object):
    
    def __init__(self):
        pass
    
    def get_json(self, fname):
        f = file('D:/worldofdeath/data/%s.json' % fname, 'r')
        return f.read()
        f.close()
