from users import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  login = db.Column(db.String(30), unique=True)

  def __init__(self, login):
    self.login = login
  
  def __repr__(self):
    return '<Login %r>' % self.name