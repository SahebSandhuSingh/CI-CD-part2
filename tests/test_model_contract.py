
import pytest
from spam_model import SpamModel
from sentiment_model import SentimentModel
from fraud_model import FraudModel

@pytest.mark.parametrize(
    "model_class",
    [SpamModel, SentimentModel, FraudModel]
)
def test_model_contract(model_class):
    model = model_class().load()

    assert hasattr(model, "predict")
    assert callable(model.predict)
