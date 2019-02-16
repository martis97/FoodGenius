import json

with open('C:/Food Genius/ideas.json', 'r') as ideas_file:
    ideas_dict = json.load(ideas_file)

for idea in ideas_dict:
    print(ideas_dict['set meal'])