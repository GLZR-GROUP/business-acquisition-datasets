"""Recompute the five within-band changes. No network calls or third-party dependencies."""
from pathlib import Path
import csv,json
from decimal import Decimal,ROUND_HALF_UP
D=Path(__file__).resolve().parent
rows=json.loads((D/'valuation-multiple-change-2023-2026.json').read_text(encoding='utf8'))['rows']
with (D/'valuation-multiple-change-2023-2026.csv').open(encoding='utf8',newline='') as f:
 csv_rows=list(csv.DictReader(f))
assert len(rows)==len(csv_rows)==5
for i,(row,cr) in enumerate(zip(rows,csv_rows)):
 a=Decimal(str(row['q2_2023_multiple']));b=Decimal(str(row['q2_2026_multiple']))
 assert a>0
 expected={'change_in_multiple':b-a,'relative_change_percent':(b/a-1)*100}
 for key,value in expected.items():
  rounded=value.quantize(Decimal('0.0001'),rounding=ROUND_HALF_UP)
  assert abs(Decimal(str(row[key]))-rounded)<Decimal('.00001'),(i,key)
 for key,value in row.items():
  assert str(value)==cr[key],(i,key,'CSV/JSON differ')
 assert row['earnings_basis']==('SDE' if i<3 else 'EBITDA')
 assert '\\u2013' not in row['enterprise_value_band_usd']
 print(f"{row['enterprise_value_band_usd']}: {row['earnings_basis']} {a} -> {b}; {row['relative_change_percent']:+.4f}%")
print('Verified five rows; no pooling across earnings bases.')
