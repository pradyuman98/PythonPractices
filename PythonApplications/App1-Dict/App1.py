import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def Meaning(w):
    if w in data:
         return data[w]
    else:
        w=w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys()))>0:
            x=input("Did you mean %s \n If Yes press Y, if No press N: "  % get_close_matches(w, data.keys())[0])
            if x=="Y":
                return data[get_close_matches(w, data.keys())[0]]
            else: "Please. Try Again..."

        else:
            return "The Word dosen't exist. Please recheck it..."

word=input("Enter word: ")

output=Meaning(word)

if type(output)== list:
    for item in output:
        print(item)

else:
    print(output)
