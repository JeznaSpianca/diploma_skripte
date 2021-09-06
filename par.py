#Argument 1 je alfa, argument 2 je beta
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import random
from decimal import Decimal, getcontext
from scipy.spatial import distance
from scipy.special import rel_entr
#from scipy.stats import entropy
from scipy import special


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

#Nastavitev velikost pisave histograma
plt.rc('xtick', labelsize=13) 
plt.rc('ytick', labelsize=13) 
plt.rc('axes', titlesize=22)
plt.rc('axes', labelsize=22)

#Izračun razredov histograma originalne porazdelitve
bins = np.histogram_bin_edges(array,bins="sturges")
counts, edges= np.histogram(array,bins)
#Izračun dolžine razreda
orig_razl=edges[1]-edges[0]
print(orig_razl)
#Deklariranje alfa, beta iz vnesenih vrednosti
alfa=float(sys.argv[1])
beta=float(sys.argv[2])

#Priprava tabel in spremenljivk
pareto=[]
porazd=[]
min_raz = 0

#Izracun prve umetne porazdelitve, da se dobi prvo minimalno razliko med razredi
for i in range(0,len(array)):
	e=1.0/alfa
	r=1-random.random()
	p=pow(r,e)
	t_med=beta/p
	pareto.append(t_med)
#Izračun velikosti razreda prve umetne porazd. in izračun razlike med razredi
#len(bins)-1 je parameter, ki pove da mora paretova porazdelitev imeti toliko razredov kot nasa zajeta
counts_p, edges_p = np.histogram(pareto,len(bins)-1)
raz=edges_p[1]-edges_p[0]
min_raz=abs(raz-orig_razl)
porazd=pareto
#print(min_raz,end="    ")
#print(alfa, end="    ")
#print(beta)
#Optimalna parametra
opt_alfa=alfa
opt_beta=beta

#Dvojna zanka, kjer gresta oba parametra do vpisane vrednosti, v vsakem koraku se 
#izračuna velikost razreda in preveri če je najmanjši do sedaj

for bt in np.arange(beta,15,0.1):
	for al in np.arange(alfa+0.1,15,0.1):
		pareto=[]
		for i in range(0,len(array)):
			e=1/al
			r=1-random.random()
			p=pow(r,e)
			t_med=bt/p
			pareto.append(t_med)	
		counts_p, edges_p = np.histogram(pareto,len(bins)-1)
		raz=edges_p[1]-edges_p[0]
		#print(abs(raz-orig_razl),end="     ")
		#print(al,end=" ")
		#print(bt)
		if min_raz > abs(raz-orig_razl):
			min_raz=abs(raz-orig_razl)
			opt_alfa=al
			opt_beta=bt
			porazd=pareto

#Izpis optimalnih parametrov in izris histograma 
print(counts)
print(counts_p)
print(min_raz)
print(opt_alfa)
print(opt_beta)
#print(len(array))

print(distance.jensenshannon(array,porazd))
counts_p, edges_p = np.histogram(porazd,len(edges)-1)
plt.hist(porazd, edges_p) 
plt.title('Histogram medprihodnih časov - umeten Pareto')
plt.xlabel('Čas med paketi (s)')
plt.ylabel('Število medprihodnih časov')
plt.show()
