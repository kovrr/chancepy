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
