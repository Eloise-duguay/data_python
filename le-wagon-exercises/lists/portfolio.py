# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [ 2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

fb_stocks_count = portfolio[3][0]
print (fb_stocks_count)

market = [ 198.84, 1217.93, 267.66, 179.06 ]

aapl_price_count = portfolio[0][0] * portfolio[0][1]
goog_price_count = portfolio[1][0] * portfolio[1][1]
tsla_price_count = portfolio[2][0] * portfolio[2][1]
fb_price_count = portfolio[3][0] * portfolio[3][1]

prices = [ aapl[1], goog[1], tsla[1], fb[1] ]

somme = 0
for n in range(0,4):
    somme += (market[n] - prices[n]) * portfolio[n][0]
    
print(somme)