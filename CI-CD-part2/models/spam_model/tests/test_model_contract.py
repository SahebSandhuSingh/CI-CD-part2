import pytest
from src.spam_model import SpamModel

@pytest.mark.parametrize(
    "model_class",
    [SpamModel]
)
def test_model_contract(model_class):
    model = model_class().load()

    assert hasattr(model, "predict")
    assert callable(model.predict)
