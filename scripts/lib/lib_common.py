# Copyright (C) 2021  Federico Angelini
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details:
# http://www.gnu.org/licenses/gpl.txt

from scripts.init_vars import paths
import os
import pickle
import pandas as pd
import numpy as np
import warnings

def read_poses(path=paths['pose']):
    report = pd.DataFrame(columns=['sample', 'dataset', 'actor', 'action', 'length', 'aver_conf', 'fn%'])
    for i in sorted(os.listdir(path)):
        with open(os.path.join(path, i), 'rb') as f:
            d = pickle.load(f)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            report = report.append({'sample': d['name'],
                                    'dataset': d['dataset'],
                                    'actor': d['actor'],
                                    'action': d['action'],
                                    'length': d['length'],
                                    'aver_conf': np.nanmean(d['seq'][:, 2, :]),
                                    'fn%': np.isnan(d['seq'][:, [0, 1], :]).sum()/d['seq'][:, [0, 1], :].size}, ignore_index=True)
    return report

