# Bitcoin or Bit by Coin
>First project for Rutgers AI Bootcamp
## Purpose
> As Bitcoin reaches a historical high of ~$90,000 [^1], the average informal investor may want to consider different strategies to trade bitcoin. The files provided aid in this goal. 
## Installation
> pip install pandas
> pip install prophet
> pip install seaborn
> Otherwise download the files making sure that tracking_kline.py is in the same folder and run project1.ipynb or HLVResults.ipynb
## Methodology and Results
> In the tracking_kline python file, requests are made to kucoin api [^2] using python's request library. Kucoin's api will return a kline of maximum size around 1000 and so in order to get an older range of kline day, segments are called and appended.

> kuc_collect_kline performs the collection of a single kline when given an appropirate interval and start_at and end_at times, both of which are the seconds since the epoch.
> ex: kuc_collect_kline("BTC-USDT", "1hour", 1696122000, 1696122000) would return a kline with columns time, open, close, high, low, volume, and turnover columns.
> kuc_collect_multi_kline performs the collection of multiple klines starting from the current time and going back a user selected number of times to generate a longer kline. 
> ex: kuc_collect_multi_kline("BTC-USDT", "hour", 1, 10) results in a kline that is ~10,000 entries starting from the current time to ~10,000 hours ago.
> to make data analysis easier using the pandas library [^3], another method change_to_datetime is provided which reads in the kline

