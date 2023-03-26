import pandas as pd
import yfinance


def get_daily_candles_for_tickers(tickers: list[str], start_date: str, end_date: str) -> pd.DataFrame:
	daily_candles = pd.DataFrame(
		columns = [
			'Date',
			'Open',
			'High',
			'Low',
			'Close',
			'Adj Close',
			'Volume',
			'Ticker',
			'Close_to_close_price_return_bps',
		]
	)
	for ticker in tickers:
		ticker_daily_info = yfinance.download(
			tickers = ticker,
			start = start_date,
			end = end_date,
			group_by = 'ticker',
		)
		ticker_daily_info.reset_index(inplace = True)
		ticker_daily_info['Ticker'] = ticker
		ticker_daily_info['Close_to_close_price_return_bps'] = (
			(ticker_daily_info['Adj Close'] - ticker_daily_info['Adj Close'].shift())
			/ ticker_daily_info['Adj Close'].shift()
			* 10_000
		)
		daily_candles = pd.concat([daily_candles, ticker_daily_info], ignore_index = True)
	return daily_candles
