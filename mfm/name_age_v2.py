def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """checks that the user responce is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def string_checker(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """checks for usesrs awser and checks it against a walid responce list"""

    while True:

        responce = input(question).lower()

        for item in valid_ans_list:

            if responce == item:
                return item

            # check if it's the first letter
            elif responce == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")


# main routine goes here
payment_ans = ('cash', 'credit')

# Ask user if they want instructions and display if necessary
want_instructions = string_checker("Do you want to see the instructions ")
print(f"you chose {want_instructions}")


# looping
while True:
    print()
    # ask user for their age
    name = not_blank("Name: ")

    # ask for their age and check that there between 12-120 years old
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    pay_method = string_checker("payment method: ", payment_ans, 2)
    print(f"you chose {pay_method}")
    print(f"{name} has bought a ticket({pay_method})")

print("we are done")
