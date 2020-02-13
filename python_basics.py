"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import numpy as np
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num % 2 == 0:
        print(num, ' is even')
    else:
        print(num, ' is odd')


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    num = np.random.randint(low=1, high=10)
    guess = input('Guess a number between 1 and 9...')
    while guess != 'exit':
        if num == int(guess):
            print('You got it right!')
            num = np.random.randint(low=1, high=10)

        elif num < int(guess):
            print('Too high!')
        else:
            print('Too low!')
        guess = input('Guess another number or type "exit" to exit.')

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    l = len(string)
    palin = True
    for i in range(int(l/2)):
        if string[i] != string[l - 1 - i]:
            palin = False
            break
    if palin:
        print(string, ' is a palindrome.')
    else:
        print(string, ' is not a palindrome.')


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    enc_usr = base64.b64encode(username.encode())
    enc_pass = base64.b64encode(password.encode())
    with open(filename, 'wb') as file:
        file.write(enc_usr+b'\n')
        file.write(enc_pass + b'\n')
    file.close()
def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, 'rb') as file:
        lines = file.readlines()
        dec_usr = base64.b64decode(lines[0]).decode()
        dec_pass = base64.b64decode(lines[1]).decode()
    print('Username: ', dec_usr)
    print('Password: ', dec_pass)
    if password is not None:
        with open(filename, 'wb') as file:
            file.write(lines[0])
            file.write(base64.b64encode(password.encode() + b'\n'))


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
