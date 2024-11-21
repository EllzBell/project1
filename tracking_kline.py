import requests
import pandas as pd
import datetime

kuc_url = r"https://api.kucoin.com/api/v1/"




def kuc_collect_kline(coin_pair, interval, start_at, end_at):
    """
    This method is used to collect a single kline from kucoin.
    Args:
        coin_pair (str): a coin pair in the style of BTC-USDT or similar
        interval_unit (str): this is the unit of time used for the kline, acceptable are min, hour, day, week, month 
        interval (str): this is the interval of the kline. Acceptable intervals are as follows: 
        1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week, 1month
        Results are: time open close high low volume turnover
    """
    
    kline_url = kuc_url + f"market/candles?type={interval}&symbol={coin_pair}&startAt={start_at}&endAt={end_at}"
    response = requests.request("GET", url=kline_url)
    response = response.json()
    if response['code'] == '200000':
        df = pd.DataFrame(response["data"], columns=["time", "open", "close", "high", "low", "volume", "turnover"])
    else:
        print("Error in kline retrieval")
    
    df = df.astype(float)
    return df

def kuc_collect_multi_kline(coin_pair, interval_unit, interval_int, rounds):
    
    """This is used to collect multiple past klines from kucoin.

    Args:
        coin_pair (str): a coin pair in the style of BTC-USDT or similar
        interval_unit (str): this is the unit of time used for the kline, acceptable are min, hour, day, week, month 
        interval_int (int): this is the amount of said unit, note that the combined acceptable interval_units and interval ints are as follows: 
        1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week, 1month
    """
    import time
    now = int(time.time())
    #first assume that the step change is for a minute interval
    #remember the step changes and other changes need to be in seconds
    step_change = 60 * interval_int
    if interval_unit == "hour":
        step_change = step_change * 60
    if interval_unit == "day":
        step_change = step_change * 60 * 24
    if interval_unit == "week":
        step_change = step_change * 60 * 24 * 7
    if interval_unit == "month":
        #Approximation of average month, February considerations are ignored
        step_change = step_change * 60 * 24 * 7 * 30
    step_change = int(step_change)
    interval = str(interval_int) + interval_unit
    past = int(now - step_change * 1000)
    first = True
    df = ""
    for r in range(rounds):
        if first:
            df = kuc_collect_kline(coin_pair, interval, start_at=past, end_at=now)
            first = False
        else:
            new_df = kuc_collect_kline(coin_pair, interval, start_at=past, end_at=now)
            df = pd.concat([df, new_df], axis=0).reset_index(drop=True)
        now = now - step_change * 1001
        past = now - step_change * 1000
    df = df.sort_values("time", ascending = True)
    return df

     
def change_to_datetime(kline):
    """This is used to change the time column to a datetime column and to set it as the index"""
    kline['time'] = kline['time'].apply(lambda d: datetime.datetime.fromtimestamp(d))
    kline = kline.set_index("time", drop=True)
    kline = kline.sort_index(ascending=True)
    return kline

if __name__ == "__main__":
    import datetime
    unit = "hour"
    unit_int = 1
    df = kuc_collect_multi_kline("ETH-USDT", unit, unit_int, 10)
    print(df.head(10))
    
    
    
    
    
    
    
    
    
    
    
