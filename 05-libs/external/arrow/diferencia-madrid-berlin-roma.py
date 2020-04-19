import arrow

now_in_madrid = arrow.now("Europe/Madrid")
now_in_lisbon = arrow.now("Europe/Lisbon")
now_in_berlin = arrow.now("Europe/Berlin")
now_in_rome = arrow.now("Europe/Rome")

print("Diferencias horarias respecto a España peninsular:")
print(" - Portugal:", now_in_madrid.utcoffset() - now_in_lisbon.utcoffset())
print(" - Alemania:", now_in_madrid.utcoffset() - now_in_berlin.utcoffset())
print(" - Italia:",  now_in_madrid.utcoffset() - now_in_rome.utcoffset())
