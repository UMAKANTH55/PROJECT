
from app import db
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    course = db.Column(db.String(50), nullable=False)

    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
