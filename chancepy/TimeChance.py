import pytz
from .BaseRandom import BaseRandom
import datetime


class TimeChance(BaseRandom):
    @classmethod
    def ampm(cls):
        return cls.random.choice(["am", "pm"])

    @classmethod
    def date(cls, year=None, month=None, day=None):
        # this method might fail if 29 of februray is selected
        random_date = datetime.date.fromtimestamp(cls.timestamp())
        match = False
        while not match:
            match_month = random_date.month == month if month is not None else True
            match_day = random_date.day == day if day is not None else True

            match = match_month and match_day
            if not match:
                random_date = random_date + datetime.timedelta(1)
        if year:
            random_date = datetime.date(
                year=year, month=random_date.month, day=random_date.day
            )
        return random_date

    @classmethod
    def timestamp(cls):
        now = int(datetime.datetime.now().timestamp())
        random_timestamp_until_now = cls.random.randint(0, now)
        return random_timestamp_until_now

    @classmethod
    def year(cls, mini=None, maxi=None):
        if not mini:
            mini = datetime.date.today().year
        return cls.random.randint(mini, maxi if maxi else mini + 100)

    @classmethod
    def month(cls, mode="numeric"):
        month = cls.random.randint(1, 12)
        if mode == "numeric":
            return month
        if mode == "short":
            return datetime.date(1970, month, 0).strftime("%b")
        if mode == "full":
            return datetime.date(1970, month, 1).strftime("%B")
        raise ValueError("invalid mode, choose 'numeric', 'short' or 'full")

    @classmethod
    def weekday(cls, mode="full"):
        date = cls.date()
        if mode == "full":
            return date.strftime("%A")
        if mode == "short":
            return date.strftime("%a")
        if mode == "numeric":
            return date.weekday()
        raise ValueError("invalid mode, choose 'numeric', 'short' or 'full")

    @classmethod
    def hour(cls, twentyfour=False):
        return cls.random.randint(1, 24 if twentyfour else 12)

    @classmethod
    def minute(cls):
        return cls.random.randint(0, 59)

    @classmethod
    def second(cls):
        return cls.random.randint(0, 59)

    @classmethod
    def millisecond(cls):
        return cls.random.randint(0, 999)

    @classmethod
    def timezone(cls):
        return pytz.timezone(cls.random.choice(pytz.all_timezones))
