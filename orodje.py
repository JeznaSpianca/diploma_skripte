import numpy as np
import sys
import os
import matplotlib.pyplot as plt

#Branje podatkov v tabelo
array = []
with open('doma_casi_2.txt') as file:
	for line in file:
		array.append(float(line.strip()))

bins = np.histogram_bin_edges(array,bins="sturges")

counts, edges= np.histogram(array,bins)
print(counts)
print(edges)

b=0
st=0
#Izpis razredov histograma
for edge in edges:
	if b==0:
		print("Spodnja meja: ", end = "")
		print("{:.9f}".format(round(edge,9)), end = " ")
		b=1
		continue
	print("Zgornja meja: ", end = " ")
	print("{:.9f}".format(round(edge,9)), end=" ")
	print("Število časov: "+ str(int(counts[st])))
	st+=1	
	if st != len(counts):
		print("Spodnja meja: ", end = "")
		print("{:.9f}".format(round(edge,9)), end = " ")
rel_frekvence = []
for i in counts:
	rel_frekvence.append(round(((i/len(array))*100),5))

#Izpis nekaterih vrednosti porazdelitve
print("velikost razreda: " + str(edges[1]-edges[0]))
print(rel_frekvence)
print("Minimalni čas: " + "{:.9f}".format(round(min(array),9)))
print("Maksimalni čas: " + str(round(max(array),9)))
print("število razredov: " + str(len(edges)-1))
print("Avg: "+ str(sum(array)/len(array)))
print("Št časov: " + str(len(array)))
plt.rc('xtick', labelsize=13) 
plt.rc('ytick', labelsize=13) 
plt.rc('axes', titlesize=22)
plt.rc('axes', labelsize=22)
#Izris histograma
plt.hist(array, bins) 
plt.title('Histogram medprihodnih časov - oddaljena lokacija')
plt.xlabel('Čas med paketi (s)')
plt.ylabel('Število medprihodnih časov')
plt.show()



