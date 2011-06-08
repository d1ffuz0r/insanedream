# -*- coding: utf-8 -*-
import time
from modules.database import DB
class Player(object):
    
    def __init__(self):
        self.player = {}

    def get(self):
        return self.player

    def load(self,username):
        db = DB()
        self.player = db.get_player(username)

    def save(self,username):
        db = DB()
        db.save_player(self.get(),username)

    def set_param(self,name,value):
        self.player[name] = value

    def get_param(self,name):
        return self.player[name]

    def to_world(self):
        location = self.get_param('location')
        player = self.get()
        world.update_loc(location, player)