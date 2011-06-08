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
        for j,t in data.items():
            print j,':',type(t)
        self.db.execute('UPDATE players SET \
        guild="'+str(data['guild'])+'" WHERE name = %s',player_name)
        '''
        guild_status="'+int(data['guild_status'])+'", \
                lager="'+int(data['lager'])+'", \
                location="'+str(data['location'])+'",\
                ghost="'+int(data['ghost'])+'", \
                journal="'+list(data['journal'])+'", \
                magic="'+list(data['magic'])+'", \
                messages="'+list(data['messages'])+'", \
                life="'+int(data['life'])+'", \
                life_max="'+int(data['life_max'])+'", \
                mana="'+int(data['mana'])+'", \
                mana_max="'+int(data['mana_max'])+'", \
                time_regenerate="'+int(data['time_regenerate'])+'", \
                time_speed="'+int(data['time_speed'])+'", \
                war="'+list(data['war'])+'", \
                pd="'+str(data['pd'])+'", \
                st="'+str(data['st'])+'", \
                p_m="'+str(data['p_m'])+'", \
                items="'+data['items']+'", \
                equip="'+data['equip']+'", \
                deystvo="'+str(data['deystvo'])+'", \
                status="'+int(data['status'])+'", \
                t_go="'+int(data['t_go'])

        '''
    def player_exists(self,player_name):
        if self.db.get('SELECT name FROM players WHERE name = %s', player_name):
            return True