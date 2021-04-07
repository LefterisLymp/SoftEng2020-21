class Config(object):
    SECRET_KEY = '35x39012dsgajgmq65sg345'
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{pw}@{url}/{db}'.format(user='root', pw='*JbS@K4nh8znE7;F',url='localhost', db='ev_charge')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False