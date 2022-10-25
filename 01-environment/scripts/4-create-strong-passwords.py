import random
import string


def generate_password(word_length: int):
    # Store the generated password
    password = []

    # Choose a random item from 'chars' and add it to 'password'
    for _ in range(word_length):
        rchar = random.choice(chars)
        password.append(rchar)

    # Convert array to string
    str_password = "".join(password)

    # Return the composed password as a string
    return str_password



if __name__ == '__main__':

    # This script will generate an 18 character password
    word_length = 18

    # Generate a list of letters, digits, and some punctuation
    components = [string.ascii_letters, string.digits, "!@#$%&"]

    # flatten the components into a list of characters
    chars = []
    for clist in components:
        for item in clist:
            chars.append(item)

    # Output generated password
    print(f'Your password: {generate_password(word_length)}')
