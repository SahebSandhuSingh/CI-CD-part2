import pytest
from src.sentiment_model import SentimentModel

@pytest.mark.parametrize(
    "model_class",
    [SentimentModel]
)
def test_model_contract(model_class):
    model = model_class().load()

    assert hasattr(model, "predict")
    assert callable(model.predict)
