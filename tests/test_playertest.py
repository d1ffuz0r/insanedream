'''
Created on 03.06.2011

@author: d1ffuz0r
'''
from datetime import time
import random
import unittest
from modules.player import Player
from modules.world import World

player = Player()
world = World()
class MyPlayerTest(unittest.TestCase):
    def test_loadPlayer(self):
        player.load('punkNdead')
        self.assertIsNotNone(player.get())
        
    def test_setParam(self):
        self.assertIsNone(player.get_param('lager'))
        player.set_param('lager', 1)
        self.assertEqual(player.get_param('lager'), 1)

    def test_savePlayer(self):
        pass #@todo build

    def test_loadInWorld(self):
        pass

if __name__ == '__main__':
    unittest.main()
