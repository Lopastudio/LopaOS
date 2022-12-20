import os
import subprocess
import time
import os.path
from os import path
ver = "1.0.0"

def oper_system():
  print ("Welcome")
  print ("in lopaOS")

def help():
    print("1 open help menu")
    print("2 open a notepad++ ")
    print("3 open a paint ")
    print("4 open a LopaOS Writer ")
    print("6 is .py opener. More help for this command you can find in README.TXT")
    print("8 list directory ")
    print("9 FILE MANAGER")
    print("32 are show you your version of operating system")
    print("64 are stop LopaOS ")

      
def calc():

  def add(x, y):
      return x + y

  def subtract(x, y):
      return x - y

  def multiply(x, y):
      return x * y

  def divide(x, y):
      return x / y


  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")

  while True:
      choice = input("Enter choice(1/2/3/4): ")

      if choice in ('1', '2', '3', '4'):
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))

          if choice == '1':
              print(num1, "+", num2, "=", add(num1, num2))

          elif choice == '2':
              print(num1, "-", num2, "=", subtract(num1, num2))

          elif choice == '3':
              print(num1, "*", num2, "=", multiply(num1, num2))

          elif choice == '4':
              print(num1, "/", num2, "=", divide(num1, num2))
          

          next_calculation = input("Let's do next calculation? (yes/no): ")
          if next_calculation == "no":
            break
      
      else:
          print("Invalid Input")#comment


if __name__ == "__main__":
    print("Library successfully loaded")
    print("Library version - " + str(ver))