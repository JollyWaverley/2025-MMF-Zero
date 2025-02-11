#functions here
def string_checker(question, valid_ans_list, ):
    """checks for usesrs awser and checks it against a walid responce list"""

    while True:

        responce = input(question).lower()

        for item in valid_ans_list:

            if responce == item:
                return item

            #check if it's the first letter
            elif responce == item[0]:
                return item

        print(f"please choose an option from {valid_ans_list}")


#main routine gose here
levels = ['easy', 'medium', 'hard']

like_coffee = string_checker("do you like coffee?  ", ['yes', 'no'])
print(f"you said {like_coffee} to coffee")
print()
choose_level = string_checker("choose a level:",levels)
print(f"You said your level was {choose_level}")