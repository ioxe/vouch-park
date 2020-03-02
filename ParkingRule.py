class ParkingRule:
    def __init__(self, date_specs, weekday_specs, hour_specs, duration, holidays):
        self.date_specs = date_specs
        self.weekday_specs = weekday_specs
        self.hour_specs = hour_specs
        self.duration = duration
        self.holidays = holidays

    def display_parking_rule(self):
        var = "Date Specs: ", self.date_specs, ", Weekday specs: ", self.weekday_specs, ", Hour Spec: ", self.hour_specs, ", Duration: ", self.duration, ", Holidays: ", self.holidays
