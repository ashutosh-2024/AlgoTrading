# AlgoTrading

1. This repository contains codes for fetching historical stock market data for Cash Market and F&O segment using Breeze Connect API. <br/>
2. It also contains codes for backtesting trading strategies using backtrader library in python.<br/>
3. The repository contains codes for automatically placing orders with the broker and exiting the positions according to the defined strategy. <br/>


# Setup virtual environment
You must install the virtualenv package via pip
```
pip install virtualenv
```

You should create breeze virtual environment via virtualenv
```
virtualenv -p python3 breeze_venv
```

And then, You can activate virtual environment via source
```
source breeze_venv/bin/activate
```

Installing the client
```
pip install --upgrade breeze-connect
```

Or, You can also install the specific release version via pip
```
pip install breeze-connect==1.0.13
```
