#!/usr/bin/env python

import os
import datetime
import hashlib


def get_hash(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        m.update(f.read())
    return m.hexdigest()


print(f"{'filename':28} {'size (bytes)':>14} {'last mod':>24} {'hash md5':>32}")
print("-"*28, "-"*14, "-"*24, "-"*32)
for fn in os.listdir("."):  # . significa "El directorio actual"
    size = os.path.getsize(fn)
    hash_md5 = get_hash(fn)
    last_mod = datetime.datetime.fromtimestamp(os.path.getmtime(fn))
    print(f"{fn:<28} {size:>14} {last_mod.ctime():24} {hash_md5:<32}")