> In the project1.ipynb file, analysis of the bitcoin kline data are peformed to determine whether certain simple strategies can be used to buy when bitcoin is low and sell when bit coin is high. The HLVResults.ipynb are part of a cursory look into whether there are any specific trends along the high and low price points. The closing and opening prices are focused on for analysis as they are the most likely prices to be achieved by the trader (as it is the last price recorded for an interval or the first for the next interval).
>
> The analysis performed are as follows:
> Correlations of volume changes and price changes
> Correlations of time spans and price changes
> Simulated strategy
> Time series fitting 
>
## Correlations of Volume Changes and Price Changes
> Using pandas libraries first determine the percent change for a twenty four hour basis.
> Then create a kline that holds only the columns with the percent changes. Using seaborn's heatmap function, create a heatmap of said kline's correlations as performed by pandas' correlation function. For a visual check, graph the change in volume with the change in price.
> Resulting graphs:
> > Heatmap:
> > 
> > ![image](https://github.com/user-attachments/assets/3333a93d-9480-4926-9021-c9d7a1658db8)
> > 
> > Percent Change of Open Price and Change in Volume:
> > 
> > ![image](https://github.com/user-attachments/assets/b452116b-7d7e-450d-a30c-fe08d15c8f6e)
> > 
> > Percent Change of Close Price and Change in Volume:
> > 
> > ![image](https://github.com/user-attachments/assets/5c325e39-75be-405f-939d-c63337cf1d44)
> > 
> As seen above, there isn't a strong correlation between the percent change of volume and the percent changes of each price point, however there seems to be a slight correlation between the magnitude of the change of price and the change in volume which is confirmed by the graph below. However, as a change in volume does not differentiate between positive or negative changes in price, a strategy based on change in volume alone is not ideal.
> 
> > ![image](https://github.com/user-attachments/assets/d34781d4-ad66-4857-bb51-1967b030bc02)

## Correlations of Time Spans and Price Changes
> Using pandas groupby and datetime monthly, hourly, and daily frequences as parameters by which to groupby, medians, means, maxes, and minimums of the percent changes of the prices are aggregated by each groupby index. As close price and open price show negligable trend differences, only the graphs for the close price are displayed below.
> 
> Monthly Mean and Median:
> 
> ![image](https://github.com/user-attachments/assets/87b410b0-bdc2-4e52-8fdf-c1884a05c1c9)
> 
> Monthly Min and Max:
> 
> ![image](https://github.com/user-attachments/assets/50791a50-72e7-4134-928d-4fb3c788e020)
> 
> Day of Week Mean and Median:
> 
> ![image](https://github.com/user-attachments/assets/f53c4d7f-ab07-44c7-85a3-20e9391e169b)
> 
> Day of Week Max and Min:
> 
> ![image](https://github.com/user-attachments/assets/11d21b99-3782-4bff-b37f-3c8eec7afa14)
> 
> Combined Monthly and Day of Week Mean and Median:
> 
> ![image](https://github.com/user-attachments/assets/0d5c887a-30e7-4dd0-bf08-4f1bdd89fa4a)
> 
> Combined Monthly and Day of Week Min and Max:
> 
> ![image](https://github.com/user-attachments/assets/d1d64d4c-96d0-4d9c-a0f9-0ed99cb05390)
> 
> Hour of Day Mean and Median:
> 
> ![image](https://github.com/user-attachments/assets/050771da-a55d-45d0-81a7-8305390a0d50)
> 
> Hour of Day Min and Max:
> 
> ![image](https://github.com/user-attachments/assets/7bf7e445-aa11-431d-8613-2c87b9c2f745)
> 
> Combined Week and Hour of Day Mean and Median:
> 
> ![image](https://github.com/user-attachments/assets/3d878eed-d71a-435b-83a2-a55500f18ea7)
> 
> Combined Week and Hour of Day Max and Min:
> 
> ![image](https://github.com/user-attachments/assets/14602e8c-ebb4-4a45-a7c5-ddc8cbe3b930)
>
> 
## Strategy Based on Above Graphs:
> Buying locations are based on relative decreases in precent change that then shift to increases while selling locations are based on relative increases in percent change that then shift to decreases. The dollar amounts and coin amounts are tracked for each transaction along with the dollar equivalent of the coin amount. There is an assumed cost to each transaction which is 0.005 times the dollar or coin amount. Buys in each trade deplete the dollar amount to convert to the coin amount while sells deplete the coin amount to convert into the dollar amount.The percent change in the buy price and sell price are tracked by holding onto the historical buy price. The resultant trends in dollar equivalent amounts, raw dollar amounts, and profit per trade are plotted. 
>   
> Month sales with buys in September and sells in April:
> 
>> Dollars:
>> 
>> ![image](https://github.com/user-attachments/assets/43030fe7-0dfd-499f-aabe-1806e14df6df)
>> 
>> Profits:
>> 
>> ![image](https://github.com/user-attachments/assets/04bfa6f0-c74b-487e-8812-8a00028d2995)
>> 
>> This strategy achieves a good increase but fails to beat the HODL strategy over the same time period which would result in ~$1900 of value by the end.
>>
>Week day sales with buys in Thursday and sells in Tuesdays:
> 
>> Dollars:
>> 
>> ![image](https://github.com/user-attachments/assets/2fa66234-eecf-463a-b425-ca19dfb62f5d)
>> 
>> Profits:
>> 
>> ![image](https://github.com/user-attachments/assets/3f5441ec-c598-48ba-9998-43d12f18c13a)
>> 
>> This strategy achieves a moderate increase but fails to beat the HODL strategy over the same time period which would result in ~$1900 of value by the end and fails to beat the Monthly sales strategy.
>> 
>Hour of day sales with buys at 10 pm and sells at 5am:
> 
>> Dollars:
>> 
>> ![image](https://github.com/user-attachments/assets/2fa17785-2b61-465f-9824-e2b90d1967e7)
>> 
>> Profits:
>> 
>> ![image](https://github.com/user-attachments/assets/bf07383d-f286-4bea-a060-7f398061c46d)
>> 
>> This strategy loses money over time.
>Combined Strategies fail to achieve any significant difference from whichever is the larger time frame compared (ex: combined Monthly with Day of Week follows the Monthly pattern)

## Prophet Modelling
> Prophet is a library that has prebuilt modules to easily fit time series data and observe trends as well as to make predictions. As Prophet[^4] models trends, the raw price data is fitted to Prophet parameters. For testing purposes a 720 hour future prediction is made.
> 
>> Close Price Fitting and Prediction
>> 
>> ![image](https://github.com/user-attachments/assets/48c3db27-d313-4ee0-96fc-fbdb159f9a7a)
>> 
>> As expected the fitting has difficulty especially where there are large frequent swings in price. The true values are frequently outside of the error. The prediction suggested by Prophet's time series fitting falls completely outside of the trend of Bitcoin's closing prices which suggests that other variables are required or that the closing prices are not fittable. 

# Conclusion
> The suggestions here are that rudementary strategies to trade Bitcoin on a short term basis fail to beat out a basic HODL strategy when following the same time span. Future consideration is required of other strategies, cryptocurrency pairs, and relationships between data to fully determine if there is no possible short term strategy that would beat out the long term HODL.

[^1]:[Bitcoin Makes New All-Time High of $94,000...](https://www.coindesk.com/markets/2024/11/19/bitcoin-makes-new-all-time-high-of-93500-as-etf-options-go-live/)
[^2]: https://www.kucoin.com/api
[^3]: https://pandas.pydata.org/docs/
[^4]: https://facebook.github.io/prophet/
