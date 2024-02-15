from flask import Flask, render_template
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

#Configuring the mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ADMIN:umakanth_9@localhost:3306/data'
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
app.register_blueprint(swagger_ui_blueprint, url_prefix='/swagger')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import and initialize models
from models.student import Student
with app.app_context():
    db.create_all()

# Import and add resources
from api.student import student_ns
api.add_namespace(student_ns)

#Inorder to render index.html file
@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

