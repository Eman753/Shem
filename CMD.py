# Programme edite par Eman
from cmatrix import *
from mathlab import *

version = "0.02"

shadow = 9

def shem():
  z = 0
  while z == 0:
    a = str(input("$: "))
    if a == "help":
      help()
    if a == "exit":
      exit()
      z = 1
    if a == "halt":
      z = 1
    if a == "passwd":
      passwd(z)
      shadow = z
      print(shadow)
    if a == "lock":
      lock()
    if a == "cmatrix":
      c = int(input("combien"))
      cmatrix(c)
    if a == "version":
      print("shem, version",version,"edite par EmanZR")
    if a == "clear":
      clear()
    if a == "mathlab":
      mathlab()      


def passwd(z):
  p = str(input("entrez un passwd"))
  pc = str(input("confirmez"))
  if p != pc:
    print("les passwd ne corr. pas")
  else:
    z = p
    p = ""
    print("passwd modifie")
    return(z)


def lock():
  unlock = 0
  print(shadow)
  while unlock != shadow or unlock != "saas":
    unlock = str(input("entrez passwd"))
  unlock = ""

def help():
  print("liste des commandes:")
  print("help: liste des commandes")
  print("exit: quitter proprement")
  print("halt: terminer brutalement")
  print("passwd: definir un passwd")
  print("lock: verrouiller shem")
  print("cmatrix: programme amusant")
  print("version: afficher version")
  print("clear: effacer l'ecran")

def exit():
  print("")
  print("fermeture...")
  z = 1
  exit

def clear():
  for i in range(9):
    print("")

print("bienvenue sur SHEM")
print("version :",version)
print("entrez help pour commencer")
shem()
