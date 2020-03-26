from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


style = {'class': 'form-control'}
submit_class = {'class': 'btn btn-primary'}


class UrlDetectionForm(FlaskForm):
    content = TextAreaField("url",
                            validators=[DataRequired()],
                            render_kw=style)
    submit = SubmitField("Extract and verify content", render_kw=submit_class)
