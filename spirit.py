import json

print("SPIRIT: Hello! I am your college assistant.")
print("Type 'bye' to exit.\n")

with open("data.json") as f:
    data = json.load(f)

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("SPIRIT: Goodbye! Have a nice day.")
        break

    found = False

    for key in data:
        if key in user:
            print("SPIRIT:", data[key])
            found = True
            break

    if not found:
        print("SPIRIT: Sorry, I don't understand that yet.")