# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:15:40 2023

@author: lovro
@version 0.2.0
"""

import regex as re
import pandas as pd
from os.path import join
from glob import glob
import os
import sys

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

UsedFileList = {}

_file = "C:/Users/lovro/OneDrive/Documents/JS/CM2 (WebGL)/assets_CrawlMaster2.js"
with open(_file) as fh:
    data = fh.read()

sources = ["LoadTextures", "LoadSprites"]
extract_regex = r'\s*=\s*\[[\-\w\.\s\*\/\,\{\}\:\"\']*\];'
line_regex = r'{[\-\w\.\s\*\/\,\:\"\']*}'
fileNamePattern = re.compile(r'srcName:\s*\"([\w\-\'\.\s]*)\"')
namePattern = re.compile(r'name:\s*\"([\w\-\'\.\s]*)\"')
warning = 0

for s in sources:
    extractionPattern = re.compile(re.escape(s) + extract_regex)
    loader = re.search(extractionPattern, data).group(0)

    for match in re.finditer(line_regex, loader):
        line = match.group(0)
        fName = re.search(fileNamePattern, line).group(1)
        Name = re.search(namePattern, line).group(1)
        if Name in UsedFileList:
            print("exists->", Name)
            warning += 1
        UsedFileList[Name] = fName

LIST = pd.DataFrame({'Name': UsedFileList})
fileList = LIST['Name'].tolist()

if warning > 0:
    sys.exit()


# =============================================================================
# # find unused
# =============================================================================

files = set(files)
fileList = set(fileList)
toDelete = files.difference(fileList)

# =============================================================================
# # delete unused
# =============================================================================

print("Deleting ", len(toDelete), " files")
for f in toDelete:
    deleteFile = Directory + f
    print("deleting file:", deleteFile)
    os.remove(deleteFile)
