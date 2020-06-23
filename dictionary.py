import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userFeedback = input("Did you mean '%s'? (y/n) " % get_close_matches(word, data.keys())[0])
        if userFeedback.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif userFeedback.lower() == "n": 
            return "The word doesn't exist."
        else:
            return "Invalid input."
    else:
        return "The word doesn't exist."

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)