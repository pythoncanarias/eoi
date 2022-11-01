import os
import collections

import matplotlib.pyplot as plt

FILETYPES = [
    ".pdf",
    ".txt",
    ".doc",
    ".mp4",
    ".xls",
    ".py",
    "ipynb",
]

counter = collections.Counter()
sizes = collections.Counter()
home = os.path.expanduser("~") + "/Dropbox"
for (basedir, dirnames, filenames) in os.walk(home):
    for filename in filenames:
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext in FILETYPES:
            counter[ext] += 1

labels = list(counter.keys())
plt.barh(labels, counter.values(), color ="coral", alpha=0.3)
plt.show()

