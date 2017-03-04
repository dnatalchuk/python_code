#!/usr/bin/python

pocket = 11.5
tshirt = 13.99
sale = 0.2

disc = tshirt * sale
new_price = tshirt - disc
score = pocket - new_price
print round(score,2)
