import pandas
import random

# lists to hold tickets details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'ticket price': all_ticket_costs,
    'Surcharge': all_surcharges
}
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

# choose random winner...
winner = random.choice(all_names)

# find index of the winner(ie: position in lost)
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index,)




# retrieve Total won
total_won = mini_movie_frame.at[winner_index, 'Total']

# Winner announcement
print(f"The lucky winner is {winner}. Thier ticket worth ${total_won:.2f} is free!")
