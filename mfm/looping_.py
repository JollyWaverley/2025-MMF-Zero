# Initialise ticket numbers
MAX_TICKET = 5
tickets_sold = 0

while tickets_sold < MAX_TICKET:
    name = input("Name: ")

    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKET:
    print(f"You have sold all the tickets (ie: {MAX_TICKET} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKET} tickets")