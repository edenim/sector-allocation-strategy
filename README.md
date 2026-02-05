# Sector Allocation Strategy under Changing Interest Rates

## Project Overview
This project analyzes how changes in interest rates affect sector-level stock performance.
The goal is to provide a consulting-style recommendation on sector allocation strategies
under different interest rate environments.

## Business Question
In different interest rate environments, which equity sectors should be overweighted
or underweighted to optimize risk-adjusted returns?

## Hypotheses
H1. Interest rate changes affect sector performance asymmetrically; not all sectors respond
to interest rate movements in the same way.

H2. During rising interest rate environments, Financials and Energy sectors outperform
the overall market.

H3. During declining interest rate environments, Technology-oriented sectors outperform
other sectors.

H4. Sectors that are more sensitive to interest rate changes exhibit higher volatility,
indicating the need for risk-adjusted allocation strategies.

## Data Sources

This project uses publicly available financial and macroeconomic data to ensure
reproducibility and transparency.

- **Interest Rate Data**: Federal Funds Rate (monthly), sourced from the Federal Reserve Economic Data (FRED).
- **Equity Sector Data**: S&P 500 sector-level ETF prices (e.g., XLK, XLF, XLE, etc.).
- **Market Benchmark**: S&P 500 Index (used for relative performance comparison).

## Data Design & Assumptions

- The analysis is conducted using **monthly data** to align interest rate movements
  with sector-level stock performance.
- The study period spans from **2005 to the most recent available data**, capturing
  multiple interest rate cycles.
- Interest rate environments are classified as:
  - **Rising**: Federal Funds Rate increased compared to the previous month.
  - **Falling**: Federal Funds Rate decreased compared to the previous month.
  - **Stable**: No change in the interest rate.
- Sector performance is measured using **ETF total return proxies**, assuming dividends
  are reinvested.

## Preliminary Findings (H1)

The analysis confirms that sector performance varies meaningfully across interest rate regimes.
Technology stocks perform strongest during stable rate environments, while Energy and defensive
sectors show relatively stronger performance during declining rate periods. These results
suggest that sector allocation strategies should be adapted to the prevailing interest rate
regime rather than applied uniformly.

