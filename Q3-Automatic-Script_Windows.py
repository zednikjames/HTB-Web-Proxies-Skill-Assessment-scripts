import binascii
import base64
import os

print("-"*80)
print("This script will automate fuzzing/brute forcing the end of a hash and will provide you with the list of the hexified strings of those MD5\n")
print("To make the string that you will be using work better once you find the right one, put in a match and replace and make turn on burp proxy and intercept on\n")
print("This will automatically grab your current working directory and will be writing a file specified name of ur choosing in the directory that your currently running this script on\n")
print("I wont give you any steps you have to figure this out on your own if you cant message me on teams or see me in person in class Mon-Wed")
print("-"*80)

CWD = os.getcwd()

SECLIST_PATH = CWD+"\\"+"SecLists"+"\\"+"Fuzzing"+"\\"+"alphanum-case.txt"
