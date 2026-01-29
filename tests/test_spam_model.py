from spam_model import SpamModel

def test_spam_model_predict_length():
    model = SpamModel().load()
    inputs = ["win money", "hello friend"]

    outputs = model.predict(inputs)

    assert len(outputs) == len(inputs)
