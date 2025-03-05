# Functions go here
def generate_statement(statement, decoration, lines):
    """will make the headings (3 lines), subhaedings(2 lines) and emphasised text / mini-heading (1 line).
       Only use emoji for single line statements"""

    middle = (f"{decoration * 3} {statement} {decoration * 3}")
    top_bottem = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottem)

    else:
        print(top_bottem)
        print(middle)
        print(top_bottem)


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


def instruction():
    generate_statement("Instructions", "⚠️", 1)
    print('''

    For each ticket holder enter ...
    -Thier name
    -Thier name
    -The payment method (cash or credit)
    The program will record the ticket sale and calculate the ticket cost
    (and the profit).
    Once you have either sold all of the tickets or entered the
    exit code ('xxx'), the program will display the ticket sales information
    and write the data to a text file.

    It will also choose one lucky ticket holder 
    who wins the draw (their ticket is free).
    ''')


def not_blank(question):
    """checks that the user responce is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


# main routine
# Initialise ticket numbers

MAX_TICKET = 5
tickets_sold = 0

# intailise variables / non defult opitions
payment_ans = ('cash', 'credit')


generate_statement("mini-movie fundraiser program","😁", 1)

print()
want_instruction = string_checker("do you want to read the instructions")

if want_instruction == "yes":
    instruction()

print()

while tickets_sold < MAX_TICKET:
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # ask for their age and check that there between 12-120 years old
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young for this movie")
        continue
    elif age > 120:
        print(f"{name} This could be a typo please check again")
        continue
    else:
        pass

    pay_method = string_checker("payment method: ", payment_ans, 2)
    print(f"you chose {pay_method}")
    print(f"{name} has bought a ticket({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKET:
    print(f"You have sold all the tickets (ie: {MAX_TICKET} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKET} tickets")
