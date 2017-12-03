from app import db
from datetime import datetime as dt

from app.modules.auth.model import User

from wtforms import Form, validators, StringField, RadioField

class Class(db.Document):
    owner = db.ReferenceField(User, required=True)
    name = db.StringField(required=True, min_length=3, max_length=50)
    person = db.ReferenceField(User, required=True)
    #events = db.ListField(db.ReferenceField(Events))
    start_time = db.DateTimeField(default=dt.now())
    end_time = db.DateTimeField(default=dt.now())
    days = db.StringField(default="",required=True)
    created_at = db.DateTimeField(default=dt.now())
    end_date = db.DateTimeField(default=dt.now())
    meta = {'strict': False}

class AddClassForm(Form):
    name = StringField('Class Name', [validators.Length(min=1, max=100),
                                        validators.DataRequired()])
    person = StringField('Professor Name', [validators.Length(min=1, max=100),
                                        validators.DataRequired()])
    #start_time = DateTimeField(default=dt.now())
    #end_time = DateTimeField(default=dt.now())
    #days = SelectMultipleField('Days', choices=[
    #    ('sunday',"Sunday"),('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', "Wednesday"), ('thursday', "Thursday"), ('friday', "Friday"), ('saturday', "Saturday")])
    #start_date = DateTimeField(default=dt.now())
    #end_date = DateTimeField(default=dt.now())