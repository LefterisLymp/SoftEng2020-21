import pandas as pd
from flask import make_response, Response
from flask import Blueprint, jsonify
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from functools import wraps
from .models import User, Charge, db
import datetime

SECRET_KEY = '35x39012dsgajgmq65sg345'

bp = Blueprint("auth", __name__, url_prefix="/evcharge/api")

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-OBSERVATORY-AUTH' in request.headers:
            token = request.headers['X-OBSERVATORY-AUTH']

        if not token:
            return make_response('Not authorized', 401)
        try:
        # if True:
            print(token)
            data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            print(2)
            print(data['id'])
            current_user = User.query.filter_by(id=data['id']).first()
            if current_user.token == token:
                print(current_user.is_admin())
                if current_user.is_admin(): return f(current_user, *args, **kwargs)
                else: return make_response('Not authorized', 401)

            else:
                if current_user.token is None:
                    return make_response('User has been logged out (Not authorized)', 401)
                else:
                    return make_response('Token is invalid (Not authorized)', 401)
        except Exception as e:
            print(e)
            return make_response('Not authorized', 401)

    return decorated


@bp.route('/admin/usermod/<user_username>/<password>', methods=['POST'])
@requires_auth
def register(current_user, user_username, password):
    if not current_user.is_admin(): return jsonify({'message': 'User is not authorized'})
    unique = User.query.filter_by(username=user_username).first()
    if not unique is None:
        unique.hash_password(password)
        db.session.add(unique)
        db.session.commit()
        return jsonify({'message': 'password modified'})
    new_user = User(username=user_username)
    new_user.hash_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'new user created'})




@bp.route('/admin/users/<user_username>', methods=['GET'])
@requires_auth
def show(current_user, user_username):
    if not current_user.is_admin:
        return make_response('User is not an admin (Not authorized)', 401)
        # return jsonify({'message': 'cant complete that,not an admin'})
    if request.method == 'GET':
        user = User.query.filter_by(username=user_username).first()
        if not user:
            return make_response('There is no user with this username', 400)
        result = {'username': user.username, 'name': user.name_, 'role': user.role_}
        return jsonify({"message": result})

@bp.route('/login', methods=['POST'])
def login():
    auth = request.form.to_dict()
    if not auth or not auth['username'] or not auth['password']:
        return make_response('Could not verify', 401)
    user = User.query.filter_by(username=auth['username']).first()
    if not user:
        return make_response('Could not verify', 401)
    print(generate_password_hash(auth['password']))
    if check_password_hash(user.password_hash, auth['password']):
        token = jwt.encode(
            {'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10)},
            SECRET_KEY)
        user.update_token(token.decode('UTF-8'))
        db.session.commit()
        return jsonify({"id": str(user.id),"token": token.decode('UTF-8')})
    return make_response('Could not verify', 401)


@bp.route('/logout', methods=['POST'])
@requires_auth
def logout(current_user):
    current_user.token = None
    db.session.commit()
    return make_response('', 200)


@bp.route('/admin/system/sessionsupd', methods=['POST'])
@requires_auth
def importcsv(current_user):
    if not current_user.is_admin:
        return make_response('User is not an admin (Not authorized)', 401)
        # return jsonify({'message': 'cant complete that,not an admin'})
    file = request.files['file']
    if file is None:
        return make_response('There is no file', 400)
        # return jsonify({"error": "Bad request"}), 400
    try:
        reader = pd.read_csv(file, ';')
    except:
        return make_response('Couldn\'t read file', 400)
        # return jsonify({"error": "Bad request"}), 400
    counter = 0
    totalRecordsInFile = reader.shape[0]
    recordsindatabase = Charge.query.count()
    for row in reader.itertuples():
        try:
            cid = getattr(row, 'Id')
            cchargingpoint_id = getattr(row, 'ChargingPointId')
            cvehicle_id = getattr(row, 'VehicleId')
            ckWhdelivered = getattr(row, 'kWhDelivered')
            cconnection_time = getattr(row, 'ConnectionTime')
            cdisconnection_time = getattr(row, 'DisconnectionTime')
            cdate_ = getattr(row, 'Date')
            cprovider_id = getattr(row, 'ProviderId')
            cprice_policy_ref = getattr(row, 'PricePolicyRef')
            ccost_per_kwh = getattr(row, 'CostPerkWh')
            cprotocol = getattr(row, 'Protocol')
            ctotal_cost = getattr(row, 'TotalCost')
            query = Charge(id=cid, chargingpoint_id = cchargingpoint_id, vehicle_id = cvehicle_id, kWhdelivered = ckWhdelivered,
                           connection_time = cconnection_time, disconnection_time = cdisconnection_time, date_ = cdate_,
                           provider_id = cprovider_id, price_policy_ref = cprice_policy_ref, cost_per_kwh = ccost_per_kwh,
                           protocol = cprotocol, total_cost = ctotal_cost)
            db.session.add(query)
            db.session.commit()
        except Exception:
            continue
        counter += 1

    return jsonify({"totalRecordsInFile": totalRecordsInFile, "totalRecordsImported": counter, "totalRecordsInDatabase": recordsindatabase + counter})


@bp.route('/healthCheck', methods=['GET'])
def health_check():
    try:
        db.session.execute('DELETE FROM dummy WHERE first ="Lefo"')
        return jsonify({'status': 'OK'})
    except:
        return make_response('There is no connection with database', 400)
        # return jsonify({'status': 'no connection with database'})


@bp.route('/admin/resetsessions', methods=['POST'])
def reset():
    try:
        db.session.query(Charge).delete()
        db.session.commit()
        admin = User(username='admin', role_ = 'admin')
        admin.hash_password('petrol4ever')
        db.session.add(admin)
        db.session.commit()
        return jsonify({'status': 'OK'})
    except:
        db.session.rollback()
        return jsonify({'status': 'failed'})