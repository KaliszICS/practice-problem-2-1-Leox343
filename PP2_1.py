'''
Lesson 2.1
created by Leo Xu
created on oct 9, 2024
last edited oct 9, 2024
'''

def q1(): 
  #Write Assignment code here
  num = input("In: ")
  num = int(num)
  num1 = num % 2
  if num1 == 1:
    print(f"{num} is odd")
  if num1 == 0:
    print(f"{num} is even")

def q2(): 
  #Write Assignment code here
  name = input("In: ")
  if name == "Kalisz":
    print("teacher")
  if name != "Kalisz":
    print("student")


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
