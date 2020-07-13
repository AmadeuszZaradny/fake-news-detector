import pickle
import pandas as pd

classifier_file = open("fake-news-detection-model.pickle", "rb")
classifier = pickle.load(classifier_file)
vectorizer_file = open("fake-news-vectorizer.pickle", "rb")
vectorizer = pickle.load(vectorizer_file)

# fake.csv is a document that contain only fake documents
data = pd.read_csv('datasets/fake.csv')

# you can take certain amount of data setting value in head method
contents = data['text'].head(100).values.astype('U')

content_vector = vectorizer.transform(contents)

# print(content_vector.shape)
# print(vectorizer.get_feature_names())

decision = classifier.predict(content_vector)

print(decision)

wrong_classifications_count = 0
for pred in decision:
    wrong_classifications_count += pred
print(wrong_classifications_count)
