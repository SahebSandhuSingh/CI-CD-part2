import pytest
from src.fraud_model import FraudModel

@pytest.mark.parametrize(
    "model_class",
    [FraudModel]
)
def test_model_contract(model_class):
    model = model_class().load()

    assert hasattr(model, "predict")
    assert callable(model.predict)
