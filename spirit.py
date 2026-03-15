import json
import difflib

print("SPIRIT: Hello! I am your college assistant.")
print("Type 'bye' to exit.\n")

with open("data.json") as f:
    data = json.load(f)

questions = list(data.keys())

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("SPIRIT: Goodbye! Have a nice day.")
        break

    match = difflib.get_close_matches(user, questions, n=1, cutoff=0.4)

    if match:
        print("SPIRIT:", data[match[0]])
    else:
        print("SPIRIT: Sorry, I don't understand that yet.")