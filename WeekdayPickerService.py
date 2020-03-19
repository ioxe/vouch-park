import WeekdaySpec
import re


class WeekdayPickerService:
    weekDays = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
    output_weekday_nums = {
        "SUN": 1,
        "MON": 2,
        "TUE": 3,
        "WED": 4,
        "THU": 5,
        "FRI": 6,
        "SAT": 7,
    }
    weekDayWords = (
    "EVERYDAY", "MON", "MONDAY", "MONDAYS", "TUE", "TUESDAY", "TUESDAYS", "WED", "WEDNESDAY", "WEDNESDAYS", "THU",
    "THURSDAY", "THURSDAYS", "FRI", "FRIDAY", "FRIDAYS", "SAT", "SATURDAY", "SATURDAYS", "SUN", "SUNDAY", "SUNDAYS")

    def __init__(self):
        pass

    def get_weekday_index(self, text):
        if "MON" in text:
            return 0
        elif "TUE" in text:
            return 1
        elif "WED" in text:
            return 2
        elif "THU" in text:
            return 3
        elif "FRI" in text:
            return 4
        elif "SAT" in text:
            return 5
        elif "SUN" in text:
            return 6

    def get_weekdays(self, text):
        returned_weekdays = []
        if "MON" in text:
            returned_weekdays.append(self.weekDays[0])
        if "TUE" in text:
            returned_weekdays.append(self.weekDays[1])
        if "WED" in text:
            returned_weekdays.append(self.weekDays[2])
        if "THU" in text:
            returned_weekdays.append(self.weekDays[3])
        if "FRI" in text:
            returned_weekdays.append(self.weekDays[4])
        if "SAT" in text:
            returned_weekdays.append(self.weekDays[5])
        if "SUN" in text:
            returned_weekdays.append(self.weekDays[6])

        return returned_weekdays

    def get_list_of_weekdays_in_the_range(self, from_weekday, to_weekday):
        returned_list = []
        if 0 <= from_weekday <= 6 and 0 <= to_weekday <= 6:
            i = from_weekday
            while True:
                returned_list.append(self.weekDays[i])

                if i == to_weekday:
                    break
                elif i == 6:  # Go in the circle
                    i = 0
                else:
                    i += 1
        return returned_list

    def pick_weekdays(self, text):

        weekNumbers = re.findall("(\d*[1-5])\s*((ST)|(ND)|(RD)|(TH))", text)
        output_days_of_week = []
        output_weeks_of_month = []

        if "MON" in text or "TUE" in text or "WED" in text or "THU" in text or "FRI" in text or "SAT" in text or "SUN" in text or "EVERYDAY" in text:

            # Now check thoroughly
            words = text.split()
            has_weekdays = False

            for word in words:
                if word.strip() in self.weekDayWords:
                    has_weekdays = True
                    break

            if has_weekdays:  # has_weekdays is just to double check. It should not misunderstand TOWED for Wednesday because TOWED contains string WED

                if "THRU" in text or "THROUGH" in text or "TO" in text:
                    output_days_of_week = self.handle_weekday_range(text)

                elif "EVERYDAY" in text:
                    output_days_of_week = list(self.weekDays)

                elif len(weekNumbers) > 0: # Weekdays with week numbers. Eg. 2nd and 4th Monday
                    days_of_week, weeks_of_month = self.handle_weekdays_for_weeks_of_month(text)

                    output_weeks_of_month = weeks_of_month
                    output_days_of_week = days_of_week

                else:
                    days_of_week = self.get_weekdays(text)
                    if "EXCEPT" in text:
                        except_weekdays = []
                        for weekday in self.weekDays:
                            if weekday not in days_of_week:
                                except_weekdays.append(weekday)
                        output_days_of_week = except_weekdays
                    else:
                        output_days_of_week = days_of_week

        if len(output_days_of_week) == 0 and len(output_weeks_of_month) == 0:
            return None
        else:
            return WeekdaySpec.WeekdaySpec([], self.transform_weekdays_into_numbers(output_days_of_week), output_weeks_of_month)  # logic for months (The first parameter into the constructor of WeekdaySpec) is not in place yet

    def transform_weekdays_into_numbers(self, weekdays):
        returned_weekdays = []
        for weekday in weekdays:
            returned_weekdays.append(self.output_weekday_nums.get(weekday))
        return returned_weekdays

    def handle_weekdays_for_weeks_of_month(self, text):

        weeks = re.findall("(\d[1-5]?)", text)
        weeks_of_month = []
        for week in weeks:
            weeks_of_month.append(int(week))

        days_of_week = self.get_weekdays(text)
        return days_of_week, weeks_of_month

    def handle_weekday_range(self, text):
        words = text.split()
        is_range_word_reached = False
        from_weekday = ""
        to_weekday = ""
        for word in words:
            if "THRU" in word or "THROUGH" in word or "TO" in word:
                is_range_word_reached = True
                continue

            weekday = self.get_weekday_index(word)

            if weekday is not None:
                if is_range_word_reached is False:
                    from_weekday = weekday
                else:
                    to_weekday = weekday
        return self.get_list_of_weekdays_in_the_range(from_weekday, to_weekday)
