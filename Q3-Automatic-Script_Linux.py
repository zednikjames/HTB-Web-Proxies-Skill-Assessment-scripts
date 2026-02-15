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

FILENAME = input("Enter filename to save your hashed/strings to: ")
FILE_PATH = CWD+"/"+FILENAME
MD5_STR = input("Please provide the string from the md5 that you decoded: ")

print(f"File will be saved at: {FILE_PATH}\n")

DEFAULT_PATH = CWD+"/SecLists/Fuzzing/alphanum-case.txt"

fd = open(FILE_PATH,'wb')

for char in DEFAULT_PATH:
    fuzzed_string = MD5_STR+"FUZZ"

    b64_string = base64.b64encode(fuzzed_string.replace("FUZZ", char).encode("utf-8"))
    hexed_string = binascii.hexlify(b64_string)
    fd.write(hexed_string + b"\n")

print("Writing file...\n")
fd.close()
print("Done")