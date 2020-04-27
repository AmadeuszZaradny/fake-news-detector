import pickle
import sys


class FakeNewsDetector:
    def __init__(self):
        sys.path.append('ml_model')
        self.classifier = pickle.load(open("ml_model/fake-news-detection-model.pickle", "rb"))
        self.vectorizer = pickle.load(open("ml_model/fake-news-vectorizer.pickle", "rb"))

    def verify_news_credibility(self, content):
        content_vector = self.vectorizer.transform(content)
        is_credible = self.classifier.predict(content_vector)[0]
        return bool(is_credible)
