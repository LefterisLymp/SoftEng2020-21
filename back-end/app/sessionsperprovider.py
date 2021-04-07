from flask import Blueprint, jsonify, Response, request,json
from .models import Provider,Charge,Station,ChargingPoint
import datetime
from .authorization import requires_auth
from .jsontocsv import json2csv
from flask import make_response
from sqlalchemy import and_
from flask_cors import cross_origin

bp = Blueprint("sessionsperprovider", __name__, url_prefix="/evcharge/api/SessionsPerProvider")

csv_first_row = ["ProviderID","ProviderName","StationID","SessionID","VehicleID","StartedOn","FinishedOn","EnergyDelivered","PricePolicyRef","CostPerKWh","TotalCost"]


@bp.route('/<providerID>/<date_from>/<date_to>', methods=['GET'])
@cross_origin(supports_credentials=True)
@requires_auth
def sessionsperpoint(_,providerID,date_from,date_to):
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

    res = Provider.query.filter_by(id = providerID).first()
    if not res:
        return make_response('The Provider ID is invalid or doesnt exist', 400)
    res_id = res.id
    res_name = res.name_

    sessionsquery1 = Charge.query.filter(Charge.provider_id == providerID).order_by(Charge.date_).filter(Charge.date_.between(date_from,date_to)).all()
    sessionsquery2 = sessionsquery1

    if not sessionsquery2:
        return make_response('There are no sessions for this provider', 402)
    
    records = []
    for record in sessionsquery2:
        staid = ChargingPoint.query.filter_by(id = record.chargingpoint_id).first()
        if not staid: return make_response('Station doesnt exist', 402)

        """
        pay = Transaction.query.filter_by(id=record.id).first()
        if not pay: return make_response('Transaction doesnt exist', 403)
        """
        extra = {"ProviderID":str(res_id),"ProviderName":str(res_name),"StationID":str(staid.station_id),
        "SessionID":str(record.id),"VehicleID":str(record.vehicle_id), "StartedOn":str(record.connection_time),
        "FinishedOn":str(record.disconnection_time),"EnergyDelivered":str(record.kWhdelivered),
        "PricePolicyRef":str("null"),"CostPerKWh":str(record.cost_per_kwh),"TotalCost":str(record.total_cost)}
        records.append(extra)

    if csvbool:
        csv_response = json2csv(records, csv_first_row)
        return Response(csv_response, mimetype='text/csv')
    else:
        return Response(json.dumps(records, sort_keys=False), mimetype='application/json')
