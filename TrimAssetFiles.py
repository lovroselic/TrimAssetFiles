# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:15:40 2023

@author: lovro
@version 0.1.0
"""

import regex as re
import pandas as pd
from os.path import join
from glob import glob
from collections import defaultdict

# =============================================================================
# # reading directory
# =============================================================================

Directory = 'C:/Users/lovro/OneDrive/Documents/JS/CM2 (WebGL)/Assets/AA/'
files = []
ext = ['*.png', '*.jpg']
for e in ext:
    files.extend(glob(join(Directory, e)))

files = sorted([f.split('\\')[1] for f in files])

# =============================================================================
# # reading assets
# =============================================================================

UsedFileList = defaultdict(dict)

_file = "C:/Users/lovro/OneDrive/Documents/JS/CM2 (WebGL)/assets_CrawlMaster2.js"
with open(_file) as fh:
    data = fh.read()

sources = ["LoadTextures", "LoadSprites"]
extract_regex = r'\s*=\s*\[[\-\w\.\s\*\/\,\{\}\:\"\']*\];'

for s in sources:
    extractionPattern = re.compile(re.escape(s) + extract_regex)
    loader = re.search(extractionPattern, data).group(0)
