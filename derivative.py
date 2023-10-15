import math

# Implements the binomial option pricing model to price a European call option on a stock
# stock_price - stock price today
# strike_price - strike price of the option
# time_to_expiry - time until expiry of the option
# interest_rate - risk-free interest rate
# volatility - the volatility of the stock
# steps - number of steps in the model

def custom_binomial_call(stock_price, strike_price, time_to_expiry, interest_rate, volatility, steps):
    dt = time_to_expiry / steps
    u = math.exp(volatility * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(interest_rate * dt) - d) / (u - d)
    option_price = {}

    for m in range(0, steps + 1):
        option_price[(steps, m)] = max(stock_price * (u ** (2 * m - steps)) - strike_price, 0)

    for k in range(steps - 1, -1, -1):
        for m in range(0, k + 1):
            option_price[(k, m)] = math.exp(-interest_rate * dt) * (p * option_price[(k + 1, m + 1)] + (1 - p) * option_price[(k + 1, m)])

    return option_price[(0, 0)]

for steps in [1, 2, 10, 100, 200, 300, 400, 500]:
    print("With {:3d} steps, the price is {:.2f}".format(steps, custom_binomial_call(100, 100, 1, 0, math.log(1.2), steps)))
