import string

def textstrip(filename):
    f = open(filename, "r")
    contents = f.read()
    f.close()

    final_contents = ""
    for i in contents:
        if i in string.ascii_lowercase:
            final_contents = final_contents + i

    return final_contents


def letter_distribution(s):
    d = {}

    for i in string.ascii_lowercase:
        d.update({i: s.count(i)})

    return d


def substitution_encrypt(s,d):
    final_string = ""

    for i in s:
        final_string = final_string + str(d[i])

    return final_string


def substitution_decrypt(s,d):
    final_string = ""

    for i in s:
        pass


def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''


def vigenere_encrypt(s,password):
    intermediate = ""
    encrypted_string = ""

    for i in range(len(s)):
        intermediate = intermediate + password[i%len(password)]

    for i in range(len(s)):
        encrypted_string = encrypted_string + string.ascii_lowercase[(string.ascii_lowercase.index(s[i]) + string.ascii_lowercase.index(intermediate[i]))%(len(string.ascii_lowercase))]
        
    return encrypted_string


def vigenere_decrypt(s,password):
    intermediate = ""
    decrypted_string = ""

    for i in range(len(s)):
        intermediate = intermediate + password[i%len(password)]

    for i in range(len(s)):
        decrypted_string = decrypted_string + string.ascii_lowercase[(string.ascii_lowercase.index(s[i]) - string.ascii_lowercase.index(intermediate[i]))%(len(string.ascii_lowercase))]
        
    return decrypted_string


def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''


def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''


def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''


def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''


testfile = "testcase2.txt"
password_for_vigenere_encrypt = "z"
file_in_lowercase = textstrip(testfile)
dict_of_lowercase_char = letter_distribution(file_in_lowercase)
encrypted_string = substitution_encrypt(file_in_lowercase, dict_of_lowercase_char)
vigenere_encrypted_string = vigenere_encrypt(file_in_lowercase, password_for_vigenere_encrypt)
vigenere_decrypted_string = vigenere_decrypt(vigenere_encrypted_string, password_for_vigenere_encrypt)

print(file_in_lowercase)
print(dict_of_lowercase_char)
print(encrypted_string)
print(vigenere_encrypted_string)
print(vigenere_decrypted_string)
