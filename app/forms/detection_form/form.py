from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


style = {'class': 'form-control', 'style': 'height: 150px;'}
submit_class = {'class': 'btn btn-primary'}


class DetectionForm(FlaskForm):
    content = TextAreaField("content",
                            validators=[DataRequired()],
                            render_kw=style)
    submit = SubmitField("Verify content", render_kw=submit_class)
