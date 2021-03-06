# Black-Scholes European Option Pricing

#### Last Update March 6, 2021 ####
#### Matteo Bottacini, [matteo.bottacini@usi.ch](mailto:matteo.bottacini@usi.ch) ####


# Project description

In this project it is discussed how to price European Call and Put options following the Black and Scholes model.

# Content
* Main variables that you can change
* Call option
* Put option  
* Conclusion

# Main variables that you can change
Feel free to play with these variables and create different settings.

```python
# main variables

asset_price        = 100
asset_volatility   = .3
strike_price       = 100
time_to_expiration = 1
risk_free_rate     = .01
```

# Call Options
The Black and Scholes formula for the Call European Options is the following:
![equation](https://miro.medium.com/max/1400/1*F592QEjBwJgnUlcWXAHd4A.png)
where:
- St     : Stock price at time t 
- X      : Strike price of the option
- σ      : Volatility term
- Φ      : Cumulative normal distribution function
- B(t,T) : Continuous discount factor
- T      : Time until maturity
- t      : Current point in time

```python
import math
from scipy.stats import norm

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
```

# Put Options
The Black and Scholes formula for the Put European Options is the following:
![equation]()

where:
- St     : Stock price at time t 
- X      : Strike price of the option
- σ      : Volatility term
- Φ      : Cumulative normal distribution function
- B(t,T) : Continuous discount factor
- T      : Time until maturity
- t      : Current point in time

```python
import math
from scipy.stats import norm

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
```

# Conclusion
In the last section are shown the results.
```python
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
```