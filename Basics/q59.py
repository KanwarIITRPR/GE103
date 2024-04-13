import random
import string

def ceasar_encrypt(s):
    letters_small = [i for i in string.ascii_lowercase] # Conerting the string of lowercase letters into a list of lowercase letters
    letters_caps = [i for i in string.ascii_uppercase] # Conerting the string of uppercase letters into a list of uppercase letters

    ceasar_shift = random.randint(0, 25) # Setting a random shift acoording to Ceasar's Encryption
    encrypted_message = "" # Initializing the the message that will store the encrypted form of the original message.

    for i in s:
        if i in letters_small: # If the selected letter in the message provided is lowercase then do the following -
            # To the encrpyted message, add the letter that is after "shift" number of elements apart from the original letter
            # To do this, find the index of original letter and add shift to it - thus giving us a new index - but to ensure that this index is present is available in the letters list, take its remainder with the length of the letter list we are using
            encrypted_message = encrypted_message + letters_small[(letters_small.index(i) + ceasar_shift)%len(letters_small)]
        elif i in letters_caps: # If the selected letter in the message provided is lowercase then do the following -
            # To the encrpyted message, add the letter that is after "shift" number of elements apart from the original letter
            # To do this, find the index of original letter and add shift to it - thus giving us a new index - but to ensure that this index is present is available in the letters list, take its remainder with the length of the letter list we are using
            encrypted_message = encrypted_message + letters_caps[(letters_caps.index(i) + ceasar_shift)%len(letters_caps)]
        else:
            # If the letter is neither a lowercase letter nor an uppercase letter, then add it as it is.
            encrypted_message = encrypted_message + i

    return encrypted_message

message = input("Enter the message that you want to encrypt: ")
print(f"The encrypted message is '{ceasar_encrypt(message)}'.")