#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop, tornado.web, tornado.autoreload, tornado.options
from tornado.escape import utf8
import os, time
from modules import world, database

current_date = time.strftime('%d-%m-%Y')
_world = world.World()
_db = database.DB()

class BaseHandler(tornado.web.RequestHandler):
            
    def get_current_user(self):
        return self.get_secure_cookie('username')
    
    def current_account(self):
        return self.get_secure_cookie('account')
    
    def initialize(self):
        self.msg = []
        if not self.get_current_user():
            self.user = None
        else:
            self.user = tornado.escape.xhtml_escape(self.get_current_user())
        
class Index(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
    
    @tornado.web.asynchronous
    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if not username:
            self.msg.append('enter login')
        elif not password:
            self.msg.append('enter password')
        else:
            if _db.user_exists(username):
                uname = _db.get_user(username)
                self.set_secure_cookie("username", uname['username'])
                #log.access('user logged in(username: %s, ip:%s)' % (uname['username'], self.request.remote_ip))
                self.redirect('/')
            else:
                self.msg.append('вы ввели неправильный пароль или такого пользователя не существует')
                #log.error('error auth(login:%s, password: %s, ip: %s)' % (username, password, self.request.remote_ip))
        self.async_callback(self._on_render())
                
    def _on_render(self):
        self.render('index.xhtml', message=self.msg, username=self.user, users_count=len(_world.who_online()))
        
class Registration(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
        
    @tornado.web.asynchronous
    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        password_repeat = self.get_argument("password_repeat", None)
        email = self.get_argument("email", None)
        if not username:
            self.msg.append('enter login')
        else:
            if _db.user_exists(username):
                self.msg.append('user with this login alreasy exists')
            else:
                if not password:
                    self.msg.append('enter password')
                elif not password_repeat:
                    self.msg.append('repeat password')
                elif password != password_repeat:
                    self.msg.append('password is not identific')
                elif not email:
                    self.msg.append('enter e-mail')
                else:
                    _db.create_user(username,password, email, current_date, self.request.remote_ip)
                    self.set_secure_cookie("username", username)
                    self.redirect('/')
        self.async_callback(self._on_render())
        
    def _on_render(self):
        self.render('register.xhtml', message=self.msg, username=self.user)

class Logout(BaseHandler):
    
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_logout())
        
    def _on_logout(self):
        self.clear_cookie('username')
        self.redirect('/')

class WhoOnline(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
    
    def _on_render(self):
        self.render('online.xhtml', message=self.msg, users=_world.who_online())

class About(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
    
    def _on_render(self):
        self.render('about.xhtml', message=self.msg)

class Contacts(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
    
    def _on_render(self):
        self.render('contacts.xhtml', message=self.msg)

class Rules(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self):
        self.async_callback(self._on_render())
        
    def _on_render(self):
        self.render('rules.xhtml', message=self.msg)

class Profile(BaseHandler):
    
    @tornado.web.asynchronous
    def get(self, username):
        self.async_callback(self._on_render(username))
        
    def _on_render(self, username):
        self.render('profile.xhtml', message=self.msg, profile=username)

class GameAccounts(BaseHandler):

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        acc = _db.get_players(self.user)
        delete_name = self.get_argument('delete', '')
        select_name = self.get_argument('select', '')
        if select_name:
            self.redirect('/game/connect/%s' % select_name)
        if delete_name:
            _db.delete_player(delete_name,acc['user']['account_id'])
            self.redirect('/game/connect')
        self.async_callback(self._on_render(acc))

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        acc = _db.get_players(self.user)
        name = utf8(self.get_argument('name_player', ''))
        if not name:
            self.msg.append('not name')
        elif _db.player_exists(name) > 0:
            self.msg.append('already exist in world')
        elif len(acc['accounts']) == 5:
            self.msg.append('maximum count characters')
        else:
            _db.create_player(acc['user']['account_id'],name)
            self.redirect('/game/connect')
        self.async_callback(self._on_render(acc))
        
    def _on_render(self, accs):
        self.render('accounts.xhtml', message=self.msg, username=self.user, accounts=accs['accounts'])

class GameAccount(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self, accountName):
        self.set_secure_cookie('account', accountName)
        self.async_callback(self._on_render(accountName))
        
    def _on_render(self, accountName):
        self.render('account.xhtml', message=self.msg, username=self.user, account=accountName)
"""
class GameAccountSettings(BaseHandler):

@tornado.web.authenticated
@tornado.web.asynchronous
def get(self, account):
    self.async_callback(self.on_render())

def _on_render(self):
self.render('settings.xhtml', message=self.msg, username=self.user)
"""
class Game(BaseHandler):
    
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        _world.add('players', self.current_account())
        self.async_callback(self._on_render())
        
    def post(self):
        pass
    
    def _on_render(self):
        self.write('you in game')
        self.finish()
        
        
class GameServer(tornado.web.Application):
    def __init__(self):
        handlers = routes = [
            (r'/', Index),
            (r'/register', Registration),
            (r'/logout', Logout),
            (r'/online', WhoOnline),
            (r'/about', About),
            (r'/contacts', Contacts),
            (r'/rules', Rules),
            (r'/profile/(.*?)', Profile),
            (r'/game', Game),
            (r'/game/connect', GameAccounts),
            (r'/game/connect/(.*?)', GameAccount),
            #(r'/game/connect/settings/(.*?)', GameAccountSettings),
            
        ]
        settings = {
            'game_title': u'World of Death',
            'template_path': os.path.join(os.path.dirname(__file__), "data/templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "data/static"),
            'xsrf_cookies': True,
            'cookie_secret': "11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            'login_url': "/",
            'port': 8080,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    srv = GameServer()
    srv.listen(srv.settings['port'])
    #thread.start_new_thread(_system, ())
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()
    tornado.autoreload.start(io_loop=None, check_time=10)
    
if __name__ == "__main__":
    main()
