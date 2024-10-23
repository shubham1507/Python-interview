# leap year

def check_leap(p_yr):
    if (p_yr %4 == 0 | p_yr%100 !=0) or (p_yr % 400):
        return True
    else:
        return False
year=2024       
if check_leap(year):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
    
        
# what is lambda function
# what is decorator
# what is generator
# write and initialize numarray
#how to debug code
#convert 1st char to upper
# pass by value and pass by referece
# how to convert list into string, tuple, dict...
# why we use super keyword
# can we static method
