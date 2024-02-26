from flask_mail import Message

from app.model.Mail import Mail
from app import db, mail
from datetime import datetime, date
from typing import List

class MailService():
    @staticmethod
    def post(email: str, subject: str, content: str, sended: datetime) -> Mail:
        data_mail = Mail(email=email, subject=subject, content=content, sended=sended)
        db.session.add(data_mail)
        db.session.commit()
        return data_mail
    
    @staticmethod
    def get() -> List[Mail]:
        return Mail.query.all()
    
    @staticmethod
    def send():
        today = datetime.now().strftime('%Y-%m-%d %H:%M')
        mail_send_today = Mail.query.filter(Mail.sended == today).first()

        if mail_send_today:
            msg = Message(mail_send_today.subject, sender='projtanjoy@gmail.com', recipients=[mail_send_today.email])
            msg.body = mail_send_today.content
            mail.send(msg)
            return "Mail Sent..."
        else:
            return "No mail to send today."

