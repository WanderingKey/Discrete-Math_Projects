while True:
    # Prompt the user to choose between encrypting, decrypting, or quitting
    choice = input("Would you like to (e)ncrypt, (d)ecrypt, or (q)uit? ")
    if choice == 'q':
        break

    # Get the key and message
    key = int(input("Enter the key: "))
    message = input("Enter the message: ")

    # Encrypt or decrypt 
    if choice == 'e':
        # Encrypt the message
        encrypted_message = ""
        for char in message:
            encrypted_message += chr((ord(char) + key) % 256)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        # Decrypt the message
        decrypted_message = ""
        for char in message:
            decrypted_message += chr((ord(char) - key) % 256)
        print("Decrypted message:", decrypted_message)
