import pytest
from flask import Flask
from app.models import db, User, Charge
from app.authorization import reset
from app import create_app

@pytest.fixture(scope="class",params=['mysql://root:Ro0t_KlM1!@127.0.0.1/testdb'],autouse=True)
def client(request):
	app = create_app()
	app.testing = True
	app.config['SQLALCHEMY_DATABASE_URI'] = request.param
	app.config['SECRET_KEY'] = '35x39012dsgajgmq65sg345'
	app.config['SQLALCHEMY_ECHO'] = False
	with app.app_context():
		db.create_all()
		yield app.test_client()
