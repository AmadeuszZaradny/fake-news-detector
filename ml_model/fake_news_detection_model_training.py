import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from timeit import default_timer as timer
from sklearn.model_selection import cross_validate
from tokenizer import stemming_tokenizer

MODEL_PATH = "fake-news-detection-model.pickle"
VECTORIZER_PATH = "fake-news-vectorizer.pickle"
DATASET_PATH = "datasets/news.csv"
FAKE_NEWS_DETECTION_FEATURES_COUNT = 5000
CROSS_VALIDATION_SPLITS_COUNT = 10


def save_model_and_vectorizer(model, vec):
    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)
    with open(VECTORIZER_PATH, "wb") as file:
        pickle.dump(vec, file)


def get_contents_and_labels_from_file(dataset_path):
    data = pd.read_csv(dataset_path)
    formatted_contents = data['text'].values.astype('U')
    formatted_labels = list(map(lambda label: 1 if label == 'REAL' else 0, data['label']))
    return formatted_contents, formatted_labels


def execute_and_print_time(comment, function):
    start = timer()
    result = function()
    end = timer()
    print(comment, "time:", end - start, "seconds")
    return result


def vectorize_data(data, ngram_range, max_features):
    vec = TfidfVectorizer(
        analyzer='word',
        ngram_range=ngram_range,
        tokenizer=stemming_tokenizer,
        max_features=max_features)
    vectorized_data = vec.fit_transform(data)
    return vectorized_data, vec


def learn_model(model, inputs, outputs):
    model.fit(X=inputs, y=outputs)
    return model


def summarize_cross_validation_results(validation_result):
    print("Cross validation score: ", validation_result['test_score'],
          " mean: ", validation_result['test_score'].mean(),
          " stddev: ", validation_result['test_score'].std())


if __name__ == "__main__":
    contents, labels = get_contents_and_labels_from_file(DATASET_PATH)

    reduced_contents_vector, vectorizer = execute_and_print_time(
        "Vectorizing",
        lambda: vectorize_data(contents, (1, 1), FAKE_NEWS_DETECTION_FEATURES_COUNT)
    )

    learning_model = svm.SVC(kernel='linear', gamma="scale", probability=False)

    cross_validation_result = execute_and_print_time(
        "Cross validation",
        lambda: cross_validate(
            estimator=learning_model,
            X=reduced_contents_vector,
            y=labels,
            cv=CROSS_VALIDATION_SPLITS_COUNT)
    )
    summarize_cross_validation_results(cross_validation_result)

    trained_model = execute_and_print_time(
        "Model learning",
        lambda: learn_model(learning_model, reduced_contents_vector, labels)
    )

    # save_model_and_vectorizer(trained_model, vectorizer)
