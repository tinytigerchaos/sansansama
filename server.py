from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from app.web.modules.pagehandlers import PageHandlers
from app.web.modules.apphandlers import AppHandler

Handlers = [(r"/insertArt/(.*)", AppHandler.AddArticleHandler),
			(r"/",PageHandlers.MainHandler),
			(r"/login",PageHandlers.LoginHandler),
			(r"/userCenter/(.*)",PageHandlers.UserHandler),
			(r"/register",PageHandlers.RegisterHandler)
			]




settings = dict(
	cookie_secret="lalalatinytiger###",
	login_url = "/login"
)


application = Application(
    Handlers,**settings
)

if __name__ == '__main__':
    server = HTTPServer(application)
    server.listen(8080)
    IOLoop.current().start()