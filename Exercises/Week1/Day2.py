# Question: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

try:
    num = input("Choose an number between 1 and 100:")
    if float(num) - int(num) == 0.0:
        if int(num)%2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
    else:
        print("The number you input is not an integer.")
except ValueError:
    print("Please enter a valid number(integer).")