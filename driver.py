#!/bin/python3

# import the code in string1.py

from stringlib import *
from worker import *
import sys


# Function to test the functions in the stringlib module
def testStringLib(inputStr):
    # Add code to call each of the functions and print the results
    print('\tInput string is ' + inputStr)
    print('\tReverse of string is ' + reverseStr(inputStr))
    print('\tDoes string contain apple? ' + containsWord(inputStr, 'apple'))
    print('\tDoes string contain banana? ' + containsWord(inputStr, 'banana'))
    print('\tIs string a palindrome? ' + isPalindrome(inputStr))
    print('\tUppercase of string is ' + upperCaseStr(inputStr))
    return


# Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    # Add code to create a Worker object
    # Use the object to call each of the methods in the Worker class
    # Print the result of each call
    work = Worker('applelppa')
    print('\tInput string is ' + work.getString())
    print('\tReverse of string is ' + work.reverseStr())
    print('\tDoes string contain apple? ' + work.containsWord('apple'))
    print('\tDoes string contain banana? ' + work.containsWord('banana'))
    print('\tIs string a palindrome? ' + work.isPalindrome())
    print('\tUppercase of string is ' + work.upperCaseStr())
    return


# check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    # call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




