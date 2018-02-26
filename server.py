#coding:utf-8
from config import settings
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from handlers.main.main_urls import handlers
from tornado.options import options,define
from models.accounts.account_user_model import *
from models.article_model.article_model import *
from models.Blog_model.blog_model import *
from models.contact_model.contact_model import*

from libs.db import create_talbes
from libs.db.dbsession import dbSession

define('port',default=8000,help="run port",type=int)
define('runserver',default=False,type=bool)
define('t',default=False,type=bool)
define('u',default=False,type=bool)

if __name__ == "__main__":
    options.parse_command_line()
    if options.t:
        create_talbes.run()

    if options.u:
        user = User()
        user.name = 'zhangsan'
        user.password = '222'
        dbSession.add(user)
        dbSession.commit()

    if options.runserver:
        app = tornado.web.Application(handlers,**settings)
        http_Server = tornado.httpserver.HTTPServer(app)
        http_Server.listen(options.port)
        print "start server..."
        tornado.ioloop.IOLoop.instance().start()
