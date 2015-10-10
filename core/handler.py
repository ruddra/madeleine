__author__ = 'arnabkumarshil'

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
