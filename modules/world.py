# -*- coding: utf-8 -*-
from modules import system

syst = system.System()

class World(object):
    
    def __init__(self):
        self.online = []
        self.world = {}
        self.locations = {}
        self._load_blank()
        self._load_location()

    def get(self):
        return self.world
    
    def get_in_lock(self,loc):
        if loc in self.world:
            return self.world[loc]
        else:
            return []

    def clear(self):
        if self.world.clear():
            return True

    def reset(self):
        self.world = {}

    def add(self, name, param):
        if name not in self.world:
            self.world.update({name:[param]})
        else:
            loc = self.world[name]
            loc.append(param)
    
    def delete(self, name, param):
        self.world.remove('')

    def save(self):
        pass
    #@todo: build save world

    def _load_blank(self):
        self.world = syst.get_json('blankworld')

    def _load_location(self):
        self.locations = syst.get_json('locations')

    def update_loc(self,name,param):
        name = str(name)
        if name not in self.world:
            self.world[name] = [param]
        else:
            loc = self.world[name]
            loc.append(param)
            self.world.update(name=loc)
            
    def move(self,item,old,new):
        old = str(old)
        new = str(new)
        if old and new in self.locations:
            if item in self.world[old]:
                player = self.world[old][syst.num_item(self.world[old],item)]
                del self.world[old][syst.num_item(self.world[old],player)]
                self.update_loc(new,player)

    def get_locations(self):
        return self.locations

    def get_loc(self, loc):
        if loc in self.locations:
            return self.locations[loc]
        else:
            return False

    def online_who(self):
        return self.online
    
    def online_add(self,name):
        if name not in self.online:
            self.online.append(name)

    def online_delete(self,name):
        self.online.remove(name)