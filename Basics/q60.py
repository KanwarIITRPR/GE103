import string
import random
import math

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other special characters removed.
    What remains is only the lower case letters, retain only the lowercase letters!'''

    f = open(filename, "r") # Opening the required file in Read-Only mode
    contents = f.read() # Readding the text written in the file
    f.close() # Closing the file

    final_contents = "" # Initializing the sorage of the lowercase letters in order
    for i in contents:
        if i in string.ascii_lowercase: # If the current character is a lowercase letter, then add it to the final text
            final_contents += i

    return final_contents

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters.
    Count the number of occurrences of each letter and return a dictionary.'''

    dict_of_letter_occurences = {} # Initializing the dictionary which counts the occurences of all letters

    for i in string.ascii_lowercase:
        dict_of_letter_occurences.update({i: s.count(i)}) # Adding the times a particular letter has appeared in the given string (contents of the text file)

    return dict_of_letter_occurences

def substitution_encrypt(s,d):
    '''Encrypt the contents of s by using the dictionary d which comprises of the substitutions for the 26 letters. Return the resulting string'''

    final_string = "" # Initializing the string which will contain the encrypted message

    for i in s:
        final_string += str(d[i]) # Adding the letter to the final string which corresponds to the current letter in the dictionary

    return final_string

def substitution_decrypt(s,d):
    '''Decrypt the contents of s by using the dictionary d which comprises of the substitutions for the 26 letters. Return the resulting string'''

    final_string = "" # Initializing the string which contains the decrypted message
    
    for i in s:
        final_string += list(d.keys())[list(d.values()).index(i)] # Adding the letter to the final string which is the key of the current "value" (letter in encrypted message)
        # list(d.keys()) gives all the "keys" present in the dictionary as a list
        # list(d.values()) gives all the "values" present in the dictionary as a list

    return final_string

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was encrypted using some substitution cipher, predict the d'''

    general_letter_frequency = [i for i in "etaoinshrdlcumwfgypbvkjxqz"] # This list contains the most used letters in general texts in descending order

    dict_of_distribution_char = letter_distribution(s) # This provides a dictionary which contains all the lowercase letters and their respective occurences
    string_alphabetical__frequency_only = [i for i in list(dict_of_distribution_char.values())] # This list contains the "values" (times used) of all the letters in alphabetical order
    string_sorted__frequency_only = string_alphabetical__frequency_only.copy() # This list contains "only frequencies" but as a copy so as to not alter the original list
    string_sorted__frequency_only.sort(reverse = True) # This command puts the "frequency only" list in descending order

    string_letter_frequency = [] # This list contains the most used letters in the string in descending order
    for i in string_sorted__frequency_only: # We will map, the descending order of letters generally used to descending order of letters of the string - thus using a descendingly ordered list and start way adding the elements
        string_letter_frequency.append(list(dict_of_distribution_char.keys())[string_alphabetical__frequency_only.index(i)]) # Adding the letter which corresponds to the current frequency (which is in already in descending order)
        # list(dict_of_distribution_char.keys()) represents a list containing the "keys" (letters) which are to stored according to descending order of occurence
        # string_alphabetical__frequency_only.index(i) represents index at which the current frequency is kept in the alphabetically order list so as to quickly find the corresponding letter
    
    d_predict = {} # Initializing the dictionary that will store the predictions of which letter was replaced by which letter

    for i in range(len(general_letter_frequency)):
        d_predict.update({string_letter_frequency[i]: general_letter_frequency[i]}) # Stores the key-value pair in the format of <letter in string> corresponds actually to <letter in original message>

    return d_predict

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and return the resulting string'''
    
    intermediate = "" # Stores the password in a repeated form till it repeats or terminates till the length of the message
    encrypted_string = "" # Initializing the string which will store the encrypted form of the message

    for i in range(len(s)): # Adding password repeadtedly to "intermediate" until intermediate's length is the same as the message
        intermediate += password[i%len(password)] # Taking modulus with respect to length of the password to generate a repeated pattern and avoid having IndexError

    # Encrypting the message by mapping each letter of intermediate to the letter in the message at that index
    for i in range(len(s)): # Encryption is done by adding the indices of both the letters and finding the net index (if exceeds then taking modulus) and puting the letter corresponding to that in the encrpyted string
        index_message = string.ascii_lowercase.index(s[i])
        index_intermediate = string.ascii_lowercase.index(intermediate[i])
        encrypted_string += string.ascii_lowercase[(index_message + index_intermediate)%26] # Taking modulus with respect to 26 as it the length of the string that contains all the lowercase letters - helpful in handling IndexError

    return encrypted_string

