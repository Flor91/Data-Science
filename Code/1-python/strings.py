from textwrap import dedent  # To keep a nicer flow in your code

import pyperclip


def my_function():
    print("""
          Dear Alice,

          Eve's cat has been arrested for catnapping, cat burglary, and extortion.

          Sincerely,
          Bob
          """)


my_function()

print("Hello".ljust(10, "*"))
print("Hello".rjust(20))
print("Hello".center(20, "="))

pyperclip.copy("GolaGola")

print(pyperclip.paste())

name = "Flor"  # input("What is your name? ")
age = 29  # input("What is your age? ")
print("Hello I'm {0}, my age is {1}".format(name, age))

a = 5
b = 10
print(f"Five plus ten is {a + b} and not {2 * (a + b)}.")
