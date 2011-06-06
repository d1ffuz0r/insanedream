'''
Created on 03.06.2011

@author: d1ffuz0r
'''
import unittest
from modules.player import Player

player = Player('punkNdead')

class MyPlayerTest(unittest.TestCase):
    def test_loadPlayer(self):
        self.assertIsNotNone(player.get())

    def test_setParam(self):
        self.assertIsNone(player.get_param('lager'))
        player.set_param('lager', 1)
        self.assertEqual(player.get_param('lager'), 1)

    def test_savePlayer(self):
        pass #@todo build

if __name__ == '__main__':
    unittest.main()