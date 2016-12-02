from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
import os.path

from app.web.modules.pagehandlers import PageHandlers
from app.web.modules.apphandlers import AppHandler
from app.web.modules.boardhandler import BoardHandlers

Handlers = [(r"/insertArt", AppHandler.AddArticleHandler),
			(r"/", PageHandlers.MainHandler),
			(r"/login", PageHandlers.LoginHandler),
			(r"/userCenter", PageHandlers.UserHandler),
			(r"/register", PageHandlers.RegisterHandler),
			(r"/addComment", BoardHandlers.AddCommentHandler),
			(r"/pickComment", BoardHandlers.PickCommentsHandlers)
			]




settings = dict(
	cookie_secret="lalalatinytiger###",
	login_url="/login",
	template_path=os.path.join(os.path.dirname(__file__), "views")
)

application = Application(
	Handlers, **settings
)

if __name__ == '__main__':
	server = HTTPServer(application)
	server.listen(options.port)
	IOLoop.current().start()
