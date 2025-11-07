# Simple AI Example Projects

A collection of simple AI/ML example projects for learning and experimentation.

## Overview

This repository contains beginner-friendly AI examples that demonstrate fundamental concepts in artificial intelligence and machine learning. Each example is self-contained and includes clear documentation.

## Projects

### 1. Sentiment Analysis
**Location:** `examples/sentiment-analysis/`

A simple sentiment analyzer that determines whether text is positive, negative, or neutral.

- **Technology:** TextBlob
- **Concepts:** Natural Language Processing, Sentiment Analysis
- **Difficulty:** Beginner

[View Example →](examples/sentiment-analysis/)

### 2. Rule-Based Chatbot
**Location:** `examples/chatbot/`

A basic conversational chatbot using pattern matching and rule-based responses.

- **Technology:** Python Standard Library (regex)
- **Concepts:** Pattern Matching, Conversational AI
- **Difficulty:** Beginner

[View Example →](examples/chatbot/)

### 3. Text Generation (Markov Chains)
**Location:** `examples/text-generation/`

A text generator that creates new content based on training text using Markov chains.

- **Technology:** Python Standard Library
- **Concepts:** Markov Chains, Text Generation, Statistical Models
- **Difficulty:** Beginner

[View Example →](examples/text-generation/)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/<your-username>/TestProjects.git
cd TestProjects
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For the sentiment analysis example, download required corpora:
```bash
python -m textblob.download_corpora
```

### Running the Examples

Each example can be run independently:

```bash
# Sentiment Analysis
cd examples/sentiment-analysis
python sentiment_analyzer.py

# Chatbot
cd examples/chatbot
python chatbot.py

# Text Generation
cd examples/text-generation
python text_generator.py
```

## Learning Path

We recommend exploring the examples in this order:

1. **Sentiment Analysis** - Start here to understand NLP basics
2. **Chatbot** - Learn about conversational AI and pattern matching
3. **Text Generation** - Explore probabilistic text generation

## What You'll Learn

- **Natural Language Processing (NLP):** How computers understand and process human language
- **Pattern Recognition:** How AI identifies patterns in data
- **Text Generation:** How machines can create new content
- **Conversational AI:** How chatbots work
- **Statistical Models:** How probability drives AI predictions

## Contributing

Feel free to add more examples or improve existing ones! This repository is for learning and experimentation.

## License

This project is open source and available for educational purposes.

## Resources

- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Markov Chains Explained](https://en.wikipedia.org/wiki/Markov_chain)

## Next Steps

Want to learn more? Consider exploring:
- Machine Learning frameworks (scikit-learn, TensorFlow, PyTorch)
- Deep Learning and Neural Networks
- Advanced NLP with transformers (BERT, GPT)
- Computer Vision with OpenCV
- Reinforcement Learning
