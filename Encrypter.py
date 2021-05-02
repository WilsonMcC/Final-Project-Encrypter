#Wilson McCormack 4/22/2021 Student ID 00322317 Final Project-Encrypter/Decrypter
#This is my final project for Programming for IT CIS-153. This python program uses different imports such as cryptography, base64, and fernet to create a encrypted message or file. First, the user is prompted if they want to encrypt or decrypt a message/file. If chooseing encrypt the user must select which type of encryption from a selection of different types. After the user selects, the message/file is saved and a key is generated. This key can then be used to decrypt the message/file later.


#imports
import time
from time import strftime
import tkinter.messagebox 
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
import base64
from tkinter import messagebox

#width and height
root = Tk()
HEIGHT = 0
WIDTH = 400
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = Frame(root, bg='dark slate grey')
frame.place(relwidth=1, relheight=1)
root.title("Wilson McCormack Final")



#Open file function

def openfile_encrypt():
    filename=filedialog.askopenfilename(title="select file")
    print(filename)
    if filename:
        encrypt_file(filename)

def openfile_decrypt():
    messagebox.showinfo( "Decrypt key", "Please select the file you want to decrypt")
    filename=filedialog.askopenfilename(title="select file to decrypt")
    print(filename)
    if filename:
        messagebox.showinfo( "Decrypt key", "Please select the key file")
        keyname=filedialog.askopenfilename(title="Select the key for the file to decrypt")
        decrypt_file(filename, keyname)

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

    file_to_encrypt = open(filename + "_Encrypted", "wb")
    file_to_encrypt.write(encrypted)
    file_to_encrypt.close()
    messagebox.showinfo( "Encrypt", "File has been encrypted")



def decrypt_file(filename, keyname):
    key_contents = None
    with open(keyname, "rb") as f:
        key_contents = f.read()
    try:
        fernet = Fernet(key_contents)
    except:
        messagebox.showerror(title = "ERROR", message = "Please select a valid key file.")
        return
    file_to_decrypt = open(filename,"rb")
    file_contents = file_to_decrypt.read()
    file_to_decrypt.close()

    extension_list = filename.split(".")
    extension = extension_list[len(extension_list)-1]
    extension = extension.replace("_Encrypted","")


    try:
        decrypted_data = fernet.decrypt(file_contents)
    except:
        messagebox.showerror(title = "ERROR", message = "Please select a valid encrypted file and key.")
        return
    Decrypted_file = open("Decrypted." + extension, "wb") 
    Decrypted_file.write(decrypted_data)
    messagebox.showinfo( "Decrypted", filename + "\n\nHas been decrypted as Decrypted." + extension)





#Fernet key 

#Encrypt button
Encrypt_file = Button(root, text="Encrypt file", command = openfile_encrypt)
Encrypt_file.pack(side=LEFT)

#Decrypt button
Encrypt_file = Button(root, text="Decrypt file", command = openfile_decrypt)
Encrypt_file.pack(side=RIGHT)



lbl = Label(root, font = ('Helvetica', 40, 'bold'),
            background = 'dark slate grey',
            foreground = 'white')

def clock():
    string = strftime('%I:%M:%S %p %b %d')
    lbl.config(text = string)
    lbl.after(1000, clock)

lbl.pack(anchor = 'center')
clock()









root.mainloop()