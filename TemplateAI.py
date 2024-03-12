import nltk  # Import NLTK library for natural language processing
import re  # Import re module for regular expressions
import random  # Import random module for generating random responses

# Sample responses for different intents
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't get that."]
}

# Define patterns for different intents
patterns = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"],
}

# Preprocess text by converting it to lowercase
def preprocess(text):
    text = text.lower()
    return text

# Define a function to respond to user input
def respond(user_input):
    user_input = preprocess(user_input)  # Preprocess user input
    for intent, patterns_list in patterns.items():
        for pattern in patterns_list:
            if re.search(pattern, user_input):  # Check if user input matches any pattern
                return random.choice(responses[intent])  # Return a random response for the matched intent
    return random.choice(responses["default"])  # If no match found, return a default response

# Main loop to interact with the user
def main():
    print("Bot: Hello! I'm a semi-advanced Python AI. How can I assist you today?")
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        else:
            response = respond(user_input)  # Get bot's response
            print("Bot:", response)  # Print bot's response

if __name__ == "__main__":
    main()
