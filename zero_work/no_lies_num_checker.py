def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return  response

        except ValueError:
            print(error)


while True:
    print()

    # ask user for thier age
    name = input("Name: ")  # replace with 'not blank'

    # ask for their age and check that there btween 12-120 years old
    age = int_check("Age: ")

    #output error message / success message
    if age < 12 :
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
