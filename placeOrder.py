import pandas as pd
import json
import datetime

from breeze_connect import BreezeConnect

breeze = BreezeConnect(api_key="")
breeze.generate_session(api_secret="", session_token="")

iso_date_string = datetime.datetime.strptime("21/03/2022","%d/%m/%Y").isoformat()[:10] + 'T05:30:00.000Z'
iso_date_time_string = datetime.datetime.strptime("21/03/2022 23:59:59","%d/%m/%Y %H:%M:%S").isoformat()[:19] + '.000Z'

breeze.place_order(stock_code="TCS",
                    exchange_code="NFO",
                    product="futures",
                    action="buy",
                    order_type="limit",
                    stoploss="0",
                    quantity="3200",
                    price="3200",
                    validity="day",
                    validity_date="2022-07-08T07:00:00.000Z",
                    disclosed_quantity="0",
                    expiry_date="2022-07-15T06:00:00.000Z",
                    right="others",
                    strike_price="0",
                    user_remark="TestOrder")
