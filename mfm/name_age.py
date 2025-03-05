def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


while True:
    print()

    # ask user for thier age
    name = input("Name: ")  # replace with 'not blank'

    # ask for their age and check that there btween 12-120 years old
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")


def not_blank(question):
    """checks that the user responce is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


# main rouetine starts here
who = not_blank("please enter your name:  ")
print(f"hello {who}")


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


# main routine gose here
payment_ans = ['cash', 'credit']

want_instructions = string_checker("Do you want to see the instructions ")
print(f"you chose {want_instructions}")
pay_method = string_checker("payment method: ", payment_ans, 2)
print(f"you chose {pay_method}")

# looping
while True:
    print()

    # ask user for thier age

    # ask for their age and check that there btween 12-120 years old
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
