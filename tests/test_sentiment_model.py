from sentiment_model import SentimentModel

def test_sentiment_model_predict_length():
    model = SentimentModel().load()
    inputs = ["I love this", "this is bad"]

    outputs = model.predict(inputs)

    assert len(outputs) == len(inputs)
