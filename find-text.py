import json

with open('group_final.ipynb') as json_file:
    data = json.load(json_file)

for each in data['cells']:
    cellType = each['cell_type']
    if cellType == "markdown":
        content = each['source']
        for line in content:
            print(line)

