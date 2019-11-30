import json

# Importation d'une variable JSON et affichage d'une partie de son contenu

x = '{ "name":"hello", "firstname":"world" }'

y = json.loads(x)

print(y["name"])

# Exportation d'un objet JSON dans une variable

y = json.dumps(x)

print(y)