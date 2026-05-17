import json

def save_score(score):
    data = {
        "score": score
    }
    with open("save.json", "w") as file:
        json.dump(data, file)
def load_score():
    try:
        with open("save.json", "r") as file:
            data = json.load(file)
            return data["score"]
    except:
        return 0