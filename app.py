#Inporting necessary modules
from flask import Flask, render_template
from flask_restx import Api,Namespace, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

#Intializing the Flask app
app = Flask(__name__)

#Configuring the mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ADMIN:umakanth_9@host.docker.internal/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an instance of the Flask-RESTx API
api = Api(app, title='Student API', version='1.0', description='CRUD operations for Students')

# Create Swagger UI blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.json',
    config={
        'app_name': "Student API"
    }
)
# Register the Swagger UI blueprint
app.register_blueprint(swagger_ui_blueprint, url_prefix='/swagger')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Student model for the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    course = db.Column(db.String(50), nullable=False)

    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

# Create the database tables
with app.app_context():
    db.create_all()

# Create a namespace for the API
student_ns = Namespace('student', description='Student operations')

# Define the student model for the API
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
    
#Defining GET,PUT,DELETE methods with the API endpoint
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

#Add the namespace to the API
api.add_namespace(student_ns)

#Inorder to render index.html file
@app.route('/index/')
def index():
    return render_template('index.html')

#Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

