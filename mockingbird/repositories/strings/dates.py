from datetime import datetime
from itertools import repeat
from itertools import imap
from random import randrange


class DateGenerator(object):

    def __init__(self,
                 min_month=1,
                 max_month=12,
                 min_year=2000,
                 max_year=None,
                 format="%m/%d/%Y"):

        max_month = 13 if max_month == 12 else max_month

        min_month = min(13, abs(min_month))
        max_month = min(13, abs(max_month))

        max_year = max_year = datetime.now().year if max_year is None else abs(max_year)
        min_year = max(1500, abs(min_year))
        max_year = max(min_year, max_year)

        self.format = format
        self.months = imap(randrange, repeat(min_month), repeat(max_month))
        self.years = imap(randrange, repeat(min_year), repeat(max_year))
        self.days = imap(randrange, repeat(1), repeat(32))

    def action(self, context):
        while 1:
            try:
                date = datetime(year=next(self.years),
                                month=next(self.months),
                                day=next(self.days))
                break
            except ValueError:
                # the day may be out of range for the month
                # just try again
                pass


        return date.strftime(self.format)
