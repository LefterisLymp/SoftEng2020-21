import os
import pytest
import urllib3
from app.models import User
from werkzeug.datastructures import FileStorage
from .configuretest import client
urllib3.disable_warnings()

class Test_Admin(object):
	token = None

	@staticmethod
	def admin_token():
		return User.query.filter(User.role_ == 'admin').first().token

	@staticmethod
	def user_token():
		return User.query.filter(User.role_ == 'car_owner').first().token

	def test_health_check(self, client):
		rv = client.get('evcharge/api/healthCheck')
		assert rv.status_code == 200

	def Test_reset(self, client):
		rv = client.post('evcharge/api/admin/resetsessions')
		assert rv.status_code == 200

	def test_admin_login(self, client):
		rv = client.post('evcharge/api/login')
		assert rv.status_code == 401

		rv = client.post(('evcharge/api/login'),data={'username': 'Nikolas', 'password':'Nikolas'})
		assert rv.status_code == 200
		assert rv.json['token'] == User.query.filter(User.username == 'Nikolas').first().token


	def test_create_new_user(self,client):
		rv = client.post('evcharge/api/admin/usermod')
		assert rv.status_code == 404
		rv = client.post('evcharge/api/admin/usermod/'+'MakiChan'+'/'+'makis123',headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		assert User.query.filter(User.username == 'MakiChan').first() is not None
		assert User.query.filter(User.username == 'MakiChan').first().verify_password('makis123')
		assert User.query.filter(User.username == 'MakiChan').first().token is None

	def test_import_csv(self, client):
		file = os.path.join("C://Users//lefte//Desktop//charge.csv")
		my_file = FileStorage(
    		stream = open(file,"rb"),
    		filename= "charge.csv",
			content_type="text/csv",
		)
		rv = client.post(('evcharge/api/admin/system/sessionsupd'),
    		headers= {'X-OBSERVATORY-AUTH': User.query.filter(User.username == 'Lefteris').first().token},
    		data={"file": my_file}, content_type = "multipart/form-data")

	def test_sessions_per_point(self, client):
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155 Nullam Av._0/2020-04-13/2020-04-18'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155 Nullam Av._0/10-04-1020/2020-04-18'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 400
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155  Av._0/2020-04-13/2020-04-18'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 402
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155 Nullam Av._0/2020-04-13/2020-04-18'), headers={'X-OBSERVATORY-AUTH': 'undifined_token'})
		assert rv.status_code == 401
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155 Nullam Av._0/2020-04-13/'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerPoint/242-7155 Nullam Av._0/2020-04-18'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert  rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerPoint/2020-04-13/2020-04-18'), headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert  rv.status_code == 404

	def test_sessions_per_station(self, client):
		rv = client.get(('evcharge/api/SessionsPerStation/242-7155 Nullam Av./2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		rv = client.get(('evcharge/api/SessionsPerStation/242-7155 Nullam Av./10-04-1020/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 400
		rv = client.get(('evcharge/api/SessionsPerStation/242-  Av./2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 402
		rv = client.get(('evcharge/api/SessionsPerStation/242-7155 Nullam Av./2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': 'undifined_token'})
		assert rv.status_code == 401
		rv = client.get(('evcharge/api/SessionsPerStation/242-7155 Nullam Av./2020-04-13/'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerStation/242-7155 Nullam Av./2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerStation/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404

	def test_sessions_per_ev(self, client):
		rv = client.get(('evcharge/api/SessionsPerEV/1/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		rv = client.get(('evcharge/api/SessionsPerEV/1/10-04-1020/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 400
		rv = client.get(('evcharge/api/SessionsPerEV/h3sasd/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 402
		rv = client.get(('evcharge/api/SessionsPerEV/1/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': 'undifined_token'})
		assert rv.status_code == 401
		rv = client.get(('evcharge/api/SessionsPerEV/1/2020-04-13/'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerEV/1/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerEV/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404

	def test_sessions_per_provider(self, client):
		rv = client.get(('evcharge/api/SessionsPerProvider/1/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		rv = client.get(('evcharge/api/SessionsPerProvider/1/10-04-1020/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 400
		rv = client.get(('evcharge/api/SessionsPerProvider/x3d/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 400
		rv = client.get(('evcharge/api/SessionsPerProvider/1/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': 'undifined_token'})
		assert rv.status_code == 401
		rv = client.get(('evcharge/api/SessionsPerProvider/1/2020-04-13/'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerProvider/1/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404
		rv = client.get(('evcharge/api/SessionsPerProvider/2020-04-13/2020-04-18'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 404

	def test_get_user_info(self, client):
		rv = client.get('evcharge/api/admin/users/Cummings',headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
		temp = rv.json['message']
		assert temp['username'] == 'Cummings'
		assert temp['name'] == 'Oliver W. Guerra'
		assert temp['role'] == 'car_owner'

	def test_user_trying_admin_request(self,client):
		rv = client.get(('evcharge/api/admin/users'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 404

		rv = client.post(('evcharge/api/SessionsPerPoint'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 404

		rv = client.get(('evcharge/api/SessionsPerStation'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 404

		rv = client.get(('evcharge/api/SessionsPerEV'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 404

		rv = client.get(('evcharge/api/SessionsPerProvider'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 404

		rv = client.get(('evcharge/api/logout'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 405

		rv = client.get(('evcharge/api/admin/system/sessionsupd'), headers={'X-OBSERVATORY-AUTH': self.user_token()})
		assert rv.status_code == 405

	def test_admin_log_out(self,client):
		rv = client.post('evcharge/api/logout')
		assert rv.status_code == 401
		rv = client.post(('evcharge/api/logout'),headers={'X-OBSERVATORY-AUTH': self.admin_token()})
		assert rv.status_code == 200
