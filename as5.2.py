# 5.2 Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'.
#
# Once 'done' is entered, print out the largest and smallest of
# the numbers.
#
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number.
#
# Enter 7, 2, bob, 10, and 4 and match the output below.
#
# Desired output:
#_______________
#
# Invalid input
# Maximum is 10
# Minimum is 2
#_______________

#prime the loop with None variable and assign to variables
largest = None
smallest = None
#begin infinite loop to ask for integer from user
while True:
    usr_inp = input('Enter a number: ')
    if usr_inp == 'done' :
        break
#make exception and punish user for not entering an int
    try :
        num = int(usr_inp)
    except :
        print('Invalid input')
    #continue until user figures out they need to enter a number (integer)
        continue
    #look for smallest and largest values and assign to num
    #so if the primer for smallest is 'None' as it is.. make smallest the int!! variable 'num'
    if smallest is None :
        smallest = num
    #else if 'num' is less then the 'smallest' user input assign smallest to the 'num' input from user
    #don't forget you made num an int and not a string! math not english (-;
    elif num < smallest :
        smallest = num
    #and if the primer for largest is 'None' just like it is.. make largest the int!! variable 'num'
    if largest is None :
        largest = num
    #else if 'num' is less then the 'smallest' user input assign smallest to the 'num' input from user
    elif num > largest :
        largest = num
#print largest and smallest numbers from user with 'Maximum is' each with their own line as per requirement
#error of 'Invalid input' as required by assignment will print as sequential instructions dictate
print('Maximum is', largest)
print('Minimum is', smallest)

