"""
Simple Text Generation Example using Markov Chains
This example demonstrates basic text generation using a Markov chain model.
"""

import random
import re


class MarkovTextGenerator:
    """A simple text generator using Markov chains."""
    
    def __init__(self, order=2):
        """
        Initialize the Markov text generator.
        
        Args:
            order (int): The order of the Markov chain (number of words to consider)
        """
        self.order = order
        self.chain = {}
    
    def train(self, text):
        """
        Train the model on a given text.
        
        Args:
            text (str): The training text
        """
        # Tokenize the text into words
        words = re.findall(r'\b\w+\b|[.,!?;]', text)
        
        # Build the Markov chain
        for i in range(len(words) - self.order):
            # Create a key from the current sequence of words
            key = tuple(words[i:i + self.order])
            
            # The next word is what follows this sequence
            next_word = words[i + self.order]
            
            # Add to the chain
            if key not in self.chain:
                self.chain[key] = []
            self.chain[key].append(next_word)
    
    def generate(self, length=50, seed=None):
        """
        Generate text using the trained model.
        
        Args:
            length (int): Number of words to generate
            seed (str): Optional seed text to start generation
            
        Returns:
            str: Generated text
        """
        if not self.chain:
            return "Please train the model first!"
        
        # Start with a random key or use seed
        if seed:
            words = re.findall(r'\b\w+\b', seed.lower())
            if len(words) >= self.order:
                current = tuple(words[-self.order:])
                if current not in self.chain:
                    current = random.choice(list(self.chain.keys()))
            else:
                current = random.choice(list(self.chain.keys()))
        else:
            current = random.choice(list(self.chain.keys()))
        
        result = list(current)
        
        # Generate text
        for _ in range(length):
            if current in self.chain:
                next_word = random.choice(self.chain[current])
                result.append(next_word)
                current = tuple(result[-self.order:])
            else:
                # If we reach a dead end, pick a random key
                current = random.choice(list(self.chain.keys()))
                result.extend(current)
        
        # Join words and clean up spacing around punctuation
        text = ' '.join(result)
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        
        return text


def main():
    """Main function to demonstrate text generation."""
    # Sample training text about AI
    training_text = """
    Artificial intelligence is transforming the world. Machine learning algorithms 
    can learn from data and make predictions. Deep learning uses neural networks 
    to process information. Natural language processing helps computers understand 
    human language. AI systems can recognize patterns and solve complex problems. 
    Computer vision enables machines to see and interpret images. Robotics combines 
    AI with mechanical systems. The future of AI is exciting and full of possibilities. 
    AI can help solve global challenges. Machine learning models improve with more data. 
    Neural networks are inspired by the human brain. AI research continues to advance 
    rapidly. Technology is making AI more accessible. Artificial intelligence will 
    change how we work and live. Innovation in AI drives progress across many fields.
    """
    
    print("=" * 60)
    print("TEXT GENERATION USING MARKOV CHAINS")
    print("=" * 60)
    
    # Create and train the generator
    generator = MarkovTextGenerator(order=2)
    generator.train(training_text)
    
    print("\nTraining completed on sample text about AI!")
    print("\n" + "=" * 60)
    print("GENERATED TEXT EXAMPLES")
    print("=" * 60)
    
    # Generate several examples
    for i in range(3):
        print(f"\nExample {i + 1}:")
        generated_text = generator.generate(length=30)
        print(generated_text)
    
    print("\n" + "=" * 60)
    print("SEEDED GENERATION")
    print("=" * 60)
    
    # Generate with a seed
    seed_text = "Artificial intelligence"
    print(f"\nSeed: '{seed_text}'")
    generated_text = generator.generate(length=25, seed=seed_text)
    print(f"Generated: {generated_text}")
    
    # Interactive mode
    print("\n" + "=" * 60)
    print("Try your own! (Press Enter with empty text to exit)")
    print("=" * 60)
    
    while True:
        seed = input("\nEnter seed text (or press Enter for random): ").strip()
        if seed is None:
            break
        
        if seed == "":
            seed = None
        
        try:
            length = input("How many words to generate? (default: 30): ").strip()
            length = int(length) if length else 30
        except ValueError:
            length = 30
        
        if seed is None and length == 0:
            break
        
        generated = generator.generate(length=length, seed=seed)
        print(f"\nGenerated: {generated}")


if __name__ == "__main__":
    main()
