from flask import Blueprint, jsonify, Response, request,json
from .models import Charge, Transaction, Vehicle
import datetime
from .authorization import requires_auth
from .jsontocsv import json2csv
from flask import make_response
from flask_cors import cross_origin
from sqlalchemy import and_

bp = Blueprint("sessionsperev", __name__, url_prefix="/evcharge/api/SessionsPerEV")

csv_first_row = ["VehicleID", "RequestTimestamp", "PeriodFrom", "PeriodTo", "NumberOfVisitedPoints","NumberOfVehicleChargingSessions", "VehicleChargingSessionsList"]

@bp.route('/<vehicleID>/<date_from>/<date_to>', methods=['GET'])
@cross_origin(supports_credentials=True)
@requires_auth
def sessionsperev(_,vehicleID,date_from,date_to):
    format = request.args.get('format')
    reqtime = datetime.datetime.now().timestamp()
    csvbool = False
    if format == 'csv': csvbool = True

    try: 
        dtf = datetime.datetime.strptime(date_from, '%Y-%m-%d')
    except: 
        return make_response('Not valid date format (YYYY-MM-DD)', 400)

    try:
        dto = datetime.datetime.strptime(date_to, '%Y-%m-%d')
    except:
        return make_response('Not valid date format (YYYY-MM-DD)', 400)

    res = Vehicle.query.filter_by(id = vehicleID).first()
    if not res:
        return make_response('The Vehicle ID is invalid', 402)

    sessionsquery1 = Charge.query.filter(Charge.vehicle_id == vehicleID).filter(Charge.date_.between(date_from,date_to)).order_by(Charge.date_).all()

    if not sessionsquery1:
        return make_response('There are no sessions for this vehicle', 402)
    

    TotalEnergyConsumed = 0
    for cur in sessionsquery1:
        TotalEnergyConsumed = TotalEnergyConsumed + cur.kWhdelivered;

    cursors = []
    for cursor in sessionsquery1:
        if cursor.chargingpoint_id not in cursors:
            cursors.append(cursor.chargingpoint_id)

    NumberOfVisitedPoints = len(cursors)

    NumberOfVehicleChargingSessions = len(sessionsquery1)

    records = []
    index = 1
    for record in sessionsquery1:
        """
        pay = Transaction.query.filter_by(id=record.id).first()
        if not pay: return make_response('Transaction doesnt exist', 403)
        """
        v_type = Vehicle.query.filter(Vehicle.id == record.vehicle_id).first()
        if not v_type: return make_response('Vehicle doesnt exist', 402)

        extra = {"SessionIndex": index, "SessionID": str(record.id) , "EnergyProvider": str(record.provider_id),"StartedOn": str(record.connection_time),
                 "FinishedOn": str(record.disconnection_time), "EnergyDelivered": str(record.kWhdelivered), "PricePolicyRef": str("null"),
                 "CostPerKWh": str(record.cost_per_kwh),"SessionCost":str(record.total_cost)}
        records.append(extra)
        index += 1

    spp = [{"VehicleID": str(res.id), "RequestTimestamp": (reqtime), "PeriodFrom": str(date_from), "PeriodTo": str(date_to),
    		 "TotalEnergyConsumed": str(TotalEnergyConsumed), "NumberOfVisitedPoints": str(NumberOfVisitedPoints), "NumberOfVehicleChargingSessions": str(NumberOfVehicleChargingSessions),"VehicleChargingSessionsList": records}]

    if csvbool:
        csv_response = json2csv(spp, csv_first_row)
        return Response(csv_response, mimetype='text/csv')
    else:
        return Response(json.dumps(spp, sort_keys=False), mimetype='application/json')
