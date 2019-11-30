import json

# Importation d'une variable JSON et affichage d'une partie de son contenu

x = '{ "name":"hello", "firstname":"world" }'

y = json.loads(x)

print(y["name"])

# Exportation d'un objet JSON dans une variable

y = json.dumps(x)

print(y)

# Test JSON avec fichiers

data = {}
data['shadow'] = []
data['shadow'].append({
  'passwd': 'wow9'
})

with open('shadow.txt', 'w') as outfile:
  json.dump(data, outfile)