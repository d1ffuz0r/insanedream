# -*- coding: utf-8 -*-
import unittest
from modules.database import DB

db = DB()

class MyTestCase(unittest.TestCase):

    def test_getPlayer(self):
        print db.get_player('punkNdead')
        
    def test_getPlayers(self):
        print db.get_players('root')

    def test_getUser(self):
        print db.get_user('root')

    def test_userExists(self):
        print db.user_exists('root')

    def test_checkLogin(self):
        print db.check_login('root','root')

    def test_playerExists(self):
        print db.player_exists('punkNdead')

    def test_createUser(self):
        print db.create_user('root1','root','email@maim.cd','11.11.11','127.0.0.1')

    def test_createPlayer(self):
        print db.create_player(1,'punkNdead')

if __name__ == '__main__':
    unittest.main()