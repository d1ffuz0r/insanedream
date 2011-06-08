# -*- coding: utf-8 -*-
class System(object):
    
    def __init__(self):
        pass
    
    def get_json(self, fname):
        f = file('D:/worldofdeath/data/%s.json' % fname, 'r')
        return eval(f.read())
        f.close()

    def num_item(self,list,who):
        i = -1
        for j in list:
            i += 1
            if j == who:
                return i