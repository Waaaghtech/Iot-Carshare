from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import requests
from wtforms.fields.html5 import DateField, TimeField
from datetime import date as da, datetime, timedelta


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        r = requests.get('http://192.168.1.109:10100/uniq/{}'.format(username.data), verify=False)
        if 'error' in r.json():
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        r = requests.get('http://192.168.1.109:10100/uemail/{}'.format(email.data), verify=False)
        if 'error' in r.json():
            raise ValidationError('Please use a different email.')

class CarSearchForm(FlaskForm):
    body_type = SelectField('Car Type',coerce=int,validate_choice=False)
    colour = SelectField('Color',coerce=int,validate_choice=False)
    make = StringField(render_kw={"placeholder": "Make"})
    seats = IntegerField(render_kw={"placeholder": "Seats"})
    status = HiddenField(1)
    submit = SubmitField('Search')


class BookingForm(FlaskForm):
    car_id = HiddenField(validators=[DataRequired()])
    user_id = HiddenField(validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    time = TimeField(validators=[DataRequired()])
    duration = IntegerField(validators=[DataRequired()],render_kw={"placeholder": "Hours"})
    submit = SubmitField('Book')
    def validate_date(self, date):
        if date.data != da.today():
            raise ValidationError('We can only book cars for today at this version')
    def validate_time(self, time):
        if datetime.combine(da.today(),time.data) < (datetime.now() + timedelta(minutes=10)):
            raise ValidationError('We need 10 minutes to prepare the car')
        if datetime.combine(da.today(),time.data) > (datetime.now() + timedelta(hours=5)):
            raise ValidationError("We don't support booking more then 5 hours in advance at this stage")
    def validate_duration(self, duration):
        if duration.data < 1:
            raise ValidationError('Must book for 1 or more hours')
            


if __name__ == "__main__":
    pass