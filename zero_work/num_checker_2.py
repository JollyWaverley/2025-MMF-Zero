def int_checker(question, low, high):
    """checks users enter an integer between two values)"""

    error = f"Oops - Please enter an integer between {low} and {high}."

    while True:

        try:

            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# loop for testing
while True:
    print()

    my_num = int_checker("Choose a number : ", 1, 10)
    print(f"You chose {my_num}")
