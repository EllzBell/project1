# Bitcoin or Bit by Coin
>First project for Rutgers AI Bootcamp
## Purpose
> As Bitcoin reaches a historical high of ~$90,000 [^1], the average informal investor may want to consider different strategies to trade bitcoin. The files provided aid in this goal. 

## Methodology
> In the tracking_kline python file, requests are made to kucoin api [^2] using python's request library. Kucoin's api will return a kline of maximum size around 1000 and so in order to get an older range of kline day, segments are called and appended.

> kuc_collect_kline performs the collection of a single kline when given an appropirate interval and start_at and end_at times, both of which are the seconds since the epoch.
> ex: kuc_collect_kline("BTC-USDT", "1hour", 1696122000, 1696122000) would return a kline with columns time, open, close, high, low, volume, and turnover columns.
> kuc_collect_multi_kline performs the collection of multiple klines starting from the current time and going back a user selected number of times to generate a longer kline. 
> ex: kuc_collect_multi_kline("BTC-USDT", "hour", 1, 10) results in a kline that is ~10,000 entries starting from the current time to ~10,000 hours ago.
> to make data analysis easier using the pandas library [^3], another method change_to_datetime is provided which reads in the kline

> In the project1.ipynb file, analysis of the bitcoin kline data are peformed to determine whether certain short term strategies can be employed to  

[^1]:[Bitcoin Makes New All-Time High of $94,000...](https://www.coindesk.com/markets/2024/11/19/bitcoin-makes-new-all-time-high-of-93500-as-etf-options-go-live/)
[^2]:https://www.kucoin.com/api
[^3]: https://pandas.pydata.org/docs/