def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and return the resulting string'''

    intermediate = "" # Stores the password in a repeated form till it repeats or terminates till the length of the message
    decrypted_string = "" # Initializing the string which will store the decrypted form of the encrypted message

    for i in range(len(s)): # Adding password repeadtedly to "intermediate" until intermediate's length is the same as the message
        intermediate += password[i%len(password)] # Taking modulus with respect to length of the password to generate a repeated pattern and avoid having IndexError

    # Encrypting the message by mapping each letter of intermediate to the letter in the message at that index
    for i in range(len(s)): # Encryption is done by subtracting the indices of both the letters (encrypted letter - password letter) and finding the net index (if exceeds then taking modulus) and puting the letter corresponding to that in the decrpyted string - so as to get back to the string
        index_message = string.ascii_lowercase.index(s[i])
        index_intermediate = string.ascii_lowercase.index(intermediate[i])
        decrypted_string += string.ascii_lowercase[(index_message - index_intermediate)%26] # Taking modulus with respect to 26 as it the length of the string that contains all the lowercase letters - helpful in handling IndexError
        
    return decrypted_string

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and returns the proportion of collisions'''

    proper_collisions = 0 # Initializing the number of collisions which represent the number of times the same letter has repeated
    for i in range(len(s)):
        if s[i] == s[(r+i)%len(s)]: # Comparing (i+1)th term and ((i+1)+r)th term - and if they match, we will add 1 to proper collisions as it satisfies its conditions
            proper_collisions += 1
    
    return (proper_collisions/len(s))*100 # Returning the percentage of proper collisons in the total content

