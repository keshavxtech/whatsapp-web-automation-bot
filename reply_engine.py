import random
import datetime

def generate_reply(message):
    message = message.lower()
    current_hour = datetime.datetime.now().hour

    greetings = [
        "haan bhai bolo 😊",
        "hey! kya scene hai?",
        "haan batao 😄"
    ]

    busy_replies = [
        "thoda busy hoon, baad me batata hoon",
        "abhi kaam me hoon yaar",
        "thodi der me reply karta hoon"
    ]

    if "hi" in message or "hello" in message:
        return random.choice(greetings)

    elif "kaha" in message:
        return "ghar pe hoon bhai 😅"

    elif "kya kar raha" in message:
        return random.choice(busy_replies)

    elif "?" in message:
        return "achha question hai, check karke batata hoon."

    elif current_hour >= 23:
        return "ab late ho gaya hai, kal baat karte hain."

    else:
        return random.choice(busy_replies)
