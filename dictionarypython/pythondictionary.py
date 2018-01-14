import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return(data[w.title()])
    elif w.upper() in data:
        return(data[w.upper()])
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Do you mean {} instead?, Enter 'Y' if yes, and 'N' if no: ".format(get_close_matches(w, data.keys())[0]))
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't match in the dictionary"
        else:
            return "You didn't input anything!!"
    else:
        return "this word does not exist in the dictionary"

word = input("enter dictionary word: ")
output = dictionary(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(2 + 2)
    print(output)
