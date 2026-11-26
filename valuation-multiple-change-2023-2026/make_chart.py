"""Generate the chart directly from the JSON. Requires matplotlib; no network calls."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parent
rows=json.loads((D/'valuation-multiple-change-2023-2026.json').read_text(encoding='utf8'))['rows']
plt.rcParams.update({'font.family':'DejaVu Sans','text.parse_math':False,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(10,6.7),facecolor='#f7f6f1');ax.set_facecolor('#f7f6f1')
fig.subplots_adjust(left=.32,right=.92,bottom=.22,top=.72)
fig.text(.07,.93,'GLZR GROUP  /  MARKET DATA',fontsize=11,color='#5d6b79')
fig.text(.07,.86,'Valuation multiples moved differently',fontsize=23,color='#14243a',weight='bold')
fig.text(.07,.79,'Q2 2023 to Q2 2026 • Change within each deal-size band',fontsize=13,color='#14243a')
for i,row in enumerate(rows):
 v=row['relative_change_percent']
 ax.barh(i,v,color='#9b7342' if v>=0 else '#4c6684',height=.48)
 if v==0:ax.plot(0,i,'o',color='#9b7342',markersize=6)
 ax.text(v+(1 if v>=0 else -1),i,f'{v:+.1f}%' if v else '0.0%',ha='left' if v>=0 else 'right',va='center',fontsize=13,color='#14243a')
labels=[r['enterprise_value_band_usd']+'  |  '+r['earnings_basis'] for r in rows]
ax.set_yticks(range(5),labels,fontsize=12,color='#14243a')
ax.invert_yaxis();ax.set_xlim(-21,29);ax.axvline(0,color='#bcc3c9',lw=1)
ax.set_xticks([-20,-10,0,10,20],['−20%','−10%','0%','+10%','+20%'],fontsize=10,color='#5d6b79')
ax.tick_params(axis='both',length=0,pad=10)
for spine in ax.spines.values():spine.set_visible(False)
fig.text(.07,.115,'Source: IBBA and M&A Source, Q2 2026 Highlights. Calculations: GLZR Group.',fontsize=10,color='#14243a')
fig.text(.07,.075,'Different transactions may underlie each period. SDE and EBITDA are separate bases.',fontsize=10,color='#5d6b79')
fig.text(.07,.04,'Change in a reported multiple is not appreciation of the same business or a price forecast.',fontsize=10,color='#5d6b79')
fig.savefig(D/'valuation-multiple-change.png',dpi=170,facecolor=fig.get_facecolor())
fig.savefig(D/'valuation-multiple-change.svg',facecolor=fig.get_facecolor(),metadata={'Date':None})
plt.close(fig)
print('Chart generated from five JSON rows.')
