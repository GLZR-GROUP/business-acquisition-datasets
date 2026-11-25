# Hedge Funds vs Private Equity Funds, Form ADV

**14,907 hedge funds and 42,763 private equity funds compared**

For the 14,907 hedge funds and 42,763 private equity funds that investment advisers reported in their latest Form ADV filings with the SEC, from 1 November 2025 to 31 October 2026: counts and gross assets; medians and bands of fund size, minimum investment and beneficial owners; the Investment Company Act exclusion relied on; master, feeder and fund-of-funds structures; where the funds are organized; ownership by non-U.S. persons; audits, prime brokers, custodians, administrators, outside valuation and marketers, compiled by GLZR Group.

## Source
U.S. Securities and Exchange Commission, Form ADV data (monthly filing data, 1 November 2025 to 31 October 2026) and the lists of registered investment advisers and exempt reporting advisers of 2 November 2026.
- https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers
- https://adviserinfo.sec.gov/adv

## Coverage
Period: 2025-11-01/2026-10-31.

## License and credit
The source data are works of the U.S. federal government (the U.S. Securities and Exchange Commission) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Securities and Exchange Commission, Form ADV data (monthly filing data, 1 November 2025 to 31 October 2026) and the lists of registered investment advisers and exempt reporting advisers of 2 November 2026; compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/hedge-fund-vs-private-equity/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-hedge-funds-vs-private-equity-funds-form-adv-2026.csv](glzr-hedge-funds-vs-private-equity-funds-form-adv-2026.csv)

- `glzr-hedge-funds-vs-private-equity-funds-form-adv-2026.csv`: Hedge funds and private equity funds on Form ADV, compared, 2025 to 2026 (49 rows, 8 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `table` | string | The part of the comparison: Size, Investors, Structure, Service providers, a Spread table or Organized in. |
| `measure` | string | What the row counts or measures. |
| `form_adv_question` | string | The question of Form ADV, Schedule D, Section 7.B.(1) the figures come from. |
| `hedge_funds` | numeric | Value for the private funds reported as hedge funds, in the row's unit. |
| `private_equity_funds` | numeric | Value for the private funds reported as private equity funds, in the row's unit. |
| `unit` | string | Unit of the two values: funds, advisers, USD, beneficial owners, percent of funds, or percent weighted by gross assets. |
| `hedge_funds_base` | numeric | What the hedge fund value is out of: the number of funds, or gross assets in USD for the weighted row; blank when the value is not a share. |
| `private_equity_funds_base` | numeric | What the private equity value is out of: the number of funds, or gross assets in USD for the weighted row; blank when the value is not a share. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/hedge-funds-vs-private-equity-funds-form-adv", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/hedge-funds-vs-private-equity-funds-form-adv
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/hedge-funds-vs-private-equity-funds-form-adv
- Method, definitions and the latest version: https://glzrgroup.com/hedge-fund-vs-private-equity/
