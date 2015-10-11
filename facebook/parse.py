import facebook

package = facebook.GraphAPI

from settings import config

APP_KEY = config.FACEBOOK_APP_KEY
APP_SECRET = config.FACEBOOK_APP_SCR


class FacebookParser(object):
    def __init__(self, query):
        self.query = None
        self.language = None
        self.location = None
        self.language = None
        self.graph = None
        self.search = None
        # self.authenticate()

    def authenticate(self):
        token = package.get_app_access_token(APP_KEY, APP_SECRET)
        print(token)

if __name__ == '__main__':
    fb = FacebookParser('test')
    fb.authenticate()

