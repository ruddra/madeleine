import os
import tornado.ioloop
import tornado.web
import routes
import logging
import settings

app_settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "portal/template"),
    'static_path': os.path.join(os.path.dirname(__file__), "portal/assets"),
}
application = tornado.web.Application(routes.routes, **app_settings)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.info('-------------- Starting Madeleine, A social media query tool ----------------')
    logger.info('-------------- Developed by Arnab Kumar Shil ----------------')
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

