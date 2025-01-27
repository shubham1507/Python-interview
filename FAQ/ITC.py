"""
Given a string of size n containing lower case letters. We need to find the maximum occurring character in a string. 
If there is more than one character with a maximum occurrence then print any of them.
"""

from collections import Counter

def max_occurence_char(s):
    frequency=Counter(s)
    max_char=max(frequency, key=frequency.get)
    return max_char

def min_occurance_char(s):
    frequency=Counter(s)
    min_char=min(frequency,key=frequency.get)
    return min_char

input_string="aanbcbdyyw"
#print(max_occurence_char(input_string))
#print(min_occurance_char(input_string))
 
"""
 Fibonacci using native method
 """

repetation=10
num1=1
num2=2
next=num2
counter=1

while counter<repetation:
    print(next, end=" ")
    counter+=1
    num1,num2=num2,next
    next=num1+num2
print()


#method2

"""
Given a string "hahahjycfgeshgds". We need to find the maximum occurring character in a string. 
If there is more than one character with a maximum occurrence then print any of them.

use python list comprehension
"""

def max_occuring_char(s):
    # Create a list of counts for each character ('a' to 'z')
    count = [s.count(chr(i + ord('a'))) for i in range(26)]
    
    # Find the maximum count in the list
    max_count = max(count)
    
    # Find the first index that has the maximum count
    max_index = count.index(max_count)
    
    # Convert the index back to the character
    return chr(max_index + ord('a'))

# Example usage
s = "hahahjycfgeshgds"
result = max_occuring_char(s)
print(f"The maximum occurring character is: {result}")
