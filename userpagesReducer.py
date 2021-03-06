#!/usr/bin/python

"""
Get all view pages for all individual users
Mapper: (ID,view page url)
Reducer: (user, view page urls list)
"""

import sys
import json

urlSet = set()  # only store unique pages
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something wrong. Skip this line.
        continue

    ID, path = data_mapped

    if oldKey and oldKey != ID:
        try:  # handle exception
            res = json.dumps(list(urlSet))
        except UnicodeDecodeError:
            continue
        print oldKey, "\t", res
        urlSet.clear()

    oldKey = ID
    urlSet.add(path)

if oldKey is not None:
    try:
        res = json.dumps(list(urlSet))
    except UnicodeDecodeError:
        pass
    print oldKey, "\t", res
    urlSet.clear()
