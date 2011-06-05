# -*- coding: utf-8 -*-
import system

class World(object):
    
    def __init__(self):
        self.names = [
                      'players',
                      'locations'
                      ]
        self.world = {
                      'players':[],
                      'locations':{}
                      }
        self.load()
        
    def get(self, layer=''):
        if not layer:
            return eval(self.world)
        elif layer in self.names:
            return eval(self.world[layer])
    
    def clear(self):
        if self.world.clear():
            return True

    def reset(self):
        self.world = {
                      'players':[],
                      'locations':{}
                      }

    def add(self, name, param):
        if name in self.names:
            if param in self.world[name]:
                return False
            else:
                self.world[name].append(param)
                return True
    
    def delete(self, name, param):
        if name in self.names:
            if param in self.world[name]:
                self.world[name].remove(param)
                return True
            else:
                return False
        else:
            return False

    def load(self):
        syst = system.System()
        self.world['locations'] = syst.get_json('blankworld')

    def save(self):
        pass
    #@todo: build save world
    
    def who_online(self):
        if self.world['players']:
            return True
