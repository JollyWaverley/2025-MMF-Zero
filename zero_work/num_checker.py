def num_checker(question, num_type, exit_code=None):
    """checks the users enter an integer / float that is more than zero
    (or the optional exit code)"""


    if num_type == "integer":
        error = "oops - please enter an integer more than zero than zero."
        change_to = int
    else:
        error = "oops - please enter an integer more than zero than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response


        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
# main routine

#loop for testing
while True:
    print()

    my_float = num_checker("please enter a number more than 0",float)
    print()
    my_int = num_checker("Please enter an integer more than 0","interger")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose{my_int}")


