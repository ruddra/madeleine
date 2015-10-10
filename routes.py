from core.handler import MainHandler
from twitter.handler import TwitterHandler

__author__ = 'arnabkumarshil'


routes = [
    (r"/", MainHandler),
    (r"/twitter", TwitterHandler),
]