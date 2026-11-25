# U.S. Business Owners by Age, 2023

**Owner age and year acquired, by state and industry (Census ABS)**

Every published figure for owner age and the year the owner acquired the business, for the United States, the 50 states and the District of Columbia, all industries, the 19 sectors the survey covers and industries not classified (2022 NAICS): the count of owners of respondent employer firms, the percent, the relative standard error, the standard error of the percent and the Census Bureau's flags, exactly as published in the U.S. Census Bureau's 2023 Annual Business Survey (reference year 2022), Characteristics of Business Owners, table AB2300CSCBO. Percents are among owners of responding firms; the Census Bureau says these tables are not intended to estimate total owners. Compiled by GLZR Group.

## Source
U.S. Census Bureau, 2023 Annual Business Survey, Characteristics of Business Owners.
- https://www2.census.gov/programs-surveys/abs/data/2023/AB2300CSCBO.zip

## Coverage
Period: 2022.
Place: United States.

## License and credit
The source data are works of the U.S. federal government (the U.S. Census Bureau) and are in the public domain in the United States. This file is GLZR Group's compilation of them. Please credit: U.S. Census Bureau, 2023 Annual Business Survey, Characteristics of Business Owners; compiled by GLZR Group (https://glzrgroup.com/).

## Method, definitions and the latest version
The page this file comes from explains the method, the definitions and the limits, and keeps the latest version: https://glzrgroup.com/business-owners-by-age/

## About GLZR Group
GLZR Group is a business acquisition intermediary. It connects business buyers and sellers. Guides, calculators and market data: https://glzrgroup.com/

## Files

- Download: [glzr-us-business-owners-by-age-state-industry-2023-abs.csv](glzr-us-business-owners-by-age-state-industry-2023-abs.csv)

- `glzr-us-business-owners-by-age-state-industry-2023-abs.csv`: Owners of U.S. businesses with employees by age and by year the owner acquired the business, by state and industry (2023 Annual Business Survey) (17,779 rows, 17 columns).

## Columns

| Column | Type | Description |
|---|---|---|
| `GEO_ID` | string | Census Bureau geographic identifier: 0100000US = the United States; 0400000US followed by the state's FIPS code = a state. |
| `GEO_LABEL` | string | Name of the area. |
| `NAICS2022` | string | 2022 NAICS code of the sector; 00 = all sectors. |
| `NAICS2022_LABEL` | string | Title of the NAICS sector. |
| `QDESC` | string | Census Bureau code of the survey question. |
| `QDESC_LABEL` | string | The question: OWNRAGE = the owner's age; YRACQBUS = the year the owner acquired the business. |
| `OWNCHAR` | string | Census Bureau code of the answer. |
| `OWNCHAR_LABEL` | string | The answer: an age group or a period, or Total reporting, Item not reported or Don't know. |
| `YEAR` | numeric | Survey year: the 2023 Annual Business Survey, whose reference year is 2022. |
| `OWNPDEMP` | numeric | Number of owners of respondent employer firms (Census Bureau label). Each firm reported on up to four owners with the largest shares; not weighted for nonresponse. |
| `OWNPDEMP_F` | string | Flag for OWNPDEMP: S = withheld because it did not meet the Census Bureau's publication standards; blank = published. |
| `OWNPDEMP_PCT` | numeric | Percent of number of owners of respondent employer firms (%), as the Census Bureau publishes it. |
| `OWNPDEMP_PCT_F` | string | Flag for OWNPDEMP_PCT: S = withheld because it did not meet the Census Bureau's publication standards; X = not applicable; blank = published. |
| `OWNPDEMP_S` | numeric | Relative standard error of number of owners of respondent employer firms (%). |
| `OWNPDEMP_S_F` | string | Flag for OWNPDEMP_S: S = withheld because it did not meet the Census Bureau's publication standards; blank = published. |
| `OWNPDEMP_PCT_S` | numeric | Standard error of the percent in OWNPDEMP_PCT, in percentage points. |
| `OWNPDEMP_PCT_S_F` | string | Flag for OWNPDEMP_PCT_S: S = withheld because it did not meet the Census Bureau's publication standards; X = not applicable; blank = published. |

## Load it

```python
from datasets import load_dataset

ds = load_dataset("glzrgroup/us-business-owners-by-age-2023", split="train")
```

## Also published on

- Hugging Face: https://huggingface.co/datasets/glzrgroup/us-business-owners-by-age-2023
- Kaggle: https://www.kaggle.com/datasets/glzrgroup/us-business-owners-by-age-2023
- Method, definitions and the latest version: https://glzrgroup.com/business-owners-by-age/
