from src.fraud_model import FraudModel

def test_fraud_model_predict_length():
    model = FraudModel().load()
    inputs = [
        [100, 1],
        [20000, 25]
    ]

    outputs = model.predict(inputs)

    assert len(outputs) == len(inputs)
