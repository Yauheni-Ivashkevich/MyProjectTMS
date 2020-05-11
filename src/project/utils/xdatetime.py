from datetime import date
from datetime import datetime
from typing import NamedTuple
from typing import Optional

from delorean import Delorean
from django.conf import settings


def utcnow() -> datetime:
    return Delorean().datetime


def now(timezone: Optional[str] = None) -> datetime:
    tz = timezone or settings.LOCAL_TIME_ZONE
    return Delorean().shift(tz).datetime


class DateDelta(NamedTuple):
    years: int
    months: int

    def __str__(self):
        parts = []

        if self.years:
            suffix = "s" if (self.years % 10) != 1 else ""
            parts.append(f"{self.years} y{suffix}")

        if self.months:
            suffix = "s" if (self.months % 10) != 1 else ""
            parts.append(f"{self.months} mo{suffix}")

        if not any((self.years, self.months)):
            parts.append("<1 mo")

        return " ".join(parts)

    @classmethod
    def build(cls, start: date, finish: Optional[date] = None) -> "DateDelta":
        finish = finish or utcnow().date()
        delta = finish - start
        years, days = divmod(delta.days, 365)
        months = days // 30
        return DateDelta(years=years, months=months)
