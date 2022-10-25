import arrow

today = arrow.get()
navidad = today.replace(month=12, day=25)
print(navidad - today)
