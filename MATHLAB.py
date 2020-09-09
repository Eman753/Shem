# programme edite par emanzr
from math import *

vmathlab = "0.03"

def mathlab():
  term = 0
  print("mathlab version",vmathlab)
  while term == 0:
    a = str(input("mathlab$: "))
    if a == "help":
      print("help: list of commands")
      print("halt: leave roughly")
      print("exit: leave properly")
      print("pythagore: calculate hypotenuse of a rectangle triangle")
      print("trinome: find the real roots of your polynomial")
      print("about: short info about mathlab")
    if a == "halt":
      term = 1
    if a == "exit":
      exit()
      term = 1
    if a == "pythagore":
      pythagore()
    if a == "trinome":
      trinome()
    if a == "about":
      print("mathlab was created by EmanZR")
      print("It is a quick tool designed to help and assist you")
      print("The developpement is still at its beginning")

def exit():
  print("See you again !")

def pythagore():
  reponse = str(input("theorem or reciprocal ? t/r"))
  if reponse == "t" or reponse == "T":
    a = float(input("first side"))
    b = float(input("second side"))
    c = sqrt(a**2+b**2)
    print("the hypotenuse worth",c)
  elif reponse == "r" or reponse == "R":
    a = float(input("first side"))
    b = float(input("second side"))
    c = float(input("longest side"))
    if c**2 == a**2 + b**2:
      print("the triangle is rectangle")
    else:
      print("the triangle isn't rectangle")
  else:
    print("please give a legal argument")

def trinome():
  a = int(input("a = ?"))
  b = int(input("b = ?"))
  c = int(input("c = ?"))
  if a == 0:
    print("This isn't a trinome")
  d = b*b-4*a*c
  print(d)
  if d == 0:
    t = -(b/2*a)
    print("the only root is",t)
  elif d > 0:
    t = -((b-sqrt(d))/2*a)
    y = -((b+sqrt(d))/2*a)
    print("the roots are",t,"and",y)
  else:
    print("this trinome doesn't have root")

    