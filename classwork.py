# # Python review function introduction
#
# ### Problem 1
# Create a ```printNumbers``` function to print integers from -25 to 20 to the console (print in the function)
#
def printNumbers():
    for x in range(-25, 21):
        print(x)
# ### Problem 2
# Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal.
# Return true if they are equal and false if they are not equal. Print the function's return value.
#
def checkPassword(password1, password2):
    if password2 == password1:
        return True
    else:
        return False

# ### Problem 3
# Write a function that determines if a number passed to it is odd or even. Pass a number of your choosing (using input a good idea)
# and then using the result from the function, print if the number was even or not.
#
# examples:
# ```
# The number 12 is an even number!
#
# The number 5 is an odd number!
# ```
def numEntered():
    userNum = int(input("Enter a number "))
    if userNum % 2 == 0:
       print(f'The number {userNum} is an even number')
    else:
        print(f'The number {userNum} is an odd number')

# ### Problem 4
# * Create a function for the challenge that you call from your ```main```
# * Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```) and returns a string using
# the passed in greeting and 'World' (ex. ```Howdy World!```)
# * From your *first* function, call the function(s) and print out the final result returned
def call():
    print(f2())

def f2():
    # !! : this could easily be user input instead of hard coded 
    return f3("Hello")

def f3(greeting):
    userGreeting = greeting + ' World'
    return userGreeting

# ### Problem 5:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def repeat():
    userInput = ''
    while userInput !='q':
        userInput = input("Enter a string. Enter 'q' to quit")

# ### Challenge
# Create a function that accepts 2 numbers. When the function is called return the sum, difference, product, and quotient as 4 separate return values.
# Print the 4 results that are returned using f-strings.
# Example: If 2 and 6 are passed into the function, output should be similar to the following:
# ```
# The sum of 2 + 6 is 8
# The difference of 2 - 6 is  -4
# The product of 2 * 6 is 12
# The quotient of 2 / 6 is .333
# ```

def main():
    #problem 1
    printNumbers()
    #problem 2
    userInput1 = input("Enter a password")
    userInput2 = input("Please confirm your password")
    print(checkPassword(userInput1, userInput2))
    #problem 3
    numEntered()
    #problem 4
    call()
    #problem 5
    repeat()

main()