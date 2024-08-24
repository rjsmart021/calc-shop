#Module 2 Lesson 5: Assignments | Python Functions
#The Calculator App
#Task 1: Create functions for each arithmetic operation.
def sum_num(num1,num2):
    try:
        print(num1+num2)
    except ValueError:
        return print("Start Over")
def dif_num(num1,num2):
    try:
        print(num1-num2)
    except ValueError:
         return print("Start Over")
def multip_num(num1,num2):
    try:
        print(num1*num2)
    except ValueError:
        return print("Value error")
def div_num(num1,num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        return print("Zero division error")
#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
x = float(input("Select operation 1.Add, 2.Subtract, 3.Multiply, 4.Divide"))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if x == 1:
    sum_num(num1,num2)
elif x == 2:
    dif_num(num1,num2)
elif x == 3:
    multip_num(num1,num2)
elif x == 4:
    div_num(num1,num2)
else:
    print("Please choose a valid input")
#2.The Shopping List Maker 
#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a function to remove items from the list.
Shoping_list = []
def add_item():
    return Shoping_list.append(input("input an item to a1dd name"))
def remove_item():
    return Shoping_list.remove(input("input item to remove"))
#Task 3: Add a function that prints out the entire list in a formatted way.
x = float(input("Select operation 1.Add item, 2.Remove item"))
if x == 1: 
    add_item()
    print(Shoping_list)
elif x == 2:
    item_2 = input("input an item in list to remove")
    remove_item()
    print(Shoping_list)
else:
    print("Invalid responce choose again")
