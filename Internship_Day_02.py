##Task 01= Take two numbers from the user and print: Sum  Difference Product  Division
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# print("Sum of Two Numbers is ", num1+ num2)
# print("Difference of Two Numbers is ", num1 - num2)
# print("Multiplication of Two Numbers is ", num1 * num2)
# print("Division of Two Numbers is ", num1 / num2)

## Task 02= Take a number from the user and determine whether it is: Even or Odd
# num_1 =int(input("Enter a Number:" ))
# if(num_1%2):
#     print("The Number is Odd")
# else:
#     print("The Number is Even")

## Task 03= Take two numbers and print Are they Equal or Not Equal

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# if num1==num2:
#     print("Numbers are Equal")
# else:
#     print("Numbers are Not Equal")

## Task 04 = Logical Operators 
# num1 = int(input("Enter the Age: "))
# num2 = (input("Do you Have ID CARD(Yes/No): "))
# if(num1>= 18 and num2.lower()=="yes"):
#     print("You can Enter")
# else:
#     print("You cannot Enter")

## Task 05 = Assignment Operators
# salary=10000
# salary += 2000
# print("Salary: ", salary)

# Task 05 = Eval Function
# expr = input("Enter expression: ")
# print(eval(expr))

# Task 06 = Command Line Arguments
# import sys

# print("Script Name:", sys.argv[0])

# if len(sys.argv) < 3:
#     print("⚠ Please provide two numbers")
# else:
#     print("First Argument:", sys.argv[1])
#     print("Second Argument:", sys.argv[2])

# from sys import argv
# print(argv[0])
# print(argv[1])
# print(argv[2])

# from sys import argv
# print(argv[1])
# print(argv[0])

# Control Flow Statements 

# num = 1
# print("num==2 condition gives: ", (num==3))
# if num == 2:
#        print("if block statements executed")
# print("out of if block statements")


# Loop Statements 
# for x in range (1,10):
#     print("Pakistan")

# list=[1,2,3,4,5,6,6,7,78,8,9,9,1,234,43]
# for x in list:
#     print(x)

# total=0
# for x in range(1,10):
#     total=total + x
#     print(total)
# print(total)

#Print all odd numbers from 1 to 20 using a loop.

# for x in range(1,21):
#     if x%2!=0:
#         print(x)

#Print sum of all even numbers from 1 to 50
# sum = 0
# for x in range (1,51):
#     if x%2==0:
#         sum = sum + x
# print(sum)

#Find the factorial of a number
 
# fac = 1
# for x in range(1,6):
#     fac= fac*x
# print(fac)

# fac = 1

# for x in range(1, 6):
#     fac = fac * x
#     print("Step", x, ":", fac)


# num1 =int(input("Enter a Number: "))
# fac = 1
# for num1 in range(1,num1+1):
#     fac= fac*num1
# print(fac)

## index Stinging Task 
# a = "Hello Abdul"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# print(a[8])
# print(a[9])
# print(a[10])

# n = "Abdul"
# for x in n:
#     print(x)


# a = "Abdul Qadoos"
# b = 5
# print(a*b)

a = "Abdul Qadoos"
print(len(a))
print(a[11])