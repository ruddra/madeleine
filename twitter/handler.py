from twitter.parse import TwitterParser
import tornado.ioloop
import tornado.web


class TwitterHandler(tornado.web.RequestHandler):
    def post(self):
        query = self.get_argument('query')
        twitter = TwitterParser(query)
        return self.write(twitter.get_json())
