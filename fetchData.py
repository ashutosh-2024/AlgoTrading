import pandas as pd
import json

from breeze_connect import BreezeConnect
breeze = BreezeConnect(api_key="")
breeze.generate_session(api_secret="", session_token="")

import datetime
iso_date_string = datetime.datetime.strptime("21/03/2022","%d/%m/%Y").isoformat()[:10] + 'T05:30:00.000Z'
iso_date_time_string = datetime.datetime.strptime("21/03/2022 23:59:59","%d/%m/%Y %H:%M:%S").isoformat()[:19] + '.000Z'

historicalData = breeze.get_historical_data(interval="30minute",
                            from_date= "2018-01-01T07:00:00.000Z",
                            to_date= "2022-07-07T07:00:00.000Z",
                            stock_code="TCS",
                            exchange_code="NSE",
                            product_type="Cash",
                            expiry_date="",
                            right="",
                            strike_price="")

with open('/Users/ashutoshaswani/Desktop/TcsCashMarket.json', 'w') as json_file:
    json.dump(historicalData['Success'], json_file)
    
df = pd.read_json (r'/Users/ashutoshaswani/Desktop/TcsCashMarket.json')
df.to_csv (r'/Users/ashutoshaswani/Desktop/TcsCashMarket.csv', index = None)
