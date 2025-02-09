from flask_restful import Resource, reqparse
from flask import request
from app.models import Person
from app import db
from sqlalchemy.exc import SQLAlchemyError

class SearchResource(Resource):
    def get(self):
        surname = request.args.get('surname', type=str)
        name = request.args.get('name', type=str)
        patronymic = request.args.get('patronymic', type=str)
        date_of_birth = request.args.get('date_of_birth', type=str)
        gender = request.args.get('gender', type=int)

        query = Person.query

        if surname:
            query = query.filter_by(surname=surname)
        if name:
            query = query.filter_by(name=name)
        if patronymic:
            query = query.filter_by(patronymic=patronymic)
        if date_of_birth:
            query = query.filter_by(date_of_birth=date_of_birth)
        if gender:
            query = query.filter_by(gender=gender)


        people = query.all()

        return {
            'peoples': [{
                'id_ern': person.id_ern,
                'surname': person.surname,
                'name': person.name,
                'patronymic': person.patronymic,
                'date_of_birth': str(person.date_of_birth),
                'gender': person.gender
            } for person in people]
        }, 200

class GetByIdResource(Resource):
    def get(self):
        id_ern = request.args.get('id_ern', type=int)

        if id_ern is None:
            return {"message": "Missing 'id_ern' parameter"}, 400

        person = Person.query.filter_by(id_ern=id_ern).first()

        if not person:
            return {"message": "Person not found"}, 404

        return {
            'person': {
                'id_ern': person.id_ern,
                'surname': person.surname,
                'name': person.name,
                'patronymic': person.patronymic,
                'date_of_birth': str(person.date_of_birth),
                'gender': person.gender
            }
        }, 200

class CreatePersonResource(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "No JSON data provided"}, 400

        try:
            new_person = Person(
                surname=str(data.get('surname', '')).strip(),
                name=str(data.get('name', '')).strip(),
                patronymic=str(data.get('patronymic', '')).strip(),
                date_of_birth=data.get('date_of_birth'),
                gender=int(data.get('gender'))
            )
            db.session.add(new_person)
            db.session.commit()
            return {"message": "Person created", "id": new_person.id_ern}, 201
        except (ValueError, SQLAlchemyError) as e:
            db.session.rollback()  # Откатить транзакцию при ошибке
            return {"message": f"Database error: {str(e)}"}, 500