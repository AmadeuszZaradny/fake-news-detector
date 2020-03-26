import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from timeit import default_timer as timer
from sklearn.model_selection import cross_validate
from tokenizer import stemming_tokenizer

FAKE_NEWS_DETECTION_FEATURES_COUNT = 5000
CROSS_VALIDATION_SPLITS_COUNT = 10

data = pd.read_csv('fake-news-service/ml_model/datasets/news.csv')
contents = data['text'].values.astype('U')
labels = list(map(lambda label: 1 if label == 'REAL' else 0, data['label']))

vectorizing_start = timer()
vectorizer = TfidfVectorizer(
    analyzer='word',
    ngram_range=(1, 3),
    tokenizer=stemming_tokenizer,
    max_features=FAKE_NEWS_DETECTION_FEATURES_COUNT)
reduced_contents_vector = vectorizer.fit_transform(contents)
vectorizing_end = timer()
print("Vectorizing time: ", vectorizing_end - vectorizing_start)

learning_model = svm.SVC(kernel='linear', gamma="scale", probability=False)

cross_validation_time_start = timer()
cross_validation_result = cross_validate(
    estimator=learning_model,
    X=reduced_contents_vector,
    y=labels,
    cv=CROSS_VALIDATION_SPLITS_COUNT)
cross_validation_time_end = timer()
print("Cross validation time: ", cross_validation_time_end - cross_validation_time_start)
print("Cross validation score: ", cross_validation_result['test_score'], " mean: ", cross_validation_result['test_score'].mean())

learning_start = timer()
learning_model.fit(X=reduced_contents_vector, y=labels)
learning_end = timer()
print("Learning time: ", learning_end - learning_start)

with open("fake-news-service/ml_model/fake-news-detection-model.pickle", "wb") as file:
    pickle.dump(learning_model, file)
with open("fake-news-service/ml_model/fake-news-vectorizer.pickle", "wb") as file:
    pickle.dump(vectorizer, file)
