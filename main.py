# Program edited by EmanZR
from CMATRIX import *
from MATHLAB import *

version = "0.02"


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
      c = int(input("how many times (loop)"))
      cmatrix(c)
    if a == "version":
      print("SHEM, version",version,"edited by EmanZR")
    if a == "clear":
      clear()
    if a == "mathlab":
      mathlab()      


def passwd(z):
  p = str(input("New passwd:"))
  pc = str(input("Again:"))
  if p != pc:
    print("The both passwd aren't matching")
  else:
    z = p
    p = ""
    print("passwd successfully modified")
    return(z)


def lock():
  unlock = 0
  print(shadow)
  while unlock != shadow or unlock != "saas":
    unlock = str(input("passwd:"))
  unlock = ""

def help():
  print("List of all the commands:")
  print("help: list the commands")
  print("exit: leave the term")
  print("halt: leave roughly")
  print("passwd: modify passwd")
  print("lock: lock SHEM")
  print("cmatrix: CMATRIX")
  print("version: show version")
  print("clear: clear screen")

def exit():
  clear()
  print("closing...")
  z = 1
  exit

def clear():
  for i in range(9):
    print("")

print("Welcome on SHEM")
print("Version :",version)
print("GNU License 2019")
shem()
