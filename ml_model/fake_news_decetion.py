import pickle
import pandas as pd

classifier_file = open("fake-news-service/ml_model/fake-news-detection-model.pickle", "rb")
classifier = pickle.load(classifier_file)
vectorizer_file = open("fake-news-service/ml_model/fake-news-vectorizer.pickle", "rb")
vectorizer = pickle.load(vectorizer_file)

data = pd.read_csv('fake-news-service/ml_model/datasets/fake.csv')
print(data.head(100))
contents = data['text'].head(100).values.astype('U')
# contents = [""" """]

content_vector = vectorizer.transform(contents)

print(content_vector.shape)
print(vectorizer.get_feature_names())

prediction = classifier.predict_proba(content_vector)
decision = classifier.predict(content_vector)

print(prediction)
print(decision)

suma = 0
for pred in decision:
    suma += pred
print(suma)
