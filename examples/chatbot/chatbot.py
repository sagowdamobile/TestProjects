"""
Simple Rule-Based Chatbot Example
This example demonstrates a basic chatbot using pattern matching.
"""

import re
import random


class SimpleChatbot:
    """A simple rule-based chatbot."""
    
    def __init__(self):
        """Initialize the chatbot with response patterns."""
        self.patterns = {
            r'hi|hello|hey': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!"
            ],
            r'how are you': [
                "I'm doing great, thank you for asking!",
                "I'm functioning perfectly! How about you?",
                "Excellent! How can I assist you?"
            ],
            r'what is your name|who are you': [
                "I'm a simple AI chatbot created to demonstrate basic conversational AI.",
                "My name is SimpleBot. I'm here to chat with you!",
                "I'm an AI assistant. You can call me SimpleBot."
            ],
            r'what can you do|help': [
                "I can have simple conversations with you! Try asking me about myself, the weather, or just say hello!",
                "I'm a basic chatbot. I can respond to greetings, answer questions about myself, and have simple chats.",
                "I can chat with you! Ask me anything, though I work best with simple questions."
            ],
            r'weather': [
                "I don't have access to real weather data, but I hope it's nice where you are!",
                "I can't check the weather, but I bet it's beautiful outside!",
                "Weather checking isn't my strong suit, but I hope you have a great day!"
            ],
            r'thanks|thank you': [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Feel free to ask more questions."
            ],
            r'bye|goodbye|exit|quit': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back anytime!"
            ],
            r'.*': [
                "That's interesting! Tell me more.",
                "I see. What else would you like to talk about?",
                "Hmm, I'm not sure how to respond to that. Can you rephrase?",
                "Interesting point! What else is on your mind?"
            ]
        }
    
    def get_response(self, user_input):
        """
        Get a response based on user input.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The chatbot's response
        """
        user_input = user_input.lower().strip()
        
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return "I'm not sure I understand. Can you try asking something else?"
    
    def chat(self):
        """Start an interactive chat session."""
        print("=" * 60)
        print("SIMPLE CHATBOT")
        print("=" * 60)
        print("Hello! I'm SimpleBot. Type 'bye' to exit.")
        print("=" * 60)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                print("Bot: Please say something!")
                continue
            
            response = self.get_response(user_input)
            print(f"Bot: {response}")
            
            if re.search(r'bye|goodbye|exit|quit', user_input.lower()):
                break


def main():
    """Main function to run the chatbot."""
    chatbot = SimpleChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()
