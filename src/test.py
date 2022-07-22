import os
import shutil

base_p = '/Users/danich/Documents/thesis/manual-captions/'
for d in os.listdir(base_p):
    base_pd = os.path.join(base_p, d)
    for inner_d in os.listdir(base_pd):
        if inner_d in ['chg', 'ref']:
            full_p = os.path.join(base_p, d, inner_d)
            for inner_dd in os.listdir(full_p):
                shutil.move(
                    os.path.join(full_p, inner_dd),
                    os.path.join(base_pd, f'old_{inner_dd}')
                )
