import os
import io

import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('emission_lines_crossmatch.csv')
filters = ['F378', 'F395', 'F410', 'F430', 'F515', 'F660', 'F861', 'G', 'I', 'R', 'Z', 'U']
iso = [f'{f}_iso' for f in filters]
iso_err = [f'e_{f}_iso' for f in filters]
aper = [f'{f}_aper_6' for f in filters]
aper_err = [f'e_{f}_aper_6' for f in filters]  

for i, row in table.iterrows():
  print(f'Plot {i} of {len(table)}')
  
  x = list(range(12))
  y_iso = row[iso].values.tolist()
  y_iso_err = row[iso_err].values.tolist()
  y_aper = row[aper].values.tolist()
  y_aper_err = row[aper_err].values.tolist()

  plt.ioff()
  plt.figure(figsize=(6, 4))
  plt.errorbar(x, y_iso, yerr=y_iso_err, fmt='--', capsize=4, alpha=.8, linewidth=1, markersize=3, marker='o', label='ISO')
  plt.errorbar(x, y_aper, yerr=y_aper_err, fmt='--', capsize=4, alpha=.8, linewidth=1, markersize=3, marker='o', label='Aper')
  plt.xticks(x, filters, rotation=45)
  plt.legend()
  plt.savefig(f'plots/{row["ID"]}', format='png', bbox_inches='tight', pad_inches=0.03)
  plt.close()