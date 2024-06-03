import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey|howdy",
        ["Hello!", "Hey there!", "Hi! How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm fine, how about you?"]
    ],
    [
        r"what can you do ?",
        ["I can help you with a variety of tasks such as providing information, answering questions, and more. Just ask!"]
    ],
    [
        r"(.*) your name ?",
        ["I'm a chatbot created by Priyanshu.", "You can call me Ruby.", "I go by the name Robye."]
    ],
    [
        r"(.*) (location|located) ?",
        ["I'm just a virtual assistant, so I don't have a physical location. But I'm here to assist you wherever you are!"]
    ],
    [
        r"(.*) (help|assist) (.*)",
        ["Sure, I'd be happy to help. What do you need assistance with?", "How can I assist you today?"]
    ],
    [
        r"what time is it ?",
        ["It's currently " + datetime.now().strftime("%H:%M") + "."]
    ],
    [
        r"(.*) (bye|goodbye)",
        ["Goodbye!", "See you later!", "Bye, take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Can you please rephrase?", "I'm still learning. Could you try saying that again?"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I'm Ruby, your virtual assistant. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Ruby:", response)
        if user_input.lower() == 'bye':
            break

if __name__ == "__main__":
    chat()
