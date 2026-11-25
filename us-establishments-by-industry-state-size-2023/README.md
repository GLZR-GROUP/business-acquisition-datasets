# U.S. Establishments by Industry, State and Size

**County Business Patterns 2023: establishments in nine employment-size classes**

Number of U.S. establishments with paid employees, their employment and annual payroll, in nine employment-size classes, for all industries, 20 sectors and 86 subsectors (2017 NAICS), for the United States, the 50 states and the District of Columbia. Compiled by GLZR Group from the U.S. Census Bureau's County Business Patterns 2023.

## Source
U.S. Census Bureau, County Business Patterns 2023.
- https://www.census.gov/data/datasets/2023/econ/cbp/2023-cbp.html

## Coverage
Period: 2023.
Place: United States.

## License and credit
The source data are works of the U.S. federal government (the U.S. Census Bureau) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Census Bureau, County Business Patterns 2023; compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/acquisition-targets/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-us-establishments-by-industry-state-size-2023.csv](glzr-us-establishments-by-industry-state-size-2023.csv)

- `glzr-us-establishments-by-industry-state-size-2023.csv`: U.S. establishments by industry, state and employment size, 2023 (5,433 rows, 18 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `area` | string | The United States, a state or the District of Columbia. |
| `naics` | string | 2017 NAICS code of the sector (2 digits) or subsector (3 digits); all = all industries. |
| `industry` | string | Title of the industry. |
| `level` | string | all, sector or subsector. |
| `establishments` | numeric | Establishments with paid employees. |
| `employees_mid_march` | numeric | Paid employees in the pay period including 12 March (mid-March employment). |
| `annual_payroll_usd_thousands` | numeric | Annual payroll, thousands of U.S. dollars. |
| `employees_1_to_4` | numeric | Establishments with 1 to 4 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_5_to_9` | numeric | Establishments with 5 to 9 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_10_to_19` | numeric | Establishments with 10 to 19 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_20_to_49` | numeric | Establishments with 20 to 49 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_50_to_99` | numeric | Establishments with 50 to 99 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_100_to_249` | numeric | Establishments with 100 to 249 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_250_to_499` | numeric | Establishments with 250 to 499 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_500_to_999` | numeric | Establishments with 500 to 999 employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `employees_1000_or_more` | numeric | Establishments with 1,000 or more employees (a count of establishments, not of employees); blank where the Census Bureau does not publish it. |
| `establishments_in_unpublished_size_classes` | numeric | Establishments in the size classes that are not published: establishments minus the published classes. |
| `year` | numeric | County Business Patterns year. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/us-establishments-by-industry-state-size-2023", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/us-establishments-by-industry-state-size-2023
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/us-establishments-by-industry-state-size-2023
- Method, definitions and the latest version: https://glzrgroup.com/acquisition-targets/
