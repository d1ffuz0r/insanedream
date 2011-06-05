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
        print world.get('locations')
        self.assertEqual(['ololo'],world.who_online())
if __name__ == "__main__":
    unittest.main()
