# Sentiment Analysis Example

A simple sentiment analysis tool that analyzes the emotional tone of text.

## What it does

This example uses TextBlob to analyze text and determine whether it's positive, negative, or neutral. It also provides:
- **Polarity**: A score from -1 (very negative) to 1 (very positive)
- **Subjectivity**: A score from 0 (very objective) to 1 (very subjective)

## Installation

From the repository root, install dependencies:
```bash
pip install -r requirements.txt
```

Then download the required corpora:
```bash
python -m textblob.download_corpora
```

## Usage

Run the example:
```bash
python sentiment_analyzer.py
```

The script will:
1. Analyze several pre-defined example texts
2. Allow you to enter your own text for analysis

## Example Output

```
Text: I love this product! It's amazing!
Sentiment: Positive
Polarity: 0.65
Subjectivity: 0.85
```

## How it works

The sentiment analyzer uses TextBlob's built-in sentiment analysis, which is based on a pre-trained model that evaluates words and phrases to determine overall sentiment.
