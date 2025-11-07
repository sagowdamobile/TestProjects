# Text Generation Example

A simple text generator using Markov chains to create new text based on training data.

## What it does

This example demonstrates text generation using a Markov chain model. It:
- Learns patterns from training text
- Generates new text that mimics the style and content of the training data
- Allows seeded generation (starting with specific words)
- Uses variable-length generation

## Installation

No external dependencies required! This example uses only Python standard library.

```bash
# Just run it!
python text_generator.py
```

## Usage

Run the text generator:
```bash
python text_generator.py
```

The script will:
1. Train on sample text about AI
2. Generate several random examples
3. Show seeded generation (starting with specific words)
4. Allow you to try your own seeds

## Example Output

```
Seed: 'Artificial intelligence'
Generated: Artificial intelligence is transforming the world. Machine learning 
algorithms can learn from data and make predictions...
```

## How it works

A **Markov chain** is a simple model that:
1. Looks at sequences of words in the training text
2. Records what words typically follow each sequence
3. Generates new text by randomly choosing the next word based on the patterns it learned

**Example:**
- If the training text has "machine learning algorithms" and "machine learning models"
- After seeing "machine learning", it might choose either "algorithms" or "models"
- This creates text that sounds similar to the training data

## Parameters

- **Order**: Number of words to consider (default: 2)
  - Order 1: Each word depends on the previous word
  - Order 2: Each word depends on the previous two words
  - Higher order = more coherent but less creative

## Limitations

This is a simple approach. Modern AI uses more sophisticated methods like:
- Neural language models (GPT, BERT)
- Transformer architectures
- Deep learning

But Markov chains are great for learning the basics!
