#coding:utf-8
from config import settings
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from handlers.main.main_urls import handlers
from tornado.options import options,define

define('port',default=8000,help="run port",type=int)
define('runserver',default=False,type=bool)

if __name__ == "__main__":
    options.parse_command_line()
    if options.runserver:
        app = tornado.web.Application(handlers,**settings)
        http_Server = tornado.httpserver.HTTPServer(app)
        http_Server.listen(options.port)
        print("start server...")
        tornado.ioloop.IOLoop.instance().start()
