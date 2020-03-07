avgtemps = []

fin = open('../files/temperatures.txt')
for line in fin:
    monthly_temps = [int(t) for t in line.strip().split(',')]
    avgtemp = sum(monthly_temps) / len(monthly_temps)
    avgtemps.append(avgtemp)
fin.close()

fout = open('avgtemps.txt', 'w')
for avgtemp in avgtemps:
    fout.write(f'{avgtemp}\n')
fout.close()
