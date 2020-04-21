import csv

import fire


def get_codemap():
    codemap = {}
    with open('iata.csv') as f:
        rd = csv.reader(f, delimiter='\t')
        header = next(rd)
        for items in rd:
            aeropuerto, pais, codigo_iata, resto = items
            codemap[codigo_iata] = (pais, aeropuerto)
    return codemap


class Airport(object):

    def __init__(self, code):
        self.codemap = get_codemap()
        self.code = code.upper()
        self.country = self.codemap[self.code][0]
        self.name = self.codemap[self.code][1]

if __name__ == '__main__':
  fire.Fire(Airport)
