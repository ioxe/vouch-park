import ParkingRule
import HourPickerService
import DatePickerService
import WeekdayPickerService
import DurationAndParkingIndicatorPickerService


class ParkingRuleService:
    def checkParkingSign(self, text_arr):

        hour_picker_Service = HourPickerService.HourPickerService()
        date_picker_Service = DatePickerService.DatePickerService()
        weekday_picker_Service = WeekdayPickerService.WeekdayPickerService()
        duration_and_parking_indicator_picker_Service = DurationAndParkingIndicatorPickerService.DurationAndParkingIndicatorPickerService()

        returned_parking_rule = ParkingRule.ParkingRule([], [], [], 0, 1)  # parking_indicator -> default is parking (1)

        sanitized_beginning_of_sign = str(text_arr[0]).strip().upper()

        returned_parking_rule.duration_minutes, returned_parking_rule.parking_indicator = duration_and_parking_indicator_picker_Service.pick_duration_and_parking_indicator(
            sanitized_beginning_of_sign)

        for text in text_arr:
            # trim and upper case
            sanitized_text = str(text).strip().upper()

            hour_spec = hour_picker_Service.pick_hour_window(sanitized_text)
            if hour_spec is not None:
                returned_parking_rule.hour_specs.append(hour_spec)

            date_spec = date_picker_Service.pick_dates(sanitized_text)
            if date_spec is not None:
                returned_parking_rule.date_specs.append(date_spec)

            weekday_spec = weekday_picker_Service.pick_weekdays(sanitized_text)
            if weekday_spec is not None:
                returned_parking_rule.weekday_specs.append(weekday_spec)

        return returned_parking_rule
