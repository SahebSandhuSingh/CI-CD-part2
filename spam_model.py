from base import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class SpamModel(BaseModel):

    def load(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

        texts = [
            "win money now",
            "free lottery ticket",
            "hello friend",
            "how are you"
        ]
        labels = [1, 1, 0, 0]

        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

        return self

    def predict(self, X):
        X_vec = self.vectorizer.transform(X)
        return self.model.predict(X_vec).tolist()
