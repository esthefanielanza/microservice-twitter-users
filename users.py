import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import sys

app = Flask(__name__)
# app.config["DEBUG"] = True
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)

db.create_all()


@app.route('/')
def test():
    all_users = User.query.all()
    result = user_schemas.dump(all_users)
    return jsonify({'users': result.data})


@app.route('/create', methods=['POST'])
def welcome():
    username = request.json['username']
    email = request.json['email']
    print('username', username)
    print('email', email)
    new_user = User(username, email)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


if __name__ == '__main__':
    app.run()

# @app.route('/register', methods=["POST"])
# def register():
#     DATABASE_URL = os.environ['DATABASE_URL']
#     connection = psycopg2.connect(DATABASE_URL, sslmode='require')
#     cur = connection.cursor()
#     try:
#       cur.execut("""SELECT * FROM Users"""))

#     except Exception as e:
#       print("Failed", e)
#       sys.stdout.flush()
#     return 'Success!'
