import argparse

parser = argparse.ArgumentParser()
parser.add_argument("target")
options = parser.parse_args()
print(options.target)

