from flask import Blueprint, jsonify, Response, request,json
from .models import ChargingPoint, Charge, Station, Vehicle
import datetime
from .authorization import requires_auth
from .jsontocsv import json2csv
from flask import make_response
from flask_cors import cross_origin

bp = Blueprint("sessionsperstation", __name__, url_prefix="/evcharge/api/SessionsPerStation")

csv_first_row = ["StationID", "Operator", "RequestTimestamp", "PeriodFrom", "PeriodTo", "TotalEnergyDelivered", "NumberOfChargingSessions","NumberOfActivePoints","SessionsSummaryList"]

@bp.route('/<stationID>/<date_from>/<date_to>', methods=['GET'])
@requires_auth
@cross_origin(supports_credentials=True)
def sessionsperpoint(_,stationID,date_from,date_to) :
    format = request.args.get('format')
    reqtime = request.args.get('time')
    csvbool = False

    if format == 'csv': csvbool = True
    try:
        dtf = datetime.datetime.strptime(date_from, '%Y-%m-%d')
    except:
        return make_response('Not valid date format (DD-MM-YYYY)', 400)
    try:
        dto = datetime.datetime.strptime(date_to, '%Y-%m-%d')
    except:
        return make_response('Not valid date format (DD-MM-YYYY)', 400)

    res = Station.query.filter_by(id=stationID).first()
    if not res:
        return make_response('No results for this station and this period.', 402)

    pointsquery = ChargingPoint.query.filter_by(station_id = stationID).all()
    cursors = []
    for cursor in pointsquery:
        cursors.append(cursor.id)

    sessionsquery1 = Charge.query.filter(Charge.chargingpoint_id.in_(cursors)).filter(Charge.date_.between(date_from, date_to)).order_by(Charge.chargingpoint_id).all()
    sessionsquery2 = sessionsquery1
    
    if not sessionsquery2:
        return make_response('There are no sessions for this Station', 402)

    nocs = len(sessionsquery2)
    
    #pointsquery2 = ChargingPoint.query.filter_by(station_id = stationID).all()
    cursors2 = []
    for cursor2 in sessionsquery1:
        if cursor2.chargingpoint_id not in cursors2:
            cursors2.append(cursor2.chargingpoint_id)
    print(cursors2)
    #activepointsquery = Charge.query.filter(Charge.chargingpoint_id.in_(cursors2)).filter(Charge.date_.between(date_from, date_to)).order_by(Charge.date_).all()
    noap = len(cursors2)
    ted = 0
    for c in sessionsquery1:
        ted += c.kWhdelivered

    records = []
    car_records = []
    for record in cursors2:
        pointquery = Charge.query.filter_by(chargingpoint_id = record).filter(Charge.date_.between(date_from, date_to)).all()

        pointses = 0
        enrdel = 0
        for x in pointquery:
            pointses += 1
            enrdel += x.kWhdelivered
            car_id = x.vehicle_id
            carquery = Vehicle.query.filter_by(id = car_id).first()
            car_json = {"VehicleId": str(carquery.id), "VehicleBrand": str(carquery.brand)}
            car_records.append(car_json)
        extra = {"PointID": str(record), "PointSessions": str(pointses) , "EnergyDelivered": str(enrdel), "Vehicles": car_records}
        records.append(json.dumps(extra))

    spp = [{"StationID": str(res.id), "Operator": (res.manager_id), "RequestTimestamp": str("null"), "PeriodFrom": str(date_from),
             "PeriodTo": str(date_to), "TotalEnergyDelivered": str(ted), "NumberOfChargingSessions": str(nocs),"NumberOfActivePoints": str(noap),
            "SessionsSummaryList": records}]


    if csvbool:
        csv_response = json2csv(spp, csv_first_row)
        return Response(csv_response, mimetype='text/csv')
    else:
        return Response(json.dumps(spp, sort_keys=False), mimetype='application/json')
