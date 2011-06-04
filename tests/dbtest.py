# -*- coding: utf-8 -*-
import unittest
from modules.player import Player

class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = Player('punkNdead')
        print p.get()
        p.set_param('lager','1')
        print p.get()
        if int(p.get()['lager']) == 1:
            print 'player is blood'

if __name__ == '__main__':
    unittest.main()