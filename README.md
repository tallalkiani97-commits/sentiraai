# SentiraAI

**An explainable NLP workspace for semantic comparison and sentiment-oriented analysis.**

SentiraAI is a Streamlit-based starter application that makes text analysis interactive. The baseline is intentionally small and interpretable, while the project structure leaves a clean path toward transformer embeddings, multilingual analysis and production inference.

## Product idea

Many AI demos hide the difference between a model and the user experience around it. SentiraAI puts the interaction layer first: enter two texts, inspect similarity, and view a simple sentiment interpretation before replacing the baseline with a larger model.

## Features

- Interactive Streamlit interface.
- Token-overlap similarity baseline.
- Small positive/negative/neutral lexicon.
- Clear separation between UI and analysis functions.
- Extension points for transformer embeddings, batch files and evaluation datasets.

## Architecture

```text
User text → normalization → similarity + sentiment → Streamlit result view
                                      ↓
                           future transformer adapter
```

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```text
app.py             # Streamlit UI and explainable baseline
requirements.txt   # runtime dependency
README.md          # documentation
```

## Roadmap

- Add multilingual sentiment models.
- Add sentence-transformer semantic similarity.
- Add confidence and calibration views.
- Add a small labelled evaluation dataset.
- Add optional API deployment with FastAPI.

## Limitations

The current sentiment method is a teaching baseline. It does not understand sarcasm, context or every language. Do not use it for high-impact decisions without a validated model and evaluation process.

## Tech stack

Python 3 · Streamlit · NLP · semantic similarity

## Author

Built by **Tallal Kiani**.
