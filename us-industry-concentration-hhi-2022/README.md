# U.S. Industry Concentration (HHI), 2022

**HHI and the shares of the 4, 8, 20 and 50 largest firms, 1,461 industries**

Every industry in the U.S. Census Bureau's 2022 Economic Census file of establishment and firm size statistics (ECNSIZE2022) with a published Herfindahl-Hirschman Index: NAICS code and level, the number of firms with payroll, sales, value of shipments or revenue, the shares of the 4, 8, 20 and 50 largest firms, and the HHI, for the United States, compiled by GLZR Group.

## Source
U.S. Census Bureau, 2022 Economic Census, Establishment and Firm Size Statistics for the U.S. (ECNSIZE2022).
- https://www2.census.gov/programs-surveys/economic-census/data/2022/API_Datasets/ECNSIZE2022.zip

## Coverage
Period: 2022.
Place: United States.

## License and credit
The source data are works of the U.S. federal government (the U.S. Census Bureau) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Census Bureau, 2022 Economic Census, Establishment and Firm Size Statistics for the U.S. (ECNSIZE2022); compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/horizontal-vs-vertical-integration/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-us-industry-concentration-2022.csv](glzr-us-industry-concentration-2022.csv)

- `glzr-us-industry-concentration-2022.csv`: U.S. industry concentration, 2022: the HHI and the shares of the 4, 8, 20 and 50 largest firms in 1,461 industries (1,461 rows, 12 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `naics` | string | 2022 NAICS code of the industry. |
| `industry` | string | Title of the NAICS industry. |
| `naics_level` | numeric | Digits of the NAICS code: 2 = sector, 3 = subsector, 4 = industry group, 5 = NAICS industry, 6 = national industry. |
| `sector` | string | The NAICS sector the industry belongs to. |
| `firms` | numeric | Number of firms with payroll in the industry. |
| `sales_shipments_or_revenue_usd_thousands` | numeric | Sales, value of shipments, or revenue of the industry, thousands of U.S. dollars. |
| `top4_share_pct` | numeric | Percent of the industry's sales, shipments or revenue held by its 4 largest firms. |
| `top8_share_pct` | numeric | Percent held by its 8 largest firms. |
| `top20_share_pct` | numeric | Percent held by its 20 largest firms; blank where the Census Bureau does not publish it. |
| `top50_share_pct` | numeric | Percent held by its 50 largest firms; blank where the Census Bureau does not publish it. |
| `hhi_50_largest_firms` | numeric | Herfindahl-Hirschman Index for the 50 largest firms, as the Census Bureau publishes it. |
| `year` | numeric | Economic Census year. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/us-industry-concentration-hhi-2022", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/us-industry-concentration-hhi-2022
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/us-industry-concentration-hhi-2022
- Method, definitions and the latest version: https://glzrgroup.com/horizontal-vs-vertical-integration/
