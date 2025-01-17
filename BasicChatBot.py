import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there! What can I do for you?"]),
    (r"how are you(.*)", ["I'm just a bot, but I'm doing well. How about you?", "I'm doing great! Thanks for asking."]),
    (r"what is your name(.*)", ["I am a chatbot created to assist you.", "You can call me ChatBot."]),
    (r"(.*) created you(.*)", ["I was created by a developer using Python and NLTK.", "A developer built me to chat with you."]),
    (r"what can you do(.*)", ["I can have simple conversations, answer questions, and keep you company!", "I am here to chat and assist you with basic information."]),
    (r"quit", ["Goodbye! Have a great day!", "Bye! Take care."]),
    (r"(.*)", ["I'm sorry, I don't understand that.", "Can you rephrase that?"])
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hi! I am a simple chatbot. Type 'quit' to exit.")
    print("How can I help you today?\n")
    chatbot.converse()

if __name__ == "__main__":
    nltk.download("punkt")  # Ensure NLTK's data is available
    start_chat()
