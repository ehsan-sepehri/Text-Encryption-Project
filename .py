while True:
    print("Please enter the number:\n\t1)Encryption\n\t2)Decryption\n\t3)Exit")
    number = input("your number: ")
    if number == "1":
        plain_text = input("text: ")
        encrypted_text = ""
        for i in plain_text:
            x = (ord(i) * 5) + 3
            encrypted_text += chr(x)
        print("encrypted text :",encrypted_text)
        print("-"*30 + "\n")
            
    elif number == "2":
        encrypted_text = input("encrypted text :")
        plain_text = ""
        for i in encrypted_text:
            x = (ord(i) - 3 ) // 5  
            plain_text += chr(x)
        print("plain text:",plain_text)
        print("-"*30 + "\n")
        
    elif number == "3":
        print("have a great day or night !! :)")
        break
        
    else:
        print("your number is wrong!")
        break

