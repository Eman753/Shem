# programme edite par emanzr
from math import *

vmathlab = "0.02"

def mathlab():
  term = 0
  print("mathlab version",vmathlab)
  while term == 0:
    a = str(input("mathlab$: "))
    if a == "help":
      print("help: list of commands")
      print("halt: leave roughly")
      print("pythagore: calculate hypotenuse of a rectangle triangle")
    if a == "halt":
      term = 1
    if a == "pythagore":
      pythagore()

def pythagore():
  z = 0
  while z == 0:
    reponse = str(input("theorem or reciprocal ? t/r"))
    if reponse == "t" or reponse == "T":
      a = float(input("first side"))
      b = float(input("second side"))
      c = sqrt(a**2+b**2)
      print("the hypotenuse worth",c)
      z = 1
    elif reponse == "r" or reponse == "R":
      a = float(input("first side"))
      b = float(input("second side"))
      c = float(input("longest side"))
      if c**2 == a**2 + b**2:
        print("the triangle is rectangle")
      else:
        print("the triangle isn't rectangle")
      z = 1
    else:
      print("please give a legal argument")