from flask import request, jsonify
from app import app
from app.service.MailService import MailService
from datetime import datetime

@app.route('/mail/save', methods=['POST'])
def save_email():
    data = request.get_json()
    email = data.get('email')
    subject = data.get('subject')
    content = data.get('content')
    sended = data.get('sended')

    if not all([email, subject, content, sended]):
        return jsonify({'message': 'Missing required fields'}), 422
    
    try:
        sended = datetime.strptime(sended, '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({'message': 'Invalid datetime format for sended'}), 422
    
    new_mail = MailService.post(email=email, subject=subject, content=content, sended=sended)
    return({
            "message": 'Email has been save', 
            'id': new_mail.id
            }), 201

@app.route('/mail', methods=['GET'])
def get_all_email():
    mails = MailService.get()
    return jsonify({
        "message": "data found",
        "data": [{
        'email': mail.email,
        'subject': mail.subject,
        'content': mail.content,
        'content': mail.content, 
        'sended': mail.sended
    } for mail in mails]}), 200

@app.route('/', methods=['GET'])
def index():
    return 'tester...'