import re
import HourSpec

class HourPickerService:

    def __init__(self):
        pass

    def convert24(self, time_string):

        # Checking if last two elements of time
        # is AM and first two elements are 12
        if time_string[-2:] == "AM" and time_string[:2] == "12":
            return "00" + time_string[2:-2].strip()
            # remove the AM
        elif time_string[-2:] == "AM":
            return time_string[:-2].strip()

        # Checking if last two elements of time is PM and first two elements are 12
        elif time_string[-2:] == "PM" and time_string[:2] == "12":
            return time_string[:-2].strip()

        elif time_string[-2:] == "PM":
            # add 12 to hours and remove PM
            return str(int(time_string[:2]) + 12) + time_string[2:-2].strip()
        return ""

    def refine_time(self, time):
        time = time.strip().strip('.').strip(',').strip('-').strip(':')
        # print(time)
        if len(time) == 1:
            return "0" + str(time) + ":00"
        elif len(time) == 2 and str(time).find(".") == -1 and str(time).find(":") == -1:
            return str(time) + ":00"
        elif len(time) == 4 and (str(time)[1] in [".", ":"]):
            return "0" + str(time)
        elif len(time) == 5 and (str(time)[2] in [".", ":"]):
            return str(time)
        return ""

    def pick_hour_window(self, text):
        time_window = re.findall("(\d{1,2}[\.,:]?\d{0,2})[\s\.,:-]*(([AP]\.?[M]\.?)|([N]\.?[O]\.?[O]\.?[N]\.?)|([M]\.?[I]\.?[D]\.?[N]\.?[I]\.?[G]\.?[H]\.?[T]\.?))", text)
        # time_window = re.findall("(\d{1,2}[\.,:]?\d{0,2})\s*([AaPp]\.?[Mm]\.?)", text)
        if not time_window:
            return None

        refined_time = []
        for i in range(len(time_window)):
            refined_am_pm = str(time_window[i][1]).replace('.', '').replace("NOON", "PM").replace("MIDNIGHT", "AM")
            refined_time_values = self.refine_time(time_window[i][0])
            time_converted_24_hours = self.convert24(refined_time_values + refined_am_pm)
            refined_time.append(time_converted_24_hours)
            # print("\n i: " + str(i))
            # print(" raw value: " + time_window[i][0].strip())
            # print(" refined_am_pm: " + refined_am_pm)
            # print(" refined_time_values: " + refined_time_values)
            # print(" time_converted_24_hours: " + time_converted_24_hours)

        return HourSpec.HourSpec(refined_time[0], refined_time[1])

