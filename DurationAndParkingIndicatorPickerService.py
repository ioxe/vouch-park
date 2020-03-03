import re


class DurationAndParkingIndicatorPickerService:

    def pick_duration_and_parking_indicator(self, text):
        NoParkingSigns = ["NO PARKING", "NO STOPPING", "TOW-AWAY", "RESERVED", "PRIVATE PARKING", "STOPPING","CUSTOMER PARKING ONLY"]

        payToPark = "PAY TO PARK"

        parking_indicator = 1  # default is parking (1)
        duration = None

        # check if no parking
        for sign in NoParkingSigns:
            if text.startswith(sign):
                parking_indicator = 0
                duration = 0
                break

        # check if pay to park
        if text.startswith(payToPark):
            parking_indicator = 2
            duration = 0

        # Find the duration if any if the parking_indicator is Parking ()
        if parking_indicator == 1:
            duration_details = re.findall("(\d{1,2}[\s+](HOUR|HOURS)[\s+]PARKING)", text)

            if not duration_details or len(duration_details) == 0 or len(duration_details[0]) == 0:
                duration = 0
            else:
                duration = int(str(duration_details[0][0]).split()[0].strip())

        return duration, parking_indicator
