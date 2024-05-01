from datetime import datetime
from pytz import timezone

class DateTime:
    date_hour = "%Y-%m-%dT%H:%M:%S"
    date = "%Y-%m-%d"
    tmz = "Brazil/East"

    def now(self, datetime_string = False, hora_zerada = False):
        now = datetime.now(timezone(self.tmz))
        now = datetime.strptime(now.strftime(self.date_hour), self.date_hour)

        if hora_zerada:
            now = datetime.strptime(
                                    now.strftime(self.date) + 'T12:00:00',
                                    self.date_hour
                                )

        if datetime_string:
            return now.strftime(self.date_hour)

        return now

dateTime = DateTime()