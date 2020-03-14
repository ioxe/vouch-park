from flask import Flask, request, jsonify
import ParkingRuleService
import ParkingRuleEncoder

api = Flask(__name__)


@api.route('/get_parking_rules', methods=['POST'])
def get_parking_Rules():
    parking_rule_service = ParkingRuleService.ParkingRuleService()

    req_data = request.get_json()
    parking_rule = parking_rule_service.checkParkingSign(req_data)

    parking_rule_json = ParkingRuleEncoder.ParkingRuleEncoder().encode(parking_rule)
    return jsonify(parking_rule_json)


if __name__ == '__main__':
    api.run()
