from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from werkzeug.routing import ValidationError
from flaskblog.models import Result

class PlatformSelectionForm(FlaskForm):
    test_environment = SelectField('Test Environment', choices=[('UAT', 'UAT'), ('QA', 'QA')])
    jurisdiction = SelectField('Test Environment', choices=[('MA', 'Massachusetts'), ('AZ', 'Arizona')])
    release_name = TextField('Release Name',validators=[DataRequired()])
    chrome_checkbox = BooleanField("Chrome")
    firefox_checkbox = BooleanField("Firefox")
    edge_checkbox = BooleanField("Edge")
    ie_checkbox = BooleanField("Internet Eplorer")
    submit = SubmitField('Submit')

    def validate_release_name(self,release_name):
        user = Result.query.filter_by(release_name=release_name.data).first()
        if user:
            raise ValidationError('Duplicate release name not allowed. Please choose a different one')