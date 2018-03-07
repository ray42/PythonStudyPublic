#!/usr/bin/env python3

# p154

#8-12. Sandwiches: Write a function that accepts a list of items a person 
#wants on a sandwich. The function should have one parameter that collects 
#as many items as the function call provides, and it should print a summary 
#of the sandwich that is being ordered. Call the function three times, using
#a different number of arguments each time.
def sandwichmaker(*fillings):
    """ Print out toppings"""
    print(fillings)

sandwichmaker('ham', 'cheese')
sandwichmaker('ham', 'cheese', 'eggs')
sandwichmaker('ham', 'cheese', 'eggs', 'penguin')

#8-13 not done

#8-14. Cars: Write a function that stores information about a car in a 
#dictionary. The function should always receive a manufacturer and a model 
#name. It should then accept an arbitrary number of keyword arguments. Call 
#the function with the required information and two other name-value pairs,
#such as a color or an optional feature. Your function should work for a 
#call like this one:
#
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#
#Print the dictionary that’s returned to make sure all the information was
#stored correctly.
def make_car(manufacturer, model, **others):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in others.items():
        car[key] = value
    
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)

