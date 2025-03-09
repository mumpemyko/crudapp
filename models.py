from app import db


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable= False)
    email = db.Column(db.Text)
    contact = db.Column(db.Integer)
    
    def __repr__(self):
        return f'User with name {self.name}'
    
    