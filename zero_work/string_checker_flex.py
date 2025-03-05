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

