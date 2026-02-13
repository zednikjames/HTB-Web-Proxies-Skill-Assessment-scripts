import binascii
import base64

print("-"*80)
print("This script will automate fuzzing/brute forcing the end of a hash and will provide you with the list of the hexified strings of those MD5\n")
print("-"*80)

md5_hash = input("Please provide the MD5 hash that you got from the cookie the original one: ")
fd = open('hex', 'wb')

for char in open("/home/stqrlost/SecLists/Fuzzing/alphanum-case.txt").read():
    base64encoded_string = base64.b64encode(str(md5_hash + "FUZZ".replace("FUZZ", char)).encode('utf-8'))
    hexifiedString = binascii.hexlify(base64encoded_string)
    fd.write(bytes(f"{hexifiedString}\n".encode("utf-8")))