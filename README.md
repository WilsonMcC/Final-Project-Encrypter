Wilson McCormack
Programming for IT CIS-153
5/3/2021




 # Final-Project-Encrypter
This is my final project for Programming for IT CIS-153. This python program uses different imports such as cryptography, base64, and fernet to create a encrypted message or file. First, the user is prompted if they want to encrypt or decrypt a message/file. If chooseing encrypt the user must select which type of encryption from a selection of different types. After the user selects, the message/file is saved and a key is generated. This key can then be used to decrypt the message/file later.




![Untitled Diagram](https://user-images.githubusercontent.com/82771488/115153346-6f91a100-a043-11eb-8581-680002a14eff.png)

# Detailed Instructions

1. Download the encrypter.py file (since tkinter is build into python you won't need to npm install)

2. Run the encrypter.py file in python 

3. You will now see a tkinter GUI pop up with two buttons on each side, encrypt file and decrypt file.![Capture](https://user-images.githubusercontent.com/82771488/117182589-8571c680-ada4-11eb-8859-aca1a790bace.PNG)

4. After clicking the encrypt button, there will now be file browse popup, you will then select the file you want to encrypt. 
![Capture44](https://user-images.githubusercontent.com/82771488/117185581-fa92cb00-ada7-11eb-9334-2803bac9e2c6.PNG)

After selecting open file, there will then be a message indicating that the file you have selected has been encrypted. ![Capture2](https://user-images.githubusercontent.com/82771488/117184391-acc99300-ada6-11eb-94b3-864e62fc86ab.PNG)

5. In same directory where you have selected the file, there should now be an extra file called the same name except with "_encrypted" at the end. This is because there is now an encrypted copy of the file you have selected. The encryption method/library used in this program is Fernet.  

![Capture32](https://user-images.githubusercontent.com/82771488/117184706-0336d180-ada7-11eb-9709-1725836e54c9.PNG) 

![Capture66](https://user-images.githubusercontent.com/82771488/117186399-c7047080-ada8-11eb-91b6-74fe1bb5300e.PNG)

in this screenshot I encrypted Test_Bear.txt so then the program output the file Test_Bear.txt_Encrypted to the directory. As you can see, the copy of the file is completely unreadable after being encrypted by Fernet

6. In the directory where you ran the program, there should now be a file called Key_file.txt. This is the key you will use to decrypt the file copy you have just encrypted.

![Capture44](https://user-images.githubusercontent.com/82771488/117187251-bc96a680-ada9-11eb-83c4-8f3950a3b035.PNG)

7. Now for the decrypting part. Open the python program again and this time click the decrypt button. There will now be a pop-up telling you to choose file you encrypted earlier (this file should end in _encrypted)

![Capture55](https://user-images.githubusercontent.com/82771488/117188283-e56b6b80-adaa-11eb-8d88-ab8b4b84590e.PNG)

![Capture88](https://user-images.githubusercontent.com/82771488/117188787-6f1b3900-adab-11eb-9f3a-9d3a9c1c6209.PNG)

8. After selecting the file there will be another pop-up telling you to select the key file that was generated when you encrypted the file. This is named Key_file.txt

![Capture22](https://user-images.githubusercontent.com/82771488/117189070-c1f4f080-adab-11eb-8dbc-6c5a0bf57b06.PNG)

#![Capture213](https://user-images.githubusercontent.com/82771488/117189890-b229dc00-adac-11eb-9558-8812329d5106.PNG)

9. Lastly there will be a message confirming that that file has been decrypted successfully and it will also display the directory where the file was saved as Decrypted.(file type of file)

![Capture435](https://user-images.githubusercontent.com/82771488/117190084-f61ce100-adac-11eb-8438-a452d53f0e9b.PNG)







## Libraries/Dependancies used

