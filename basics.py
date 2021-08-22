# single line comments
'''
multiline comments

'''

###### importing modules ##########
import sys
import os
import random

# to import Python 2 module into Python 3 module
# from __future__ import division

###### print statement #########
print("Hey There!")
# python is an interpreter language and hence it executes code line by line... for example -
print("Welcome to the Python 3 learning session!")
print('*' * 10)

# using quote in string, multiline string, concatenating different types of strings in print statement
quote = "\"This is the way to use one double quote into double quoted string"
quote_single = 'You can also use " inside single quoted string'
multi_line_quote = ''' This is a 
multi line quote
and looks similar to the multiline comment
'''
print("%s %s %s %s" % ("Here I am concatenating quotes!", quote, quote_single, multi_line_quote))

# Printing new line
print("\n This will write on new line every single time" * 5)
print("Using 'end' method to avoid", end="")
print(" new line")
print("\n")

########### receiving input from the user ##########
name = input("What is your name? ")
print("Hello " + name)

# or receiving input using sys module
print("Which session you want to enter to?")
session = sys.stdin.readline()
print("Welcome to the session of ", session)
