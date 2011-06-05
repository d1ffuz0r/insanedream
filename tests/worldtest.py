'''
Created on 03.06.2011

@author: d1ffuz0r
'''
import unittest
from modules.world import World

world = World()

class MyWorldTest(unittest.TestCase):

    def test_getWorld(self):
        self.assertIsNotNone(world.get('locations'))

    def test_addWorld(self):
        self.assertTrue(world.add('players','ololo'))
        self.assertFalse(world.add('pla','ololo'))

    def test_deleteFromWorld(self):
        self.assertTrue(world.delete('players','ololo'))
        self.assertFalse(world.delete('players','ololo1'))

    def test_saveWorld(self):
        pass #@todo build 

    def test_whoOnline(self):
        self.assertFalse(world.who_online())

if __name__ == "__main__":
    unittest.main()
