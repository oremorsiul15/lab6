from difflib import SequenceMatcher
import json

f = open('db.json')
data = json.load(f)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


while True:
    question = input('q: ')
    filtered_list = [
        dictionary for dictionary in data
        if similar(dictionary['question'], question) > .8
    ]
    for q in filtered_list:
        print('match: ')
        print(q['question'])
        print(q['ans'])
        print('-----------------------------')
