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