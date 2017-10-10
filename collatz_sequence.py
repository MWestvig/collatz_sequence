# This programme takes a user's input and creates a Collatz Sequence with it.


def collatz(number):
    if number % 2 == 0:            # Checks if the number is even
        return number // 2
    else:                          # Else assumes number is odd
        return 3 * number + 1


while True:
    try:
        collatz_number = int(input("Enter the number you would like to apply the Collatz Sequence to: "))
    except ValueError:
        # Value entered is not a valid number, so the user gets asked again
        print("Value entered isn't a valid number, please enter an integer.")
        continue
    else:
        # Value entered is a valid number and we can exit the loop
        break

while collatz_number != 1:         # Prints the Collatz Sequence until it reaches 1
    collatz_number = collatz(collatz_number)
    print(collatz_number)
