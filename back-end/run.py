from flask import Flask
from app import create_app
from app.models import db
from flask_cors import cross_origin

app = create_app()

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def hello_world():
    return 'Success! Hello World! So happy here in Flask!'

if __name__ == "__main__":
    #app.run(host='127.0.0.1', debug=True, port=8765, ssl_context='adhoc')
    app.run()