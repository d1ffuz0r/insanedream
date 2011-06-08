'''
Created on 03.06.2011

@author: d1ffuz0r
'''
import unittest
from modules.player import Player
from modules.world import World

world = World()
player = Player('punkNdead')

class MyWorldTest(unittest.TestCase):

    def test_getWorld(self):
        self.assertIsNotNone(world.get())

    def test_add_online(self):
        self.assertEqual([],world.online_who())
        world.online_add('ololo')
        self.assertEqual(['ololo'],world.online_who())

    def test_delete_online(self):
        world.online_delete('ololo')

    def test_saveWorld(self):
        pass #@todo build 

    def test_who_online(self):
        print self.assertEqual([],world.online_who())

    def test_in_world(self):
        player_loc = player.get()['location']
        world.add(player_loc,player.get())

        
'''
    def test_load_location(self):
        player_loc = player.get()['location']
        playerz = player.get()
        world.update({'%s'% player_loc : playerz})
        self.assertIsNotNone(world.get_locations())
        self.assertIsNotNone(world.get('locations')['loc.bank'])
        self.assertIsNotNone(world.get_loc('loc.bank'))
'''
if __name__ == "__main__":
    unittest.main()
