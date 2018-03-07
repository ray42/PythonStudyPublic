
#p199
#10-3. Guest: Write a program that prompts the user for their name. When they
#respond, write their name to a file called guest.txt.
def guest():
    """Program to write a person's name in a file."""
    name = input('Please enter your name: ')

    with open('guest.txt', 'w') as file_object:
        file_object.write(name + '\n')

guest()

#10-4. Guest Book: Write a while loop that prompts users for their name. When
#they enter their name, print a greeting to the screen and add a line recording
#their visit in a file called guest_book.txt. Make sure each entry appears on a
#new line in the file.

class GuestBook():
    """Some class"""

    def __init__(self):
        pass

    def guest_book(self):
        """guest book function"""
        with open('guest_book.txt', 'a') as file_object:
            name = ''
            while True:
                name = input('Please enter your name: ')
                if name == 'q':
                    break

                file_object.write(name + '\n')

gb = GuestBook()
gb.guest_book()
                
#10-5. Programming Poll: Write a while loop that asks people why they like
#programming. Each time someone enters a reason, add their reason to a file
#that stores all the responses.

#Not done, this is very similar to 10-4

