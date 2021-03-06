import datetime
import re

import DateSpec


class DatePickerService:
    DATE_FORMAT = "%m-%d-%Y"

    def __init__(self):
        self.us_federal_holidays = [
            # 2020
            "01-01-2020",
            "01-20-2020",
            "02-17-2020",
            "05-25-2020",
            "07-03-2020",  # Independence day observed
            "07-04-2020",
            "09-07-2020",
            "10-12-2020",
            "11-11-2020",
            "11-26-2020",
            "12-25-2020",

            # 2021
            "01-01-2021",
            "01-18-2021",
            "02-15-2021",
            "05-31-2021",
            "07-04-2021",
            "07-05-2021",  # Independence day observed
            "09-06-2021",
            "10-11-2021",
            "11-11-2021",
            "11-25-2021",
            "12-24-2021",  # Christmas day observed
            "12-25-2021",
            "12-31-2021",  # New Year's Day observed
        ]
        self.us_holidays = [
            # 2020
            "01-01-2020",
            "01-20-2020",
            "05-25-2020",
            "07-03-2020",  # Independence day observed
            "07-04-2020",
            "09-07-2020",
            "11-11-2020",
            "11-26-2020",
            "12-25-2020",

            # 2021
            "01-01-2021",
            "01-18-2021",
            "05-31-2021",
            "07-04-2021",
            "07-05-2021",  # Independence day observed
            "09-06-2021",
            "11-11-2021",
            "11-25-2021",
            "12-24-2021",  # Christmas day observed
            "12-25-2021",
            "12-31-2021",  # New Year's Day observed
        ]

    def sanitize_year(self, year):
        if len(year) == 2:
            return "20" + year
        return year

    def pick_dates(self, text):

        date_range = re.findall("((0|1)\d{1})[-\/]((0|1|2)\d{1})[-\/]((19|20)?\d{2})", text)
        returned_date_spec = DateSpec.DateSpec(False, [])

        if "EXCEPT" in text:
            returned_date_spec.except_flag = True

            if "HOLIDAY" in text:  # This will also cover text "HOLIDAYS"
                if "FEDERAL" in text:
                    returned_date_spec.dates = self.us_federal_holidays
                else:
                    returned_date_spec.dates = self.us_holidays

        elif date_range and len(date_range) == 2:
            from_year = self.sanitize_year(date_range[0][4])
            from_date = datetime.date(int(from_year), int(date_range[0][0]), int(date_range[0][2]))

            to_year = self.sanitize_year(date_range[1][4])
            to_date = datetime.date(int(to_year), int(date_range[1][0]), int(date_range[1][2]))

            today = datetime.date.today()
            for i in range(365):  # Evaluate for 1 year
                date_to_evaluate = today + datetime.timedelta(days=i)
                if from_date <= date_to_evaluate <= to_date:
                    returned_date_spec.dates.append(date_to_evaluate.__str__())  # convert date to string

        if len(returned_date_spec.dates) == 0:
            return None
        else:
            return returned_date_spec
