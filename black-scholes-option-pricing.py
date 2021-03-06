""" Black-Scholes Options Pricing """

"""
Author: Matteo Bottacini, matteo.bottacini@usi.ch
last update: March 6, 2021
"""

# import modules
import math
from scipy.stats import norm

# main variables
asset_price = 100
asset_volatility = .3
strike_price = 100
time_to_expiration = 1
risk_free_rate = .01

# European Call -- BS Model
class EuropeanCall:

    def call_price(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z1 = z1 * asset_price
        x2 = math.log(asset_price / (b * strike_price)) - .5 * (asset_volatility * asset_volatility) * time_to_expiration
        x2 = x2 / (asset_volatility * (time_to_expiration ** .5))
        z2 = norm.cdf(x2)
        z2 = b * strike_price * z2
        return z1 - z2

    def __init__(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.call_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)

# European Put -- BS Model
class EuropeanPut:

    def put_price(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log((b * strike_price) / asset_price) + .5 * (asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z1 = b * strike_price * z1
        x2 = math.log((b * strike_price) / asset_price) - .5 * (asset_volatility * asset_volatility) * time_to_expiration
        x2 = x2 / (asset_volatility * (time_to_expiration ** .5))
        z2 = norm.cdf(x2)
        z2 = asset_price * z2
        return z1 - z2

    def __init__(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.put_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)

# results
ec = EuropeanCall(asset_price=asset_price,
                  asset_volatility=asset_volatility,
                  strike_price=strike_price,
                  time_to_expiration=time_to_expiration,
                  risk_free_rate=risk_free_rate)
print("European call price is: " + str(ec.price))

ep = EuropeanPut(asset_price=asset_price,
                 asset_volatility=asset_volatility,
                 strike_price=strike_price,
                 time_to_expiration=time_to_expiration,
                 risk_free_rate=risk_free_rate)
print("European put price is: " + str(ep.price))
