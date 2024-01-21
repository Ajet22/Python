from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2
def subract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

cal = {
  "+":add,
  "-":subract,
  "*":multiply,
  "/":divide
}

def caluclator():
  print(logo)
  num1 = float(input("What is the first number:\n"))
  for key in cal:
    print(key)
  value = True
  while value:
    symbol = input("Pick an operation :\n")
    if symbol in cal:
      num2 = float(input("What is the next number:\n"))
      operation = cal[symbol]
      if operation=="":
        print("Please Enter valid input value\n")
      answer = operation(num1,num2) 
      print(f"{num1}{symbol}{num2} = {answer}")
      uservalue = input(f"If you want to continue with calulcation using {answer}. Type \"Y\" or \"N\" to continue with new caluclation:\n").lower()
      if uservalue == "y":
        num1 = answer
      elif uservalue=="n":
        value = False
        clear()
        caluclator()
      else:
        print("Please enter valid input \n")
        value = False
    else:
      print("Please Enter valid input value\n")
caluclator()
    
  