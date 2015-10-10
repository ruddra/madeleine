from module.utils import LangNameRetriever
from module.purifiers import Purifiers

__author__ = 'arnabkumarshil'

import json

from twython import Twython

from settings import config

APP_KEY = config.TWITTER_APP_KEY
APP_SECRET = config.TWITTER_APP_SCR

# APP_KEY = '1ZSShnzXc2woPfX8fsWj9qpbN'
# APP_SECRET = 'YtLHFvg0foDOJOnS1f9hLvBBn1RmOWkRI7l2Hv9qyDoXOnvLPa'

twitter_parser = Twython


class TwitterParser(object):
    def __init__(self, query):
        self.location = None
        self.language = None
        self.query = query
        self.twitter = None
        self.search = None
        self.authenticate()  # Does the authentication
        self.do_search()  # Does searching
        self.parse_data()  # Does the parsing

    def authenticate(self):
        """
        Gets twitter authentication
        :return:
        """
        twpy = twitter_parser(APP_KEY, APP_SECRET, oauth_version=2)
        ACCESS_TOKEN = twpy.obtain_access_token()
        self.twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

    def do_search(self):
        """
        Searches query through twitter API
        :return:
        """
        self.search = self.twitter.search(q=self.query)

    def parse_data(self):
        """
        Parses data and builds location and language dictionary
        :return:
        """
        if len(self.search) != 0:
            statuses = self.search['statuses']
            self.location = self.get_location(statuses)
            self.language = self.get_language(statuses)

    def get_location(self, data):
        """
        Builds location dictionary
        :param data:
        :return:
        """
        loc_list = list()
        for item in data:
            validator = Purifiers()
            _location = validator.purify_country_name(item['user']['location'])
            loc_list.append(_location)

        loc_dict = self.make_data_dict(loc_list)
        return loc_dict

    def get_language_name(self, langcode):
        try:
            lobj = LangNameRetriever(langcode)
            return lobj.language
        except:
            return langcode

    def make_data_dict(self, ldata):
        """
        Converts list into dictionary
        :param ldata:
        :return:
        """
        keys = list(set(ldata))
        _ddict = dict()
        for key in keys:
            if key:
                _ddict[key] = ldata.count(key)

        return _ddict

    def get_language(self, data):
        """
        Builds dictionary from list for language
        :param data:
        :return:
        """
        lan_list = list()
        for item in data:
            _language = self.get_language_name(item['metadata']['iso_language_code'])
            lan_list.append(_language)

        loc_dict = self.make_data_dict(lan_list)
        return loc_dict

    def get_json(self):
        """
        Returns json with proper data
        :return:
        """
        _jdict = dict()
        _jdict['query'] = self.query
        _jdict['language'] = self.language if self.language else {'None': 0}
        _jdict['location'] = self.location if self.location else {'None': 0}

        return json.dumps(_jdict)


if __name__ == '__main__':
    twits = TwitterParser(query='python')
    print(twits.get_json())
