'''
Created on 03.06.2011

@author: d1ffuz0r
'''
import unittest
from modules.world import World

class Test(unittest.TestCase):

    def testLoadWorld(self):
        world = World()
        world.add('players', 'ololo')
        print world.who_online()
        print world.get('locations')
if __name__ == "__main__":
    unittest.main()
