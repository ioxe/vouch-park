from json import JSONEncoder


class ParkingRuleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
