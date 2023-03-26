import decimal

from portfolio_risk_metrics import settings, calculation, data_types, download_data

if __name__ == '__main__':
	# TODO: fix currency rate
	portfolio_metrics = data_types.PortfolioMetrics(
		portfolio_exposures_eur = {'SPY': decimal.Decimal('1000'), 'MSFT': decimal.Decimal('3000')}
	)
	daily_trade_candles = download_data.get_daily_candles_for_tickers(
		tickers = list(portfolio_metrics.portfolio_exposures_eur.keys()),
		start_date = portfolio_risk_metrics.settings.static.START_DATE,
		end_date = portfolio_risk_metrics.settings.static.END_DATE,
	)
	calculation.value_at_risk()
