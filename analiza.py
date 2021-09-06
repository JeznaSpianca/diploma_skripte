import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import random
from scipy.spatial import distance

#branje datoteke s casi v tabelo
array = []
with open('doma_pi_diploma_casi.txt') as file:
	for line in file:
		array.append(float(line.strip()))



#del kode če bomo odstranjevali top n željenih časov
"""
array.sort(reverse=True)
for i in range(0,5542):
	array.pop(0)
print(len(array))
"""

#Izračun razredov histograma originalne porazdelitve
bins = np.histogram_bin_edges(array,bins="sturges")
counts, edges= np.histogram(array,bins)
print(counts)
print(edges)
#Izračun dolžine razreda
orig_razl=edges[1]-edges[0]

sir_cilj=edges[1]-edges[0]
#print(sir_cilj)

#Izracun prve umetne porazdelitve, da se dobi prvo minimalno razliko med razredi
poisson = []
min_raz = 0
t=float(sys.argv[1])
t_min=float(sys.argv[1])
for i in range(0,len(array)):
	t_med=-t*np.log(float(1)-random.random())
	poisson.append(t_med)
#Izračun velikosti razreda prve umetne porazd. in izračun razlike med razredi
#len(bins)-1 je parameter, ki pove da mora paretova porazdelitev imeti toliko razredov kot nasa zajeta
counts_p, edges_p = np.histogram(poisson,len(bins)-1)
raz=edges_p[1]-edges_p[0]
min_raz=abs(raz-orig_razl)
umeten_poiss=poisson
#print(min_raz,end="    ")
#print(t)

#Dvojna zanka, kjer gresta oba parametra do vpisane vrednosti, v vsakem koraku se 
#izračuna velikost razreda in preveri če je najmanjši do sedaj
for t in np.arange(float(sys.argv[1])+0.01,10.00,0.01):
	poisson = []
	for i in range(0,len(array)):
		t_med=-t*np.log(float(1)-random.random())
		poisson.append(t_med)
	counts_p, edges_p = np.histogram(poisson,len(bins)-1)
	raz=edges_p[1]-edges_p[0]
	#print(abs(raz-orig_razl),end="     ")
	#print(t)
	if min_raz > abs(raz-orig_razl):
		min_raz=abs(raz-orig_razl)
		umeten_poiss=poisson
		t_min=t

#Izpis optimalnih parametrov in izris histograma		
print("Originalna: "+ str(orig_razl))
print(counts_p)
print(edges_p)
print(min_raz)
print(t_min)
print(round(distance.jensenshannon(array,umeten_poiss),3))
#counts_p, edges_p = np.histogram(umeten_poiss,len(bins)-1)
plt.rc('xtick', labelsize=13) 
plt.rc('ytick', labelsize=13) 
plt.rc('axes', titlesize=22)
plt.rc('axes', labelsize=22)
plt.hist(umeten_poiss, edges_p) 
plt.title('Histogram medprihodnih časov - umetna eksponentna')
plt.xlabel('Čas med paketi (s)')
plt.ylabel('Število medprihodnih časov')
plt.show()

