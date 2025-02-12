#functions here
def string_checker(question, valid_ans_list,num_letters):
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

like_coffee = string_checker("do you like coffee?  ", ['yes', 'no'])
print(f"you said {like_coffee} to coffee")
print()

