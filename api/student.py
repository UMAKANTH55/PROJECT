# api/student.py
from flask_restx import Namespace, Resource, fields
from models.student import Student
from app import db

#Create a namespace
student_ns = Namespace('student', description='Student operations')
#Define the model for API operations
student_model = student_ns.model('Student', {
    'id': fields.Integer(readOnly=True, description='The student unique identifier'),
    'name': fields.String(required=True, description='Student Name'),
    'roll_no': fields.String(required=True, description='Roll No'),
    'course': fields.String(required=True, description='Course')
})
#Defining GET,POST methods with the API endpoint
@student_ns.route('/')
class StudentResource(Resource):
    @student_ns.marshal_with(student_model, as_list=True)
    def get(self):
        students = Student.query.all()
        return students

    @student_ns.expect(student_model)
    @student_ns.marshal_with(student_model, code=201)
    def post(self):
        data = student_ns.payload
        student = Student(**data)
        db.session.add(student)
        db.session.commit()
        return student, 201
#Defining GET,PUT,DELETE methods with the API endpoint using id
@student_ns.route('/<int:id>')
class StudentDetailResource(Resource):
    @student_ns.marshal_with(student_model)
    def get(self, id):
        student = Student.query.get(id)
        return student

    @student_ns.expect(student_model)
    @student_ns.marshal_with(student_model)
    def put(self, id):
        data = student_ns.payload
        student = Student.query.get(id)
        student.name = data['name']
        student.roll_no = data['roll_no']
        student.course = data['course']
        db.session.commit()
        return student

    @student_ns.response(204, 'Student deleted successfully')
    def delete(self, id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return '', 204

