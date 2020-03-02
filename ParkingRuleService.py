from datetime import datetime
import re
import HourSpec
import ParkingRule
import HourPickerService


class ParkingRuleService:

    def __init__(self):
        pass


    def checkParkingSign(self, text, date_time):

        # trim and upper case
        sanitized_text = str(text).strip().upper()

        # duration
        duration = None

        # No parking sigs
        NoParkingSigns = ["NO PARKING", "NO STOPPING", "TOW-AWAY NO", "RESERVED", "PRIVATE PARKING",
                          "CUSTOMER PARKING ONLY"]
        for sign in NoParkingSigns:
            if str(sanitized_text).startswith(sign):
                sanitized_text = sanitized_text.replace(sign, "")
                duration = 0

        # gets time window
        hour_specs = HourPickerService.HourPickerService.pick_hour_windows(sanitized_text)

        parking_rule = ParkingRule.ParkingRule(0, 0, hour_specs, duration, 0)

        print("parking_rule: ", parking_rule.hour_specs[0].from_hour, " , " , parking_rule.hour_specs[0].to_hour)

        # return parking_rule


parkingRuleService = ParkingRuleService()
parkingRuleService.checkParkingSign(text="NO PARKING 12:01 A.M. TO 2 A.M. TUE THRU THUR STREET CLEANING", date_time=datetime.now())
parkingRuleService.checkParkingSign(text="NO PARKING 2:00 p.M. TO 2 a.M. TUE THRU THUR STREET CLEANING", date_time=datetime.now())
# checkParkingSign(text= "2 HOUR PARKING 8AM-6PM MON THRU FRI EXCEPT VEHICLES WITH X PERMIT", date_time = datetime.now())
