import dataclasses
import decimal


@dataclasses.dataclass
class PortfolioMetrics:
	portfolio_exposures_eur: dict[str, decimal.Decimal]
