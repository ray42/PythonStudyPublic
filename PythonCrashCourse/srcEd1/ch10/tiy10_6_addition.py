import sys

def get_number():
    """Get the numbers to be added"""
    num_str = ''
    while not num_str.isdigit():
        num_str = input('Enter number: ')
    
        try:
            num = int(num_str)
        except ValueError:
            print("Please enter a numerical value")
    
    return num

num1 = get_number()
num2 = get_number()

sumofnums = num1 + num2
print("Sum of " + str(num1) + " and " + str(num2) + " is: " + str(sumofnums))

