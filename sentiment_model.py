from base import BaseModel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

class SentimentModel(BaseModel):

    def load(self):
        self.vectorizer = CountVectorizer()
        self.model = LogisticRegression()

        texts = [
            "I love this product",
            "this is amazing",
            "I hate this",
            "very bad experience"
        ]
        labels = [1, 1, 0, 0]

        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

        return self

    def predict(self, X):
        X_vec = self.vectorizer.transform(X)
        return self.model.predict(X_vec).tolist()
