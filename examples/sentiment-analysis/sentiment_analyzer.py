"""
Simple Sentiment Analysis Example
This example demonstrates basic sentiment analysis using TextBlob.
"""

from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary containing polarity, subjectivity, and sentiment label
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment label
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": sentiment
    }


def main():
    """Main function to demonstrate sentiment analysis."""
    # Example texts
    texts = [
        "I love this product! It's amazing!",
        "This is terrible. I hate it.",
        "The weather is okay today.",
        "Artificial Intelligence is transforming the world.",
        "I'm disappointed with the service."
    ]
    
    print("=" * 60)
    print("SENTIMENT ANALYSIS EXAMPLES")
    print("=" * 60)
    
    for text in texts:
        result = analyze_sentiment(text)
        print(f"\nText: {result['text']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Polarity: {result['polarity']:.2f} (range: -1 to 1)")
        print(f"Subjectivity: {result['subjectivity']:.2f} (range: 0 to 1)")
        print("-" * 60)
    
    # Interactive mode
    print("\n" + "=" * 60)
    print("Try your own text! (Press Enter with empty text to exit)")
    print("=" * 60)
    
    while True:
        user_text = input("\nEnter text to analyze: ").strip()
        if not user_text:
            break
        
        result = analyze_sentiment(user_text)
        print(f"Sentiment: {result['sentiment']}")
        print(f"Polarity: {result['polarity']:.2f}")
        print(f"Subjectivity: {result['subjectivity']:.2f}")


if __name__ == "__main__":
    main()
