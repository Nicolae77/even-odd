
while True:
    number = int(input("Enter the number:\n"))
    if number % 2 == 0:
        print("This is even number.")
    else:
        print("This is odd number")
    continue_check = input("Would you like to continue? type 'y', if not 'e' to exit:\n")
    if continue_check == 'y':
        continue
    elif continue_check == 'e':
        break
    else:
        print("You should type 'y' to continue or 'e' to exit")