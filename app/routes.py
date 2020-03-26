from app import app
from flask import render_template, flash, redirect, url_for
from app.forms.detection_form.form import DetectionForm
from app.forms.url_detection_form.form import UrlDetectionForm
from ml_model.detector.FakeNewsDetector import FakeNewsDetector
from app.tools.html_utils import extract_text_from_html

APP_NAME = "FakeNewsDetector"

detector = FakeNewsDetector()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home/index.html', app_name=APP_NAME)


@app.route('/detect/content', methods=['GET', 'POST'])
def detect():
    form = DetectionForm()
    if form.validate_on_submit():
        verify_credibility(form.content.data)
    return render_template('detection/index.html', form=form)


@app.route('/detect/url', methods=['GET', 'POST'])
def detect_url():
    form = UrlDetectionForm()
    if form.validate_on_submit():
        url = form.content.data
        try:
            text = extract_text_from_html(url)
            verify_credibility(text)
        except:
            flash(f'Invalid url! {url}')
            return render_template('url_detection/index.html', form=form)
    return render_template('url_detection/index.html', form=form)


def verify_credibility(text):
    is_credible = detector.verify_news_credibility([text])
    flash(f'This news is rated as: {"REAL" if is_credible else "FAKE"}')
