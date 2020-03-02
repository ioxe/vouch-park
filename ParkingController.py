from flask import Flask, json
from service.ParkingRuleService import ParkingRuleService

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():

    result = ParkingRuleService.checkParkingSign("", None)
    return json.dumps(result)
if __name__ == '__main__':
    api.run()