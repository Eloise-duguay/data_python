# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
portfolio = {
        
  "aapl": {
    "volume": 10,
    "strike": 154.12
  },
  "goog": {
    "volume": 2,
    "strike": 812.56
  },
  "tsla": {
    "volume": 12,
    "strike": 342.12
  },
  "fb": {
    "volume": 18,
    "strike": 209.0
  }
  
}
print(portfolio['tsla']['volume'])
print(portfolio['goog']['strike'])

market = {
  "aapl":  198.84,
  "goog": 1217.93,
  "tsla":  267.66,
  "fb":    179.06
}

list_brand = ['aapl','goog','tsla','fb']

somme = 0
for n in range(0,4):
    somme += ( market[list_brand[n]] - portfolio[list_brand[n]]["strike"] ) * portfolio[list_brand[n]]["volume"]
print(somme)