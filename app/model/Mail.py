from app import db
from datetime import datetime

class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sended = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "<Mail {}>".format(self.id)
    
"""
if u use postgre or mysql replace id to biginteger
"""