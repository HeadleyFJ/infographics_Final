import csv
import numpy as np
import matplotlib.pyplot as plt

lum = []
log_mass = []
log_steldens = []
veldisp = []

with open('AGN_data.csv') as csv_file:
    file = csv.DictReader(csv_file, delimiter=',')
    for col in file:
        lum.append(float(col['Column8']))
        log_mass.append(float(col['Column12']))
        log_steldens.append(float(col['Column13']))
        veldisp.append(float(col['Column17']))

zero_index = []

for i in log_mass:
    if i == 0:
        zero_index.append(log_mass.index(i))
        log_mass.remove(i)
        
for i in zero_index:
    del lum[i]
    del log_steldens[i]
    del veldisp[i]
    
ninetynine_index = []

for i in lum:
    if i == 99:
        ninetynine_index.append(lum.index(i))
        lum.remove(i)
        
for i in ninetynine_index:
    del log_mass[i]
    del log_steldens[i]
    del veldisp[i]

print(len(log_mass))

plt.figure(figsize=(30,30),dpi=80)
plt.scatter(log_mass,lum,alpha=0.2,c='r')

