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

import shutil
from zipfile import ZipFile
from scripts.init_vars import archives_paths, paths
import os
import tarfile

def unzip(filename, save_to):
    with ZipFile(filename, 'r') as zipObj:
        for member in zipObj.namelist():
            file = os.path.basename(member)
            # skip directories
            if not file:
                continue
            source = zipObj.open(member)
            target = open(os.path.join(save_to, file), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

def extract_posenet_pose(force=False, verbose=True):
    if verbose:
        print('Extracting PoseNet poses...')
    if any(os.scandir(paths['posenet'])) and not force:
        if verbose:
            print('\t{} already extracted, skipping...'.format(os.listdir(archives_paths['posenet'])[0]))
    else:
        if verbose:
            print('\tExtracting: {}'.format(os.listdir(archives_paths['posenet'])[0]))
        unzip(filename=os.path.join(archives_paths['posenet'],
              os.listdir(archives_paths['posenet'])[0]),
              save_to=paths['posenet'])