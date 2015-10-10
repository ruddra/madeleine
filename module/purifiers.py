import re

class Purifiers:

    def purify_country_name(self, name):
        try:
            robject = re.sub(r'([^\s\w]|_)+', '', name)
            return robject
        except:
            pass #todo