def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which some text has resulted in the string s.
    We just need to return the number k.'''

    rotation = 1 # Initialzing the number of rotations we are at - so at to know from which rotation to which rotation we found jump in comparing - as we are using rotate_compare()
    start = False # Initializing the variable that indicates the start of recording the "rotation" - when first time the jump comes
    final = False # Initializing the variable that indicates the finish of recording the "rotation" - when the jump comes again
    while start == False or final == False:
        current_percentage = rotate_compare(s, rotation) # Storing the percentage of letters that were same when rotated by the current "rotation"

        if math.floor(current_percentage) == 6: # The required "jump" is the around 6% while the general percentage of letters being same is 3.84%
            if start == False: # If noting the rotation hasn't started yet but the jump has occured, store the current rotation as starting rotation - and change "start" to true because the recording has started
                rotation_start = rotation
                start = True
            else: # If noting the rotation has started and the jump has occured, store the current rotation as finishing rotation - and change "final" to true because the recording has finished - so as to stop the while loop
                rotation_end = rotation
                final = True

        rotation += 1 # Going through an incremented rotation everytime the loop runs

    return rotation_end - rotation_start # Returning the length of the password as length = end - start

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a password of length k, find out what is the password'''

    vigenere_pass = "" # Initializing the password which was used to encrypt the message
    for i in range(k): # Running the "for" loop k times as the program divides the encrypted message into k parts - each part contains a string which is made using the fact that the indices of all the letters are in the form of: <multiple of k> + <remainder (from 0 to k-1)> - thus divided into remainder categories
        string_with_same_pass_letter = "" # Initializing the string which will contain al the letters with same remainder category
        for j in range(0, len(s), k): # Remainder category established using "k" steps
            if i + j < len(s): # To avoid getting IndexError or overwriting the text
                string_with_same_pass_letter += s[i+j]

        letter_frequency = letter_distribution(string_with_same_pass_letter) # Finding the frequencies (occurences) of letters in the string with same remainder category
        frequencies = list(letter_frequency.values()) # Extracts the frequencies of letters in a separate list
        letter_with_max_frequency = list(letter_frequency.keys())[frequencies.index(max(frequencies))] # Extracts the letter with highest frequency/occurence - will be matched with "e" as it is supposed to be the letter that will occur more frequently in a text
        
        index_max_freq = string.ascii_lowercase.index(letter_with_max_frequency) # Sets the index of the letter with maximum frequency with respect to lowercase letters
        index_e = string.ascii_lowercase.index("e") # Sets the index of e with respect to lowercase letters
        vigenere_pass += string.ascii_lowercase[(index_max_freq - index_e)%26] # Taking modulus with respect to 26 as it the length of the string that contains all the lowercase letters - helpful in handling IndexError

    return vigenere_pass

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as the plaintext'''
    
    length_password = cryptanalyse_vigenere_findlength(s) # Predicting the length of the password by providing the encrypted message
    password = cryptanalyse_vigenere_afterlength(s, length_password) # Predicting the password using the encrypted message and it's predicted length

    decrpyted_message = vigenere_decrypt(s, password) # Carries out the normal vigenere decrypt as we know the encrypted string and the password used to generate it

    return password, decrpyted_message

testfile = "GE103/english_random.txt" # File to be worked on
text_in_file = textstrip(testfile) # Retaining all the lowercase text present in the given file
print(f"The lowercase letters in the text file are: {text_in_file}.")

# Making the dictionary to be used for normal substitution cipher
random_lowercase_char = [i for i in string.ascii_lowercase] # Getting all the lowercase letters in a list
random.shuffle(random_lowercase_char) # And then randomizing the list
dict_for_encryption = {string.ascii_lowercase[i]: random_lowercase_char[i] for i in range(len(string.ascii_lowercase))} # Finally adding them to the dictionary that will be used to encrpyt messages
# For each lowercase letter, it "picks" a random letter and makes a dictionary out of it
print(f"The dictionary used for encryption of the message is: {dict_for_encryption}.")

# Encrpyting the entered message using the dictionary made for encryption
encrypted_string = substitution_encrypt(text_in_file, dict_for_encryption)
print(f"The message encrypted using the dictionary is {encrypted_string}.")

# Decrpting the message that was encrypted using the encrpyted dictionary
decrypted_string = substitution_decrypt(encrypted_string, dict_for_encryption)
print(f"The encrypted message when decypted is: {decrypted_string}.")

# Predicting the dictionary that we have used to "substitute encrypt" the message - using the law of large data
d_predicted = cryptanalyse_substitution(encrypted_string)
print(f"The dictionary used to encrypt the message is predicted to be: {d_predicted}.")

# Encrypting the entered message using vigenere method of encryption where a password is required - according to which the content is altered
password_for_vigenere_encrypt = "asknkheajjoiahfoihoiaqflklfhfpiehfuuhmpihuguxorkr" # Password to be used for vigenre encryption
vigenere_encrypted_string = vigenere_encrypt(text_in_file, password_for_vigenere_encrypt)
print(f"The message encrypted using the vigenere method of encryption is: {vigenere_encrypted_string}.")

# Decrypting thr message that was encrpyted using the password that was required - reverse engineering it to get back to the original contents
vigenere_decrypted_string = vigenere_decrypt(vigenere_encrypted_string, password_for_vigenere_encrypt)
print(f"The vigenere enctypted message when decrypted is: {vigenere_decrypted_string}.")

# Predicting the length of the password used to vigenere encrypt the original message just by seeing the vigenere encrypted string
vigenere_pass_length = cryptanalyse_vigenere_findlength(vigenere_encrypted_string)
print(f"The predicted length of the password used to vigenere encrypt the message is: {vigenere_pass_length}.")

# Predicting the password used to vigenere encrypt the original message just by seeing the length of the password (which was predicted)
predicted_vigenere_pass = cryptanalyse_vigenere_afterlength(vigenere_encrypted_string, vigenere_pass_length)
print(f"The password that is used to vigenere encrypt the message is predicted as: {predicted_vigenere_pass}.")

# Predicting the original message that was encrypted using vigenere method of encryption
predicted_vigenere_pass, predicted_vigenere_decrypted_message = cryptanalyse_vigenere(vigenere_encrypted_string)
print(f"The password that is used to vigenere encrypt the message is predicted as: {predicted_vigenere_pass}.")
print(f"The vigenere encrypted message when decrypted is predicted as: {predicted_vigenere_decrypted_message}.")