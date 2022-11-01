import random
import argparse
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

    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument('word_length', type=int, help='length of the password')
    parser.add_argument('-A', '--ascii', type=int, default=1, help='if 1, it will use ascii characters, 0 if not')
    parser.add_argument('-D', '--digits', type=int, default=1, help='if 1, it will use digits, 0 if not')
    parser.add_argument('-P', '--punctuation', type=int, default=1, help='if 1, it will use puctuation [!@#$%&], 0 if not')

    args = parser.parse_args()

    # This script will generate an password
    word_length = args.word_length
    use_ascii = args.ascii
    use_digits = args.digits
    use_punctuation = args.punctuation

    # Generate a list of letters, digits, and some punctuation
    components = []

    if use_ascii:
        components.append(string.ascii_letters)

    if use_digits:
        components.append(string.digits)

    if use_punctuation:
        components.append("!@#$%&")

    # flatten the components into a list of characters
    chars = []
    for clist in components:
        for item in clist:
            chars.append(item)

    # Output generated password
    print(f'Your password: {generate_password(word_length)}')
