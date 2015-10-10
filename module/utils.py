import pycountry

class LangNameRetriever(object):

    def __init__(self, lang_code):
        self.language = None
        self.get_language_name(lang_code)

    def get_language_name(self, lang_code):
        try:
            pycntry_obj = pycountry.languages.get(iso639_1_code=lang_code)
            self.language = pycntry_obj.name

        except:
            self.language = lang_code

