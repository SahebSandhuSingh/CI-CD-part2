# Multi-Model ML CI/CD Architecture

This repository has been refactored into a production-grade multi-model ML CI/CD architecture where each model is independently testable, buildable, and deployable.

## Architecture Overview

```
models/
├── fraud_model/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── fraud_model.py
│   │   └── base.py
│   ├── tests/
│   │   ├── test_fraud_model.py
│   │   └── test_model_contract.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── sentiment_model/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── sentiment_model.py
│   │   └── base.py
│   ├── tests/
│   │   ├── test_sentiment_model.py
│   │   └── test_model_contract.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── spam_model/
    ├── src/
    │   ├── __init__.py
    │   ├── spam_model.py
    │   └── base.py
    ├── tests/
    │   ├── test_spam_model.py
    │   └── test_model_contract.py
    ├── requirements.txt
    └── Dockerfile
```

## Testing Each Model

Each model can be tested independently:

```bash
# Test fraud model
cd models/fraud_model
python3 -m pytest tests/ -v

# Test sentiment model
cd models/sentiment_model
python3 -m pytest tests/ -v

# Test spam model
cd models/spam_model
python3 -m pytest tests/ -v
```

## Building Docker Images

Each model has its own Dockerfile and can be built independently:

```bash
# Build fraud model
cd models/fraud_model
docker build -t fraud-model:latest .

# Build sentiment model
cd models/sentiment_model
docker build -t sentiment-model:latest .

# Build spam model
cd models/spam_model
docker build -t spam-model:latest .
```

## Running Docker Containers

```bash
# Run fraud model
docker run fraud-model:latest

# Run sentiment model
docker run sentiment-model:latest

# Run spam model
docker run spam-model:latest
```

## Dependencies Per Model

### Fraud Model
- numpy
- pandas
- scikit-learn
- joblib
- pytest

### Sentiment Model
- numpy
- scikit-learn
- joblib
- pytest

### Spam Model
- numpy
- scikit-learn
- joblib
- pytest

## CI/CD Integration

Each model can now have its own CI/CD pipeline:
- Independent testing
- Independent Docker builds
- Independent deployment
- Model-specific versioning

This architecture supports:
- ✅ Isolated testing per model
- ✅ Independent Docker builds
- ✅ Model-specific dependencies
- ✅ Parallel CI/CD execution
- ✅ Individual model deployment
- ✅ Clear separation of concerns
