import pickle
import pandas as pd

classifier_file = open("fake-news-detection-model.pickle", "rb")
classifier = pickle.load(classifier_file)
vectorizer_file = open("fake-news-vectorizer.pickle", "rb")
vectorizer = pickle.load(vectorizer_file)

data = pd.read_csv('datasets/fake.csv')
print(data.head(100))
contents = data['text'].head(100).values.astype('U')

content_vector = vectorizer.transform(contents)

print(content_vector.shape)
print(vectorizer.get_feature_names())

decision = classifier.predict(content_vector)

print(decision)

suma = 0
for pred in decision:
    suma += pred
print(suma)
