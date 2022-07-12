import pandas as pd
import json
import datetime

from breeze_connect import BreezeConnect

breeze = BreezeConnect(api_key="")
breeze.generate_session(api_secret="", session_token="")

iso_date_string = datetime.datetime.strptime("21/03/2022","%d/%m/%Y").isoformat()[:10] + 'T05:30:00.000Z'
iso_date_time_string = datetime.datetime.strptime("21/03/2022 23:59:59","%d/%m/%Y %H:%M:%S").isoformat()[:19] + '.000Z'

# spot price at 12:42 pm on 12th July is at 16101.20
# placing order for 15900 - 16300 short strangle on 12th July 2022.

breeze.place_order(stock_code="NIFTY",
                    exchange_code="NFO",
                    product="options",
                    action="sell",
                    order_type="limit",
                    stoploss="50",
                    quantity="50",
                    price="36",
                    validity="day",
                    validity_date="2022-07-12T07:00:00.000Z",
                    disclosed_quantity="50",
                    expiry_date="2022-07-15T06:00:00.000Z",
                    right="put",
                    strike_price="15900",
                    user_remark="TestOrder")

breeze.place_order(stock_code="NIFTY",
                    exchange_code="NFO",
                    product="options",
                    action="sell",
                    order_type="limit",
                    stoploss=40",
                    quantity="50",
                    price="27.25",
                    validity="day",
                    validity_date="2022-07-12T07:00:00.000Z",
                    disclosed_quantity="50",
                    expiry_date="2022-07-15T06:00:00.000Z",
                    right="call",
                    strike_price="16300",
                    user_remark="TestOrder")
