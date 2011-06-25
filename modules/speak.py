from modules.system import System

__author__ = 'd1ffuz0r'
class Speak(object):

    def __init__(self):
        self.dialogs = {}
        self.load()

    def get(self,npc=''):
        if not npc:
            return self.dialogs
        else:
            return self.dialogs[npc]

    def load(self):
        system = System()
        self.dialogs = system.get_json('dialogs')