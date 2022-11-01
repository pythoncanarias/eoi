import random
import string

def generate_password(word_length: int, char_options: int):
    # Store the generated password
    password=[]

    # Choose a random item from 'chars' and add it to 'password'
    for i in range(word_length):
        rchar = random.choice(char_options)
        password.append( rchar )

    # Return the composed password as a string
    return password  



if __name__ == '__main__':

    # This script will generate an 18 character password
    word_length = 18

    # Generate a list of letters, digits, and some punctuation
    components = [string.ascii_letters, string.digits, "!@#$%&"]

    chars = []
    # flatten the components into a list of characters
    for clist in components:
        for item in clist:
            chars.append(item)     

    password=generate_password(word_length, chars)

    # Output generated password
    print(f'Your password: { password }')