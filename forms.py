from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField, TextAreaField


class Drawing(FlaskForm):
    initial_state = TextField('Initial state')
    productions = TextAreaField('Productions')
    number_steps = IntegerField('Number of steps')
    angle = IntegerField('Turning angle')
    step_size = IntegerField('Step size')
    submit = SubmitField('Submit')
