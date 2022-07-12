# AlgoTrading

[![Downloads](https://pepy.tech/badge/algoashutosh)](https://pepy.tech/project/algoashutosh)

1. This repository contains codes for **fetching historical stock market data** for Cash Market and F&O segment using Breeze Connect API. <br/><br/>
2. It also contains codes for **backtesting pre defined option strategies**, and this code has also been **published as a PyPI library** at https://pypi.org/project/AlgoAshutosh/0.0.1/#description<br/><br/>
3. The repository contains codes for **automatically placing orders with the broker** according to the defined strategy. <br/><br/>


# Setup virtual environment<br/>

**1. Setup virtual environment for fetching historical stock market data / placing orders with broker :-<br/>**
<br>

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
  <br>
  
  **2. Setup virtual environment for backtesting option strategies on historical stock market data :-<br/>**
  <br>
  Starting by creating a virtual environment in conda by the name vnv
  ```
  conda create --name vnv
  ```
  
  Switching to the above created virtual environment
  ```
  source activate vnv
  ```
  
  Installing jupyter notebook to work on it
  ```
  conda install jupyter
  ```
  
  Installing the AlgoAshutosh library from PyPI to work on it and backtest option strategies.
  ```
  pip install AlgoAshutosh
  ```
  
  # Running a backtesting strategy example:<br>
  
  Opening up jupyter notebook
  
  ```
  jupyter-notebook
  ```
  The code : 
  ```
  from AlgoAshutosh import *
  object = ironCondor() 
  object.ironCondorStrategy(<location of put file>,<location of call file>,<location of futures file>,100,100,200,200,1,10,50)
  ```
  
  Sample output be something like this : <br>
  
  <img width="1148" alt="Screenshot 2022-07-12 at 12 01 07 PM" src="https://user-images.githubusercontent.com/78266562/178423814-3db70f65-5a15-48a2-827f-f7e4f1bb50dd.png">

  
