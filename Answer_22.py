"""     You have 200 rupees.

You decide to buy a book for 60 rupees. How much do you have left?

Then, you receive 30 rupees from a friend. How much do you have now?

You decide to donate 10% of your current money to charity. How much do you have left?

You find 5 rupees in your pocket. Add this to your current amount.

You want to split the remaining amount equally between yourself and a friend. How much does each of you get?

You win a prize and the amount you have is tripled. How much do you have now?

Finally, you purchase a rose, usually the price of rose is 50 rupees but todaythe price is incremented by 10 rupees due to demand. How much do you pay now?"""


amount = 200   # Initial amount
print('Initial Amount:', amount)

amount -= 60   # Bought book for 60 rupees
print('Money left after buying books:', amount)

amount += 30   # Received 30 rupees from a friend
print('Money left after receiving 30 rupees from friend:', amount)

charity_amount = amount * 10/100
amount -= charity_amount     # Donated 10% of your current money to charity
print('Money left after 10% donation to charity:', amount)

amount += 5   # Found 5 rupees in pocket
print('Money left after 5 rupees found:', amount)

amount /= 2   # Split the remaining amount equally with a friend
print('Money left after splitting 50% with friend:', amount)

amount *= 3   # Amount tripled as you win a prize
print('Money gained after tripling from a prize :', amount)


rose_price = 50
rose_price += 10   # Rose of 50 increases by 10 rupees
print('rose price paid:', rose_price)
amount -= rose_price   # Price of Rose Deduced
print('Finally Money left:', amount)


# Answer:
"""Initial Amount: 200
Money left after buying books: 140
Money left after receiving 30 rupees from friend: 170
Money left after 10% donation to charity: 153.0
Money left after 5 rupees found: 158.0
Money left after splitting 50% with friend: 79.0
Money gained after tripling from a prize : 237.0
rose price paid: 60
Finally Money left: 177.0"""


