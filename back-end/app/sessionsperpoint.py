from flask import Blueprint, jsonify, Response, request,json
from .models import ChargingPoint, Charge, Transaction, Vehicle
import datetime
from .authorization import requires_auth
from .jsontocsv import json2csv
from flask import make_response
from sqlalchemy import and_
from flask_cors import cross_origin

bp = Blueprint("sessionsperpoint", __name__, url_prefix="/evcharge/api/SessionsPerPoint")

csv_first_row = ["Point", "PointOperator", "RequestTimestamp", "PeriodFrom", "PeriodTo", "NumberOfChargingSessions", "ChargingSessionsList"]


@bp.route('/<pointID>/<date_from>/<date_to>', methods=['GET'])
@requires_auth
@cross_origin(supports_credentials=True)
def sessionsperpoint(_,pointID,date_from,date_to):
    format = request.args.get('format')
    reqtime = request.args.get('time')
    csvbool = False
    if format == 'csv': csvbool = True
    try: dtf = datetime.datetime.strptime(date_from, '%Y-%m-%d')
    except: return make_response('Not valid date format (YYYY-MM-DD)', 400)
    try:
        dto = datetime.datetime.strptime(date_to, '%Y-%m-%d')
    except:
        return make_response('Not valid date format (YYYY-MM-DD)', 400)

    res = ChargingPoint.query.filter_by(id = pointID).first()
    if not res:
        return make_response('The Point ID is invalid', 402)

    sessionsquery1 = Charge.query.filter(Charge.chargingpoint_id == pointID).filter(Charge.date_.between(date_from,date_to)).order_by(Charge.date_).all()
    sessionsquery2 = sessionsquery1

    if not sessionsquery2:
        return make_response('There are no sessions for this point', 402)
    
    nocs = len(sessionsquery2)
    records = []
    index = 1
    for record in sessionsquery2:
        """
        pay = Transaction.query.filter_by(id=record.id).first()
        if not pay: return make_response('Transaction doesnt exist', 403)
        """
        v_type = Vehicle.query.filter(Vehicle.id == record.vehicle_id).first()
        if not v_type: return make_response('Vehicle doesnt exist', 402)
        extra = {"SessionIndex": index, "SessionID": str(record.id) , "StartedOn": str(record.connection_time),
                 "FinishedOn": str(record.disconnection_time), "Protocol": str(record.protocol),
                 "EnergyDelivered": str(record.kWhdelivered), #"Payment": str(pay.payment_method),
                 "VehicleType": str(v_type.type_)}
        records.append(extra)
        index += 1

    spp = [{"Point": str(res.id), "PointOperator": (res.operator_id), "RequestTimestamp": str(reqtime), "PeriodFrom": str(date_from),
    		 "PeriodTo": str(date_to), "NumberOfChargingSessions": str(nocs), "ChargingSessionsList": records }]

    if csvbool:
        csv_response = json2csv(spp, csv_first_row)
        return Response(csv_response, mimetype='text/csv')
    else:
        return Response(json.dumps(spp, sort_keys=False), mimetype='application/json')
    
