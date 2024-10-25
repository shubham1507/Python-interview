# Using replace method
string = "Hello World, How are you?"
no_whitespace = string.replace(" ", "")
print(no_whitespace)  # Output: HelloWorld,Howareyou?

# Using join and split
no_whitespace = ''.join(string.split())
print(no_whitespace)  # Output: HelloWorld,Howareyou?

"""
I have a file which has 3 rows fname lastname and grade
having values as Shubham, Joshi and A respectively
write a python code which take the file as argument on cmd and print the value

"""

import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Read fname, lastname, and grade from a file")
parser.add_argument("filename", help="Name of the file containing the data")

# Parse arguments
args = parser.parse_args()

# Open the file and read the values
try:
    with open(args.filename, "r") as file:
        # Read the three lines
        fname = file.readline().strip()
        lastname = file.readline().strip()
        grade = file.readline().strip()

    # Print the values
    print(f"First Name: {fname}")
    print(f"Last Name: {lastname}")
    print(f"Grade: {grade}")

except FileNotFoundError:
    print(f"Error: The file '{args.filename}' was not found.")

