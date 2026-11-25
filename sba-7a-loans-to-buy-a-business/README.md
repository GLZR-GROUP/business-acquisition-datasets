# SBA 7(a) Loans to Buy a Business, FY2020-2026

**Change-of-ownership 7(a) loans by fiscal year, state and industry**

For each fiscal year from 2020 to 2026, and for the seven years together, and for the United States, each state, the District of Columbia and the territories with loans, all industries and the 2022 NAICS sectors: the number of SBA 7(a) term loans recorded as a change of ownership (without the loans later cancelled), the amount approved, the median loan, their share of all 7(a) term loans, the loans later cancelled, the lines of credit, and the loans in five size bands, compiled by GLZR Group from the U.S. Small Business Administration's 7(a) FOIA loan data, as of 30 September 2026.

## Source
U.S. Small Business Administration, 7(a) FOIA loan data; U.S. Census Bureau, County Business Patterns 2023.
- https://data.sba.gov/sites/default/files/uploaded_resources/FOIA_7a_FY2020_Present_asof_260930.csv

## Coverage
Period: 2019-10-01/2026-09-30.
Place: United States.

## License and credit
The source data are works of the U.S. federal government (the U.S. Small Business Administration and the U.S. Census Bureau) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Small Business Administration, 7(a) FOIA loan data; U.S. Census Bureau, County Business Patterns 2023; compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/sba-loans-to-buy-a-business/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-sba-7a-loans-to-buy-a-business-fy2020-fy2026.csv](glzr-sba-7a-loans-to-buy-a-business-fy2020-fy2026.csv)

- `glzr-sba-7a-loans-to-buy-a-business-fy2020-fy2026.csv`: SBA 7(a) loans to buy a business (change of ownership) by fiscal year, state and industry, fiscal 2020 to 2026 (7,813 rows, 17 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `fiscal_year` | string | Fiscal year the loans were approved (U.S. federal fiscal years end 30 September); 2020-2026 = the seven years together. |
| `area_code` | string | Two-letter code of the state, the District of Columbia or the territory of the project (SBA ProjectState); US = the United States. |
| `area_name` | string | Name of the area. |
| `naics_sector` | string | 2022 NAICS sector of the business (the first two digits of its NAICS code; 31-33, 44-45 and 48-49 are each one sector); 00 = all industries. |
| `naics_sector_title` | string | Title of the NAICS sector. |
| `loans` | numeric | SBA 7(a) term loans recorded with the business age 'Change of Ownership', without the loans later cancelled. Revolving lines of credit are not included. |
| `amount_usd` | numeric | Total amount approved for those loans (GrossApproval), U.S. dollars. |
| `median_usd` | numeric | Median amount approved, U.S. dollars, rounded half up to the dollar; blank where there are fewer than 5 loans. |
| `share_of_7a_term_loans_pct` | numeric | loans as a percent of all_7a_term_loans, to one decimal, rounded half up; blank where all_7a_term_loans is 0. |
| `loans_cancelled` | numeric | Change-of-ownership 7(a) term loans later cancelled (LoanStatus CANCLD); not included in loans. |
| `lines_of_credit` | numeric | Change-of-ownership revolving lines of credit (RevolverStatus Y) not cancelled; not included in loans. |
| `all_7a_term_loans` | numeric | All 7(a) term loans not cancelled in the same fiscal year, area and sector, every business age. |
| `loans_up_to_150k` | numeric | Loans of up to $150,000. |
| `loans_150k_to_350k` | numeric | Loans of over $150,000 to $350,000. |
| `loans_350k_to_1m` | numeric | Loans of over $350,000 to $1 million. |
| `loans_1m_to_2m` | numeric | Loans of over $1 million to $2 million. |
| `loans_2m_to_5m` | numeric | Loans of over $2 million to $5 million. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/sba-7a-loans-to-buy-a-business", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/sba-7a-loans-to-buy-a-business
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/sba-7a-loans-to-buy-a-business
- Method, definitions and the latest version: https://glzrgroup.com/sba-loans-to-buy-a-business/
