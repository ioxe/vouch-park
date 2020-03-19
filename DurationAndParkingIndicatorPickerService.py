import re


class DurationAndParkingIndicatorPickerService:

    def pick_duration_and_parking_indicator(self, text):
        NoParkingSigns = ["NO PARKING", "NO STOPPING", "TOW-AWAY", "RESERVED", "PRIVATE PARKING", "STOPPING","CUSTOMER PARKING ONLY"]

        payToPark = "PAY TO PARK"

        parking_indicator = 1  # default is parking (1)
        duration_minutes = None

        # check if no parking
        for sign in NoParkingSigns:
            if text.startswith(sign):
                parking_indicator = 0
                duration_minutes = 0
                break

        # check if pay to park
        if text.startswith(payToPark):
            parking_indicator = 2
            duration_minutes = 0

        # Find the duration if any if the parking_indicator is Parking ()
        if parking_indicator == 1:
            duration_details = re.findall("(\d{1,2}\s+(HOUR|HOURS|MINUTE|MINUTES|MIN|MIN\.)\s+(PARKING|MAXIMUM|LIMIT))", text)

            if not duration_details or len(duration_details) == 0 or len(duration_details[0]) == 0:
                duration_minutes = 0
            else:
                duration_minutes = int(str(duration_details[0][0]).split()[0].strip())
                if str(duration_details[0][1]).strip() in ["HOUR", "HOURS"]:  # duration is in hours
                    duration_minutes *= 60
        return duration_minutes, parking_indicator
