# -*- coding: utf-8 -*-
import tornado.database, hashlib
__author__ = 'd1ffuz0r'

class DB(object):
    def __init__(self):
        self.db = tornado.database.Connection(host='localhost', database='wofd', user='root', password='root')

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
        return self.db.get('SELECT name FROM players WHERE name = %s', player_name)

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

    def player_exists(self,player_name):
        if self.db.get('SELECT name FROM players WHERE name = %s', player_name):
            return True