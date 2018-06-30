from app import app
from flask import request
from app import db
from Lawyer import Lawyer


@app.route('/')
def index():
    firstmember = Lawyer.query.first()
    return '<h1> Here you can find device list! </h1>'


@app.route('/lawyer')
def view():
    lawyer = Lawyer.query.first()
    if lawyer is not None:
        return str('First member name \n' + lawyer.to_string())
    else:
        return "Device with this id does not exist"


@app.route('/lawyer/<id>')
def get_lawyer(id):
    lawyer = Lawyer.query.get(id)
    if lawyer is not None:
        return lawyer.to_string()
    else:
        return "Device with this id does not exist"


@app.route('/lawyer', methods=['POST'])
def add_lawyer():
    id = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']

    lawyer = Lawyer()
    lawyer.id = id
    lawyer.name = name
    lawyer.lastname = lastname

    db.session.add(lawyer)
    db.session.commit()

    return lawyer.to_string()


@app.route('/lawyer/<id>', methods=['PUT'])
def lawyer_update(id):
    name = request.json['name']

    new_lawyer = Lawyer.query.get(id)
    new_lawyer.id = id
    new_lawyer.name = name
    db.session.commit()

    return new_lawyer.to_string()


@app.route('/lawyer/<id>', methods=['DELETE'])
def lawyer_delete(id):
    lawyer = Lawyer.query.get(id)
    db.session.delete(lawyer)
    db.session.commit()
    return str("Deleting succssesfull")
