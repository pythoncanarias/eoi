import csv

import fire

class Airport(object):

    def __init__(self, code):
        self.code = code.upper()
        self.source = 'airports.csv'
        with open(self.source) as f:
            rd = csv.reader(f)
            header = next(rd)
            for items in rd:
                if self.code == items[0]:
                    self.nombre = items[1]
                    self.latitud = float(items[2])
                    self.longitud = float(items[3])
                    self.coords = (self.latitud, self.longitud)
                    self.msg = f"{self.code} {self.nombre} ({self.latitud}, {self.longitud})"
                    break
            else:
                self.msg = f"Codigo {self.code} no encontrado"

    def __str__(self):
        return self.msg

if __name__ == '__main__':
    fire.Fire(Airport)
