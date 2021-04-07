from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(64), nullable=False, unique=True)
    name_ = db.Column(db.VARCHAR(64), unique=False)
    password_hash = db.Column(db.VARCHAR(256))
    token = db.Column(db.String(256), default=None, unique=True)
    role_ = db.Column(db.VARCHAR(64), nullable=False)

    def update_token(self, newToken):
        self.token = newToken

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self): return self.role_ == "admin"

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.VARCHAR(64))
    type_ = db.Column(db.VARCHAR(64))
    charger_type = db.Column(db.VARCHAR(64), unique=False)
    usable_battery_size = db.Column(db.Integer, unique=False)
    average_consumption = db.Column(db.Integer, unique=False)
    owner_id = db.Column(db.Integer, unique=False)

class Charge(db.Model):
    __tablename__ = 'Charge'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chargingpoint_id = db.Column(db.VARCHAR(64))
    vehicle_id = db.Column(db.Integer)
    kWhdelivered = db.Column(db.Integer)
    connection_time = db.Column(db.TIMESTAMP)
    disconnection_time = db.Column(db.TIMESTAMP)
    date_ = db.Column(db.Date)
    provider_id = db.Column(db.Integer)
    price_policy_ref = db.Column(db.VARCHAR(64))
    cost_per_kwh = db.Column(db.Numeric(5, 2))
    protocol = db.Column(db.VARCHAR(64))
    total_cost = db.Column(db.Numeric(5,2))

class Transaction(db.Model):
    __tablename__ = 'Transaction_'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    charge_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(5, 2))
    points = db.Column(db.Integer)
    payment_method = db.Column(db.VARCHAR(64))
    date_ = db.Column(db.Date)

class Provider(db.Model):
    __tablename__ = 'Provider'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_ = db.Column(db.VARCHAR(64))

class ChargingPoint(db.Model):
    __tablename__ = 'ChargingPoint'
    id = db.Column(db.VARCHAR(64), primary_key=True)
    operator_id = db.Column(db.VARCHAR(64))
#    site_id = db.Column(db.Integer)
#    space_id = db.Column(db.String(64))
    station_id = db.Column(db.VARCHAR(64))
    charger_type = db.Column(db.Integer)

class Station(db.Model):
    __tablename__ = 'Station'
    id = db.Column(db.VARCHAR(64), primary_key=True)
    manager_id = db.Column(db.VARCHAR(64))
