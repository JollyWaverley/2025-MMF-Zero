# funtion here
def yes_no(question):


    while True:
        responce = input(question).lower()


        if responce == "yes" or responce == "y":
            return "yes"
        if responce == "no" or responce == "n":
            return "no"

        else:print("please enter yes or no")

#main route here

#loop for testing
while True:
    want_instruction = yes_no("would you like to read the instructions? ")
    print(f"you chose{want_instruction}\n")




