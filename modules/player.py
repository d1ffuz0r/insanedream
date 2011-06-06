# -*- coding: utf-8 -*-
from modules.database import DB

class Player(object):
    
    def __init__(self,username):
        self.player = {}
        self.load(username)

    def get(self):
        return self.player

    def load(self,username):
        db = DB()
        self.player = db.get_player(username)
        
    def set_param(self,name,value):
        self.player[name] = value

    def get_param(self,name):
        return self.player[name]

