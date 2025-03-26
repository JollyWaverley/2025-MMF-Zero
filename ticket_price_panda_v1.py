import pandas


def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in. \n to try again")


def string_checker(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """checks for users answer and checks it against a walid response list"""

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

# ticket price
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENOIR_PRICE = 6.50

# lists to hold tickets details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'ticket price': all_ticket_costs,
    'Surcharge': all_surcharges
}
# credit surcharge 5%
CREDIT_SURCHARGE = 0.05

# looping
while True:
    print()
    # ask user for their age
    name = not_blank("Name: ")
    if name == "xxx":
        break

    # ask for their age and check that there between 12-120 years old
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    # child ticket price
    elif age < 16:
        ticket_price = CHILD_PRICE

    elif age < 65:
        ticket_price = ADULT_PRICE

    elif age < 121:
        ticket_price = SENOIR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method
    pay_method = string_checker("payment method: ", payment_ans, 2)

    if pay_method == "cash ":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# create dataframe / table from dicionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable and profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['ticket price'] + mini_movie_frame['Surcharge']
mini_movie_frame['profit'] = mini_movie_frame['ticket price'] - 5

# work out the total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['profit'].sum()

print(mini_movie_frame)
print()
print(f"Total paid: ${total_paid:.2f}")
print(f"Total profit ${total_profit:.2f}")
