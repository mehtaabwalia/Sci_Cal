import math
print("welcome to calculator created by mehtaab, \n what do you want to do?")

def addition():
  first_num=float(input("enter the first value:"))
  second_num=float(input("enter the second value:"))

  c=first_num+ second_num
  print(c)

def substraction():
  first_num=float(input("enter the first value:"))
  second_num=float(input("enter the second value:"))

  c=first_num-second_num
  print(c)

def multiplication():
  first_num=float(input("enter the first value:"))
  second_num=float(input("enter the second value:"))

  c=first_num*second_num
  print(c)

def division():
  first_num=float(input("enter the numnominator:"))
  second_num=float(input("enter the demoninator:"))
  if second_num == 0:
        print("Division by zero is undefined")
  else:
   print("result:", first_num/second_num)

def average():
  n1=float(input("enter the value:"))
  n2=float(input("enter the value:"))
  n3=float(input("enter the value:"))
  n4=float(input("enter the value:"))
  n5=float(input("enter the value:"))
  n=5
  c=n1+n2+n3+n4+n5
  d=c/5
  n
  print(d)

def percentage():
  g1=float(input("marks obtanied:"))
  g2=float(input("total marks:"))

  f=g1/g2*100
  print(f)

def square_root():
  v1=float(input("enter the number:"))
  print("square root is:",(math.sqrt(v1)))

def sine():
  f1=float(input("enter angle in degrees:"))
  print("sine:", math.sin(math.radians(f1)))

def tangent():
  m1=float(input("enter angle in degrees:"))
  print("tangent:", math.tan(math.radians(m1)))

def cosine():
  r1=float(input("enter angle in degrees"))
  print("Cosine:", math.cos(math.radians(r1)))  
  

def whatelse():
  print("what else?")





def recalling():
  while True:
    a=int(input(" press 1 for addition,\n press 2 for subtraction,\n press 3 for multiplication,\n Press 4 for division,\n Press 5 for average,\n Press 6 for percentage,\n press 7 for square root,\n press 8 for sine,\n press 9 for tangent, \n press 10 for cosine \n"))
    if a==1:
      print("addition is performing")
      addition()
      whatelse()
      break
    elif a==2:
      print("subtraction is performing")
      substraction()
      whatelse()
      break
    elif a==3:
      print("multiplication is performing")
      multiplication()
      whatelse()
      break
    elif a==4:
      print("division is performing")
      division()
      whatelse()
      break
    elif a==5:
      print("average is performing")
      average()
      whatelse()
      break
    elif a==6:
      print("percentage is performing")
      percentage()
      whatelse()
      break
    elif a==7:
     print("finding square root")
     square_root()
     whatelse()
     break
    elif a==8:
     print("finding sine")
     sine()
     whatelse()
     break
    elif a==9:
     print("finding tangent")
     tangent()
     whatelse()
     break
    elif a==10:
     print("finding cosine")
     cosine()
     whatelse()
     break  
    else:
      print("invalid num, enter a valid num")
      recalling()

def reprint():
    p=int(input("press 1 to repeat a function,\n press 2 to end it \n"))
    if p==1:
        recalling()
        reprint()
    else:
        print("thank you for using my calculator, \n Have a nice day!")

recalling()
reprint()

