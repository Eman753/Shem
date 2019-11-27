# programme edite par emanzr
vmathlab = "0.01"

def mathlab():
  term = 0
  print("mathlab version",vmathlab)
  while term == 0:
    a = str(input("mathlab$: "))
    if a == "help":
      print("help: liste des commandes")
      print("halt: quitter brutalement")
    if a == "halt":
      term = 1