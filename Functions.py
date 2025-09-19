# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 22:26:10 2025

@author: Engr_Hassan_Khan
"""

# functions

# Function without parameters

def name():
    print("My name is Python!")



for i in range(1,11):
    name()

"""
OUTPUT:

    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!
    My name is Python!

"""


for i in range(3):
    print("")
    name()

"""
OUTPUT:
    My name is Python!

    My name is Python!

    My name is Python!
"""

for j in range(10):
    print("*",end='')

"""
OUTPUT:
    **********
"""

for k in range(2):
    print()

# FUNCTIONS WITH PARAMTERS

# Program to check two numbers are equal or not using Functions with
# Arguments

def match(b,a):
    if a==b:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))

match(x,y) # x will pass value to a, y will pass value to b

"""
OUTPUT:
    Enter First number: 9
    Enter Second number: 9
    Numbers are equal
"""

# Program to create table
# Function with Arguments

def tab(n):
    for q in range(1,11):
        print(f"{n}x{q}={n*q}")

num1 = int(input("Enter a positive number: "))
tab(num1)

"""
OUTPUT:
    Enter a positive number: 6
    6x1=6
    6x2=12
    6x3=18
    6x4=24
    6x5=30
    6x6=36
    6x7=42
    6x8=48
    6x9=54
    6x10=60

"""