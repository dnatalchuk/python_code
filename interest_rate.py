#Program to calculate money on saving account with interest year in 5 years

amount = 1000 # amount of money on saving account
interest_rate = 0.05 # interest rate 5%
year = 1
period = 5

while year <= period:
	
	amount = amount * (1 + interest_rate)
	print amount
	year += 1

