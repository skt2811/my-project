import math

# Implements the binomial option pricing model to price a European call option on a stock
# S - stock price today
# K - strike price of the option
# T - time until expiry of the option
# r - risk-free interest rate
# vol - the volatility of the stock
# N - number of steps in the model

def binomial_call(S, K, T, r, vol, N):
    dt = T / N
    u = math.exp(vol * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)
    C = {}

    for m in range(0, N + 1):
        C[(N, m)] = max(S * (u ** (2 * m - N)) - K, 0)

    for k in range(N - 1, -1, -1):
        for m in range(0, k + 1):
            C[(k, m)] = math.exp(-r * dt) * (p * C[(k + 1, m + 1)] + (1 - p) * C[(k + 1, m)])

    return C[(0, 0)]

for N in [1, 2, 10, 100, 200, 300, 400, 500]:
    print("With {:3d} steps, the price is {:.2f}".format(N, binomial_call(100, 100, 1, 0, math.log(1.2), N)))
