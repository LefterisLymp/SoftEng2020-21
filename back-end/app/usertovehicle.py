from flask import Blueprint, jsonify, Response, request,json
from .models import User, Vehicle
from .authorization import requires_auth
from flask import make_response
from sqlalchemy import and_
from flask_cors import cross_origin

bp = Blueprint("usertovehicle", __name__, url_prefix="/evcharge/api/UserToVehicle")

@bp.route('/<userID>', methods=['GET'])
@cross_origin(supports_credentials=True)
#@requires_auth
def usertovehicle(userID):
    res = User.query.filter_by(id = userID).first()
    if not res:
        return make_response('The User ID is invalid or doesnt exist', 402)

    Vehicles = Vehicle.query.filter_by(owner_id = userID).all()

    records=[]
    for record in Vehicles:
        extra = {"id": str(record.id), "brand": str(record.brand), "type_": str(record.type_),
                 "charger_type": str(record.charger_type), "usable_battery_size": str(record.usable_battery_size),
                 "average_consumption": str(record.average_consumption)}
        records.append(extra)

    return Response(json.dumps(records, sort_keys=False), mimetype='application/json')