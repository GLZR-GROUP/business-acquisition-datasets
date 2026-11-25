# Valuation Multiples by Country, 2026

**Country-adjusted SDE and EBITDA multiples for 102 countries (estimates)**

GLZR Group estimates of SDE and EBITDA multiples by enterprise-value band for 102 countries in the Americas, Europe, the Middle East, Africa, Asia and Oceania, derived by applying Damodaran's January 2026 rating-based country risk premiums to the IBBA and M&A Source Market Pulse Q2 2026 U.S. multiples with a capitalization-rate build-up. Estimates, not observed deal prices.

## Source
GLZR Group, derived from IBBA and M&A Source Market Pulse Q2 2026 and Damodaran (January 2026).
- https://www.ibba.org/wp-content/uploads/2026/08/mp-highlights-q2-2026.pdf
- https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html

## Coverage
Period: 2026-04-01/2026-06-30.
Places: 102 countries (the list is in the file).

## License and credit
GLZR Group's estimates are licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Credit: GLZR Group, derived from IBBA and M&A Source Market Pulse Q2 2026 and Damodaran (January 2026). The inputs they are derived from are the sources' own and are cited, not relicensed. Estimates, not observed deal prices.

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/valuation-multiples/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-country-adjusted-multiples-2026-10.csv](glzr-country-adjusted-multiples-2026-10.csv)

- `glzr-country-adjusted-multiples-2026-10.csv`: Country-adjusted small business valuation multiples, 2026 (102 countries) (102 rows, 12 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `country` | string | Country name. |
| `iso` | string | ISO 3166-1 alpha-2 country code. |
| `currency` | string | ISO 4217 code of the country's currency. |
| `moodys_rating` | string | Moody's sovereign rating behind the rating-based country risk premium. |
| `country_risk_premium` | numeric | Damodaran's country risk premium, January 2026 update (rating-based), as a decimal: 0.0023 = 0.23%. |
| `crp_in_excess_of_us` | numeric | The country's premium minus the U.S. premium, floored at 0, as a decimal. |
| `adjusted_multiple_lt500k` | numeric | GLZR Group's country-adjusted multiple of SDE (seller's discretionary earnings), purchase price under $500K. An estimate, not an observed deal price. |
| `adjusted_multiple_500k_1m` | numeric | Country-adjusted SDE multiple, purchase price $500K to $1M. An estimate, not an observed deal price. |
| `adjusted_multiple_1m_2m` | numeric | Country-adjusted SDE multiple, purchase price $1M to $2M. An estimate, not an observed deal price. |
| `adjusted_multiple_2m_5m` | numeric | Country-adjusted EBITDA multiple, purchase price $2M to $5M. An estimate, not an observed deal price. |
| `adjusted_multiple_5m_50m` | numeric | Country-adjusted EBITDA multiple, purchase price $5M to $50M. An estimate, not an observed deal price. |
| `method` | string | How the multiple is derived: 1 / (1 / U.S. multiple + the premium in excess of the U.S.), with Damodaran's January 2026 premiums and the IBBA Q2 2026 U.S. multiples as the base. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/valuation-multiples-by-country-2026", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/valuation-multiples-by-country-2026
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/valuation-multiples-by-country-2026
- Method, definitions and the latest version: https://glzrgroup.com/valuation-multiples/
