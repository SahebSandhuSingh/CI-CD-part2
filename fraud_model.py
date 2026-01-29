from base import BaseModel
from sklearn.ensemble import RandomForestClassifier

class FraudModel(BaseModel):

    def load(self):
        self.model = RandomForestClassifier(
            n_estimators=10,
            random_state=42
        )

        X = [
            [100, 1],
            [200, 2],
            [5000, 10],
            [20000, 25]
        ]
        y = [0, 0, 1, 1]

        self.model.fit(X, y)

        return self

    def predict(self, X):
        return self.model.predict(X).tolist()
