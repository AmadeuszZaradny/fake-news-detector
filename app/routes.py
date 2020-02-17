from app import app
from flask import render_template, flash, redirect, url_for
from app.forms.detection_form.form import DetectionForm
from ml_model.detector.FakeNewsDetector import FakeNewsDetector


APP_NAME = "FakeNewsDetector"

detector = FakeNewsDetector()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home/index.html', app_name=APP_NAME)


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    form = DetectionForm()
    if form.validate_on_submit():
        is_credible = detector.verify_news_credibility([form.content.data])
        flash(f'This news is rated as: {"REAL" if is_credible else "FAKE"}')
        return redirect(url_for('home'))
    return render_template('detection/index.html', form=form)

