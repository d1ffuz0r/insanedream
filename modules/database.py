# -*- coding: utf-8 -*-
import tornado.database
import hashlib

class DB(object):
    def __init__(self):
        self.db = tornado.database.Connection(host='localhost', database='wofd', user='root', password='root')
        self.db

    def user_exists(self,username):
        if self.db.get("SELECT username FROM accounts WHERE username = %s", username):
            return True

    def check_login(self, username, password):
        if self.db.get("SELECT username FROM accounts WHERE username = %s AND password = %s", username, hashlib.md5(password).hexdigest()):
            return True

    def create_user(self, username, password, email, date, ip):
        if self.user_exists(username):
            return False
        else:
            if self.db.execute('INSERT INTO accounts (username,password,email,date,ip) VALUES(%s,%s,%s,%s,%s)', username,hashlib.md5(password).hexdigest(), email, date, ip):
                return True
            
    def get_user(self, username):
        return self.db.get("SELECT username FROM accounts WHERE username = %s LIMIT 1", username)

    def get_player(self, player_name):
        return self.db.get('SELECT * FROM players WHERE name = %s', player_name)

    def get_players(self,user):
        self.id = self.db.get('SELECT account_id FROM accounts WHERE username = %s', user)
        self.accs = self.db.query('SELECT name,status FROM players WHERE account_id = %s',int(self.id['account_id']))
        return {'user':self.id,'accounts':self.accs}

    def create_player(self, account_id, name):
        if self.player_exists(name):
            return False
        else:
            if self.db.execute('INSERT INTO players (account_id,name) VALUES (%s,%s)', int(account_id), str(name)):
                return True

    def delete_player(self, player_name, account_id):
        if self.db.execute('DELETE FROM players WHERE name = %s and account_id = %s', player_name, int(account_id)):
            return True
    def save_player(self, data, player_name):
        self.db.execute('UPDATE players SET guild=%s, guild_status=%s, lager=%s, location=%s, ghost=%s, journal=%s, magic=%s, messages=%s, life=%s, life_max=%s, mana=%s, mana_max=%s, time_regenerate=%s, time_speed=%s, war=%s, pd=%s, st=%s, p_m=%s, items=%s, equip=%s, deystvo=%s, status=%s, t_go=%s  WHERE name = %s',data['guild'],data['guild_status'],data['lager'],data['location'],data['ghost'],data['journal'],data['magic'],data['messages'],int(data['life']),int(data['life_max']),int(data['mana']),int(data['mana_max']),data['time_regenerate'],data['time_speed'],data['war'],data['pd'],data['st'],data['p_m'],data['items'],data['equip'],data['deystvo'],data['status'],data['t_go'],player_name)
        
    def player_exists(self,player_name):
        if self.db.get('SELECT name FROM players WHERE name = %s', player_name):
            return True