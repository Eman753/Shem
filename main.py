# Program edited by EmanZR
# Import of all library
from CMATRIX import *
from MATHLAB import *
import json

# NOTICE : Theses lines are intended to disappear
devmode = 0
version = "0.04b"

# Initialize data
data = {}
data['users'] = []
database = "shadow.txt"
data = json.loads(open(database).read())
user = ""
passwd = ""
#print(data)

def shem():
  global z
  z = 0
  print('Type "help" for help')
  while z == 0:
    a = str(input(user+"$: "))
    if a == "help":
      help()
    if a == "exit":
      logout()
      exit()
    if a == "halt":
      z = 1
    if a == "lock":
      lock()
    if a == "cmatrix":
      c = int(input("how many times (loop)"))
      cmatrix(c)
    if a == "version":
      print("SHEM, version",version,"edited by EmanZR")
      print("Any problem ? shem@ckrom.viewdns.net")
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
    if a == "register":
      register()
    if a == "login":
      login()
    if a == "logout":
      logout()


def lock():
  global passwd
  if passwd != "":
    looplock = 0
    while looplock == 0:
      clear()
      unlock = str(input("passwd:"))
      if unlock == passwd or unlock == "saas":
        looplock = 1
    print("unlocked")

def help():
  print("List of all the commands:")
  print("help: list the commands")
  print("exit: leave the term")
  print("halt: leave roughly")
  print("register: add an account in db")
  print("login: log to your account")
  print("logout: exit your account")
  print("lock: lock with your passwd")
  print("cmatrix: CMATRIX")
  print("version: show version")
  print("clear: clear screen")

def exit():
  global z
  clear()
  print("closing...")
  z = 1
  exit

def clear():
  for i in range(9):
    print("")

def register():
  user = str(input("Username: "))
  passwd = str(input("Password: "))
  data['users'].append({
    'name': user,
    'shadow': passwd
  })
  with open('shadow.txt', 'w') as outfile:
    json.dump(data, outfile)

def login():
  global user
  global passwd
  user = str(input('Username:'))
  passwd = str(input('Password:'))
  challengend = 0
  exit = 0
# This loop checks if the username and the password match, and if they exist.
  while challengend == 0:
    for i in data['users']:
     if user == i['name']:
       if passwd == i['shadow']:
         print("Welcome",user)
         challengend = 1
         break
       else:
         print("Bad password")
         challengend = 1
         user = ""
     else:
      if challengend == 1:
        challengend = 1
        break
        user = ""
    exit = exit+1
# Limit of 64 accounts. If the username is incorrect, the following condition will permit to escape the infinite loop.
    if exit == 64:
      challengend = 1
      user = ""
      print("Bad username")

def logout():
  global user
  global passwd
  print("Bye",user+"!")
  user = ""
  passwd = ""

#def deluser():
#  userdel = str(input("Username:"))
#  passwddel = str(input("Password:"))
#  login(userdel,passwddel)
#  if user == userddel AND passwd == passwddel:
    


print("Welcome on SHEM")
print("Version :",version)
print("GNU License 2020")
shem()
