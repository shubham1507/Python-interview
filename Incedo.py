# Using replace method
string = "Hello World, How are you?"
no_whitespace = string.replace(" ", "")
print(no_whitespace)  # Output: HelloWorld,Howareyou?

# Using join and split
no_whitespace = ''.join(string.split())
print(no_whitespace)  # Output: HelloWorld,Howareyou?
