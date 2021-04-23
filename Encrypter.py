#Wilson McCormack 4/22/2021 Student ID 00322317 Final Project-Encrypter/Decrypter
#This is my final project for Programming for IT CIS-153. This python program uses different imports such as cryptography, base64, and fernet to create a encrypted message or file. First, the user is prompted if they want to encrypt or decrypt a message/file. If chooseing encrypt the user must select which type of encryption from a selection of different types. After the user selects, the message/file is saved and a key is generated. This key can then be used to decrypt the message/file later.


#imports
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
import base64
from tkinter import messagebox

#width and height
root = Tk()
HEIGHT = 300
WIDTH = 400
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = Frame(root, bg='dark slate grey')
frame.place(relwidth=1, relheight=1)
root.title("Wilson McCormack Final")



    





#Open file function

def openfile():
    filename=filedialog.askopenfilename(title="select file")
    print(filename)
    if filename:
        encrypt_file(filename)

def encrypt_file(filename):
    key = Fernet.generate_key()
    filekey = open("Key_file.txt", "wb") 
    filekey.write(key)
    filekey.close()

    file_to_encrypt = open(filename, "rb")
    original = file_to_encrypt.read()
    file_to_encrypt.close()


    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)

    file_to_encrypt = open(filename, "wb")
    file_to_encrypt.write(encrypted)
    file_to_encrypt.close()
    messagebox.showinfo( "Hello Python", "File has been encrypted")



def decrypt_file():
    pass

#Open file button
fileButton = Button(root, text ="Open file", command=openfile)
fileButton.pack(side=TOP)

#Fernet key 

#Encrypt button
Encrypt_file = Button(root, text="Encrypt file", command = openfile)
Encrypt_file.pack(side=LEFT)




















root.mainloop()