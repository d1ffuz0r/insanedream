# -*- coding: utf-8 -*-
'''
Created on 03.06.2011

@author: d1ffuz0r
'''
import unittest
from modules.database import DB

db = DB()

class MyDatabaseTest(unittest.TestCase):

    def test_getPlayer(self):
        self.assertDictEqual(dict(name=u'punkNdead'),db.get_player('punkNdead'))
        
    def test_getPlayers(self):
        print db.get_players('root')

    def test_getUser(self):
        self.assertDictEqual(dict(username=u'root'),db.get_user('root'))

    def test_userExists(self):
        self.assertTrue(db.user_exists('root'))

    def test_checkLogin(self):
        self.assertTrue(db.check_login('root','root'))

    def test_playerExists(self):
        self.assertTrue(db.player_exists('punkNdead'))

    def test_createExistsUser(self):
        self.assertFalse(db.create_user('root1','root','email@maim.cd','11.11.11','127.0.0.1'))

    def test_createExistsPlayer(self):
        self.assertFalse(db.create_player(1,'punkNdead'))

if __name__ == '__main__':
    unittest.main()