#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
#
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
#
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.


class Worker:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    # reverseStr - takes as input a string and returns the reverse of it
    #
    def reverseStr(self):
        return self.string[::-1]

    # containsWord - takes as input two strings, containingStr and containedStr,
    # and returns "Yes" if containedStr is anywhere within containingStr
    # and returns "No" otherwise
    #
    def containsWord(self, containedStr):
        if containedStr in self.string:
            return "Yes"
        else:
            return "No"

    # isPalindrome - takes as input a string and returns "Yes" if it is
    # palindrome and "No" otherwise
    def isPalindrome(self):
        if self.string == self.string[::-1]:
            return "Yes"
        else:
            return "No"

    # upperCaseStr - takes as input a string and returns the identical string
    # with the characters 'a' ... 'z' changed to uppercase
    def upperCaseStr(self):
        return self.string.upper()
