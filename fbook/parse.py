import facebook

# from settings import config

# APP_KEY = config.FACEBOOK_APP_KEY
# APP_SECRET = config.FACEBOOK_APP_SCR

APP_KEY = '1638346193112812'
APP_SECRET = '5e946eb30492334c25b4ee9b42a06c5f'


class FacebookParser(object):
    def __init__(self, query):
        self.query = None
        self.language = None
        self.location = None
        self.language = None
        self.graph = None
        self.search = None
        # self.authenticate()

    def get_token(self):
        graph = facebook.GraphAPI()
        token = graph.get_app_access_token(APP_KEY, APP_SECRET)
        return token

    def do_search(self, token):
        graph = facebook.GraphAPI(token)
        print(graph.request('/search/q=test'))


if __name__ == '__main__':
    fb = FacebookParser('test')
    token = fb.get_token()
    print(token)
    fb.do_search(token)
