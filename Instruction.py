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

#functions here
def string_checker(question, valid_ans_list=('yes', 'no'),num_letters=1 ):
    """checks for usesrs awser and checks it against a walid responce list"""

    while True:

        responce = input(question).lower()

        for item in valid_ans_list:

            if responce == item:
                return item

            #check if it's the first letter
            elif responce == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")


#main routine gose here
payment_ans = ['cash', 'credit']

want_instructions = string_checker("Do you want to see the instructions ")
print(f"you chose {want_instructions}")
pay_method = string_checker("payment method: ", payment_ans, 2)
print(f"you chose {pay_method}")

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

