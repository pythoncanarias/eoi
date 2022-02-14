import arrow

WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

dia = arrow.utcnow()
futuro = dia.shift(years=8, months=3, days=9)
wd = futuro.weekday()
print(f"El día {futuro.format('D/MMM/YYYY')} cae en {WEEKDAYS[wd]}")
