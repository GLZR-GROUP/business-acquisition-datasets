# Private Equity Firms on SEC Form ADV, 2026

**Advisers with a private equity fund, by the funds' gross assets**

For each of the 4,419 investment advisers whose latest Form ADV filing with the SEC, from 1 November 2025 to 31 October 2026, lists at least one private equity fund: its CRD number, names, main office, type of filer, the date of the filing, the number of private equity funds and their gross assets as reported in Schedule D, Section 7.B.(1), the part in funds of funds and in feeder funds, and its private funds of all types, compiled by GLZR Group.

## Source
U.S. Securities and Exchange Commission, Form ADV data (monthly filing data, 1 November 2025 to 31 October 2026) and the lists of registered investment advisers and exempt reporting advisers of 2 November 2026.
- https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers
- https://adviserinfo.sec.gov/adv

## Coverage
Period: 2025-11-01/2026-10-31.

## License and credit
The source data are works of the U.S. federal government (the U.S. Securities and Exchange Commission) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Securities and Exchange Commission, Form ADV data (monthly filing data, 1 November 2025 to 31 October 2026) and the lists of registered investment advisers and exempt reporting advisers of 2 November 2026; compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/private-equity-firms/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-private-equity-firms-sec-form-adv-2026.csv](glzr-private-equity-firms-sec-form-adv-2026.csv)

- `glzr-private-equity-firms-sec-form-adv-2026.csv`: Investment advisers with a private equity fund on Form ADV: private equity funds and their gross assets by adviser, 2025 to 2026 (4,419 rows, 19 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `rank` | numeric | Rank by the gross assets of the adviser's private equity funds, largest first. |
| `crd` | string | The adviser's CRD number, as on Form ADV. |
| `adviser` | string | The adviser's primary business name. |
| `legal_name` | string | The adviser's legal name. |
| `main_office_city` | string | City of the main office, from the SEC's lists of advisers; blank when the main office is a private residence. |
| `main_office_state` | string | Two-letter state code of a main office in the United States; blank outside it and for a private residence. |
| `main_office_country` | string | Country of the main office; blank for a private residence. |
| `main_office_private_residence` | string | Y when the adviser checked the Form ADV box saying its main office address is a private residence; the SEC's lists give no address for it. |
| `filer` | string | registered = registered with the SEC; exempt reporting = exempt reporting adviser. |
| `latest_filing_date` | string | Date of the adviser's latest Form ADV filing from 1 November 2025 to 31 October 2026. |
| `private_equity_funds` | numeric | Private funds the adviser reports as 'Private Equity Fund' in Form ADV, Schedule D, Section 7.B.(1). |
| `private_equity_gross_assets_usd` | numeric | Gross assets of those funds as reported at question 11, U.S. dollars. |
| `private_equity_funds_of_funds` | numeric | Of those funds, the number that answer yes to question 8(a) (funds of funds). |
| `private_equity_gross_assets_in_funds_of_funds_usd` | numeric | Gross assets of those funds of funds, U.S. dollars. |
| `mostly_funds_of_funds` | string | Y when funds answering yes to question 8(a) hold at least half of the adviser's private equity gross assets; otherwise N. |
| `private_equity_feeder_funds` | numeric | Of the private equity funds, the number reported as feeder funds in a master-feeder arrangement (question 6(c)). |
| `private_equity_gross_assets_in_feeder_funds_usd` | numeric | Gross assets of those feeder funds, U.S. dollars. |
| `private_funds_all_types` | numeric | All private funds the adviser reports, of every type. |
| `private_fund_gross_assets_all_types_usd` | numeric | Gross assets of all those private funds, U.S. dollars. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/private-equity-firms-sec-form-adv-2026", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/private-equity-firms-sec-form-adv-2026
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/private-equity-firms-sec-form-adv-2026
- Method, definitions and the latest version: https://glzrgroup.com/private-equity-firms/
