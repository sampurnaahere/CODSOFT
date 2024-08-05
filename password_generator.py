import random
import string

def password_generator():
    print ("Welcome to Password Generator")
    password_len = int(input("enter the desired length of the password:"))

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(password_len))

    print ("generated password :", password)

while True:
    password_generator()
    ch = input ("Do you want to create another one ?(yes/no) :")
    if ch=="no":
        print ("Thank you for visiting")
        break
