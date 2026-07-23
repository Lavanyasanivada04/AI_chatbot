import datetime
import random

print("🤖 Welcome to LavanyaBot!")
name = input("Before we start, what's your name? ")

print(f"\nHello, {name}! 😊")
print("Type 'bye' to exit.\n")

jokes = [
    "Why do programmers love Python? Because it's easy to read!",
    "Debugging is like being a detective in your own code.",
    "A SQL query walks into a bar and joins two tables."
]

while True:
    user = input(f"{name}: ").lower()

    if user == "hello":
        print(f"Bot: Hello {name}! 👋")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is LavanyaBot.")

    elif user == "who created you":
        print("Bot: I was created by Lavanya using Python.")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    elif user == "good morning":
        print("Bot: Good morning! Have a wonderful day!")

    elif user == "good night":
        print("Bot: Good night! Sleep well.")

    elif user == "time":
        print("Bot:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot:", datetime.date.today())

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif "+" in user:
        try:
            a, b = user.split("+")
            print("Bot:", float(a) + float(b))
        except:
            print("Bot: Please enter like 12+5")

    elif "-" in user:
        try:
            a, b = user.split("-")
            print("Bot:", float(a) - float(b))
        except:
            print("Bot: Please enter like 12-5")

    elif "*" in user:
        try:
            a, b = user.split("*")
            print("Bot:", float(a) * float(b))
        except:
            print("Bot: Please enter like 12*5")

    elif "/" in user:
        try:
            a, b = user.split("/")
            if float(b) == 0:
                print("Bot: Cannot divide by zero.")
            else:
                print("Bot:", float(a) / float(b))
        except:
            print("Bot: Please enter like 12/5")

    elif user == "bye":
        print(f"Bot: Goodbye, {name}! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
