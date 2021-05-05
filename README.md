Wilson McCormack
Programming for IT CIS-153
5/3/2021




## Final-Project-Encrypter
This is my final project for Programming for IT CIS-153. This python program uses different imports such as cryptography, base64, and fernet to create a encrypted message or file. First, the user is prompted if they want to encrypt or decrypt a message/file. If chooseing encrypt the user must select which type of encryption from a selection of different types. After the user selects, the message/file is saved and a key is generated. This key can then be used to decrypt the message/file later.




![Untitled Diagram](https://user-images.githubusercontent.com/82771488/115153346-6f91a100-a043-11eb-8581-680002a14eff.png)

## Instructions

1. Download the encrypter.py file (since tkinter is build into python you won't need to npm install)

2. Run the encrypter.py file

3. You will now see a tkinter GUI pop up with two buttons on each side, encrypt file and decrypt file

4. After clicking the encrypt button, there will now be file browse popup, you will then select the file you want to encrypt. After selecting a file, there will then be a message indicating that the file you have selected has been encrypted. 

5. In same directory where you have selected the file, there should now be an extra file called the same name except with "_encrypted" at the end. This is because there is now an encrypted copy of the file you have selected. The encryption method/library used in this program is Fernet.

6. In the directory where you ran the program, there should now be a file called Key_file.txt. This is the key you will use the decrypt the file you have just encrypted.

7. 






## Libraries/Dependancies used
