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

## Findings on Rising Rate Environments (H2)

H2 hypothesized that Financials and Energy sectors would outperform the broader market
during rising interest rate environments.

However, the empirical results indicate that this relationship is not consistent.
While Financials and Energy perform adequately in certain periods, they do not
systematically dominate sector returns during rate hikes. In several instances,
Technology and defensive sectors exhibit comparable or superior performance.

These findings suggest that rising interest rates alone are insufficient to explain
sector-level outperformance, and that broader macroeconomic and earnings-related factors
play a critical role during tightening cycles.

## Findings on Falling Rate Environments (H3)

H3 proposed that Technology-oriented sectors would outperform during declining
interest rate environments, reflecting improved growth expectations and lower
discount rates.

The analysis shows that Technology does not uniformly lead sector performance
during falling rate periods. Instead, sectors such as Energy and Health Care often
demonstrate strong returns, indicating that rate cuts frequently coincide with
broader economic transitions rather than directly benefiting growth-oriented sectors.

This suggests that declining interest rates should be interpreted in a broader
macroeconomic context when forming sector allocation strategies.

## Strategic Implications

The findings suggest that sector allocation strategies should not rely solely on the
direction of interest rate movements. While interest rates influence market conditions,
sector-level performance is shaped by a combination of macroeconomic dynamics, earnings
expectations, and regime-specific factors.

A regime-based approach to sector allocation—adjusting exposure based on broader
interest rate environments rather than fixed assumptions—can provide more flexibility
than static sector positioning. In particular, Technology and defensive sectors may
remain competitive even during tightening cycles, while traditional rate-sensitive
sectors do not consistently dominate returns.

These results highlight the importance of adaptive, data-driven allocation frameworks
when forming investment or strategic recommendations.

## Risk-Adjusted Performance (H4)

Evaluating sector strategies based solely on returns can be misleading.
Incorporating volatility and risk-adjusted metrics such as the Sharpe ratio
provides a more comprehensive assessment of strategy effectiveness. The
risk-adjusted analysis reinforces the need to balance performance with
consistency when comparing allocation strategies.

## Limitations and Future Work

This analysis focuses on sector-level ETF proxies and monthly data, which may
mask intra-month dynamics and stock-specific effects. Future research could
extend the framework by incorporating firm-level data, alternative macroeconomic
indicators, or international market comparisons.

## Project Structure

- `python`: Data collection, analysis, and strategy simulation
- `r`: Statistical validation 
