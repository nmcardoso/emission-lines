import os
import io

import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv('emission_lines_crossmatch.csv')
filters = [ 'U', 'F378', 'F395', 'F410', 'F430', 'G', 'F515', 'R', 'F660', 'I', 'F861', 'Z']
alias = ['U', 'J0378', 'J0395', 'J0410', 'J0430', 'G', 'J0515', 'R', 'J0660', 'I', 'J0861', 'Z']
x = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
iso = [f'{f}_iso' for f in filters]
iso_err = [f'e_{f}_iso' for f in filters]
aper = [f'{f}_aper_6' for f in filters]
aper_err = [f'e_{f}_aper_6' for f in filters]  

for i, row in table.iterrows():
  print(f'Plot {i + 1} of {len(table)}')
  
  y_iso = row[iso].values.tolist()
  y_iso_err = row[iso_err].values.tolist()
  y_aper = row[aper].values.tolist()
  y_aper_err = row[aper_err].values.tolist()

  plt.ioff()
  plt.figure(figsize=(6, 4))
  plt.errorbar(x, y_iso, yerr=y_iso_err, fmt='-', capsize=4, alpha=.8, linewidth=1, markersize=3, marker='o', label='ISO')
  plt.errorbar(x, y_aper, yerr=y_aper_err, fmt='-', capsize=4, alpha=.8, linewidth=1, markersize=3, marker='o', label='APER')
  plt.gca().invert_yaxis()
  plt.xlabel('Wavelength [$\AA$]')
  plt.ylabel('Magnitude')
  plt.legend()
  plt.savefig(f'plots/{row["ID"]}', format='png', bbox_inches='tight', pad_inches=0.03)
  plt.close()