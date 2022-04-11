import datetime

from mails_to_santa.holidays import HOLIDAY_LIST


class MailsToSanta:
    @staticmethod
    def calculated_time_to_process(time_of_arrival: datetime.datetime) -> datetime.datetime:
        holidays = HOLIDAY_LIST
        a = time_of_arrival
        res = a
        print(a)

        if a.hour < 8:
            res = a.replace(hour = 8, minute = 0, second = 0)
        if a.hour > 15 or a.hour == 15 and a.minute == 59:
            res = a.replace(hour = 8, minute = 0, second = 0)
            res += datetime.timedelta(days = 1)
        if a.weekday() > 4 or a.weekday() == 4 and a.hour > 15:
            res = a.replace(hour = 8, minute = 0, second = 0)
            res += datetime.timedelta(days = 7 - a.weekday())

        holi = []
        for i in range(len(holidays)):
            start = datetime.date(a.year, holidays[i]["start"]["month"], holidays[i]["start"]["day"])
            end = datetime.date(a.year, holidays[i]["end"]["month"], holidays[i]["end"]["day"])
            for j in range((end - start).days + 1):
                holi.append(start + datetime.timedelta(days = j))
                holi.append(start + datetime.timedelta(days = j + 366))


        while a.date() in holi:
            a += datetime.timedelta(days = 1)
            res = a.replace(hour = 8, minute = 0, second = 0)
            if res.weekday() > 4 or res.weekday() == 4 and res.hour > 15:
                res = res.replace(hour = 8, minute = 0, second = 0)
                res += datetime.timedelta(days = 7 - res.weekday())

        return res