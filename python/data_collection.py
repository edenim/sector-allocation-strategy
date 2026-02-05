import pandas as pd
from fredapi import Fred

FRED_API_KEY = "e95f83e8329556b55ad3e1902f15cef7"

fred = Fred(api_key=FRED_API_KEY)

# Federal Funds Rate (monthly)
rate = fred.get_series("FEDFUNDS")
rate = rate.to_frame(name="rate")
rate.index.name = "date"
rate = rate.reset_index()

# rate change + regime
rate["rate_change"] = rate["rate"].diff()
rate["rate_regime"] = rate["rate_change"].apply(
    lambda x: "Rising" if x > 0 else ("Falling" if x < 0 else "Stable")
)

print(rate.head(10))

import yfinance as yf

sector_etfs = {
    "Technology": "XLK",
    "Financials": "XLF",
    "Energy": "XLE",
    "Health Care": "XLV",
    "Consumer Discretionary": "XLY",
    "Industrials": "XLI",
    "Consumer Staples": "XLP",
    "Utilities": "XLU"
}

prices = []

for sector, ticker in sector_etfs.items():
    df = yf.download(ticker, start="2005-01-01", interval="1mo", progress=False)

    # MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)

    price_col = "Adj Close" if "Adj Close" in df.columns else "Close"
    df = df[[price_col]].rename(columns={price_col: "price"})

    df["sector"] = sector
    df["etf_ticker"] = ticker
    prices.append(df)

sector_prices = pd.concat(prices).reset_index().rename(columns={"Date": "date"})

sector_prices["monthly_return"] = (
    sector_prices.groupby("sector")["price"].pct_change()
)

print(sector_prices.head(10))

rate_subset = rate[["date", "rate_regime"]]

analysis_df = pd.merge(
    sector_prices,
    rate_subset,
    on="date",
    how="inner"
)

print(analysis_df.head())

h1_result = (
    analysis_df
    .dropna(subset=["monthly_return"])
    .groupby(["rate_regime", "sector"])["monthly_return"]
    .mean()
    .reset_index()
)

h1_pivot = h1_result.pivot(
    index="sector",
    columns="rate_regime",
    values="monthly_return"
)

print(h1_pivot)

import matplotlib.pyplot as plt

h1_pivot.plot(kind="bar", figsize=(10, 6))
plt.title("Average Monthly Sector Returns by Interest Rate Regime")
plt.ylabel("Average Monthly Return")
plt.axhline(0, linewidth=0.8)
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Select top 2 sectors for each interest rate regime
top2_by_regime = {}
for regime in ["Rising", "Falling", "Stable"]:
    top2 = (
        h1_pivot[regime]
        .sort_values(ascending=False)
        .head(2)
        .index
        .tolist()
    )
    top2_by_regime[regime] = top2

print("Top sectors by regime:")
print(top2_by_regime)


# Prepare clean dataset
analysis_df_clean = analysis_df.dropna(subset=["monthly_return"]).copy()


# Compute monthly strategy return based on regime-specific sector allocation
def strategy_return_for_month(group):
    regime = group["rate_regime"].iloc[0]
    selected_sectors = top2_by_regime.get(regime, [])

    if len(selected_sectors) == 0:
        return np.nan

    return group[group["sector"].isin(selected_sectors)]["monthly_return"].mean()


# Strategy monthly returns
strategy_monthly = (
    analysis_df_clean
    .groupby("date", as_index=False)
    .apply(strategy_return_for_month, include_groups=False)
    .rename(columns={None: "strategy_return"})
)


# Equal-weight sector benchmark
benchmark_monthly = (
    analysis_df_clean
    .groupby("date")["monthly_return"]
    .mean()
    .reset_index()
    .rename(columns={"monthly_return": "equal_weight_benchmark"})
)


# Merge performance data and compute cumulative returns
perf = (
    pd.merge(strategy_monthly, benchmark_monthly, on="date", how="inner")
    .dropna()
)

perf["strategy_cum"] = (1 + perf["strategy_return"]).cumprod()
perf["benchmark_cum"] = (1 + perf["equal_weight_benchmark"]).cumprod()

print(perf.head())


# Plot cumulative performance
perf.set_index("date")[["strategy_cum", "benchmark_cum"]].plot(figsize=(10, 6))
plt.title("Regime-Based Sector Rotation Strategy vs Equal-Weight Benchmark")
plt.ylabel("Cumulative Growth of $1")
plt.tight_layout()
plt.show()

# ---- Risk Metrics (H4) ----

# Monthly volatility
strategy_vol = perf["strategy_return"].std()
benchmark_vol = perf["equal_weight_benchmark"].std()

# Sharpe ratio (risk-free rate assumed to be 0 for simplicity)
strategy_sharpe = perf["strategy_return"].mean() / strategy_vol
benchmark_sharpe = perf["equal_weight_benchmark"].mean() / benchmark_vol

print("\n=== Risk Metrics ===")
print(f"Strategy Volatility (monthly): {strategy_vol:.4f}")
print(f"Benchmark Volatility (monthly): {benchmark_vol:.4f}")
print(f"Strategy Sharpe Ratio: {strategy_sharpe:.2f}")
print(f"Benchmark Sharpe Ratio: {benchmark_sharpe:.2f}")
