import os
from pathlib import Path

p = Path('.')
for entry in p.iterdir():
    if entry.is_dir():
        print(f'{entry.name}/')
    else:
        size = os.path.getsize(entry)
        print(f'{entry.name} {size} bytes')
