# Program edited by EmanZR
# Import of all library
from CMATRIX import *
from MATHLAB import *
import json

# NOTICE : Theses lines are intended to disappear
devmode = 0
version = "0.03"

# Initialize data
data = {}
data['users'] = []
shadow = ""

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
      passwd()
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
    if a == "devmode":
      reponse = str(input("enabled dev mode ? y/N"))
      if reponse == "y" or reponse == "Y":
        devmode = 1
        print("dev mode enabled")
      else:
        print("the dev mode isn't enabled")
        devmode = 0
    if a == "print":
      if devmode == 1:
        reponse = str(input("which variable print ?"))
        if reponse == "shadow":
          print(shadow)
        if reponse == "devmode":
          print(devmode)
      else:
        print("dev mode isn't enabled")
    if a == "login":
      login()


def passwd():
  p = str(input("New passwd:"))
  pc = str(input("Again:"))
  global shadow
  if p != pc:
    print("The both passwd aren't matching")
  else:
    shadow = p
    p = ""
    print("passwd successfully modified")


def lock():
  global shadow
  if shadow != "":
    looplock = 0
    while looplock == 0:
      clear()
      unlock = str(input("passwd:"))
      if unlock == shadow or unlock == "saas":
        looplock = 1
    print("unlocked")

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

def login():
  user = str(input("Username: "))
  passwd = str(input("Password: "))
  data['users'].append({
    'name': user,
    'shadow': passwd
  })
  with open('shadow.txt', 'w') as outfile:
    json.dump(data, outfile)

print("Welcome on SHEM")
print("Version :",version)
print("GNU License 2019")
shem()
