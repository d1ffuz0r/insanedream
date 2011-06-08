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

    def go(self, new_loc):
        loc = self.get_param('location')
        c_loc = world.get_loc(loc)['war']
        n_loc = world.get_loc(new_loc)['war']
        if new_loc in world.get_loc(self.get_param('location'))['exits']:
            self.set_param('location',new_loc)
            if (c_loc==2) and (n_loc==1):
                self.set_param('journal','you in peace territory')
            elif (c_loc==1) and (n_loc==2):
                self.set_param('journal','you in war territory')
            elif c_loc==n_loc:
                self.set_param('journal','')
            #world.move(self.get(),loc,new_loc)
            return new_loc
        else:
            return False
        del c_loc,n_loc