import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"(.*) (happy|excited|glad)",
        ["That's great to hear!",]
    ],
    [
        r"(.*) (sad|depressed|unhappy)",
        ["I'm sorry to hear that. How can I help?",]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon.",]
    ],
]

# Create a Chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

def main():
    print("Hello! I'm a chatbot. You can talk to me. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    main()
