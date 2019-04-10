import math as mt
import random as rd
import csv

rd.seed(1)

# -----------------------------------
#
#
# ----------- OGGETTI ---------------
#
#
# -----------------------------------

class Team:
	def __init__(self, name, overall):
		self.name = name
		self.overall = overall
		
class Match:
	def __init__(self, home, away, result):
		self.home = home
		self.away = away
		self.result = result

# metodi per calcolare l'overall di una squadra
all_team = []
team = ["Atalanta", "Benevento Calcio", "Bologna", "Cagliari", "Chievo Verona", "Crotone", "Fiorentina", "Genoa", "Inter", "Juventus", "Lazio", "Milan", "Napoli", "Roma", "Sampdoria", "Sassuolo", "Ferrara (SPAL)", "Torino", "Udinese", "Hellas Verona"]	

# -----------------------------------
#
#
# ------------ METODI ---------------
#
#
# -----------------------------------

# ritorna la media overall della squadra
def team_overall(lista):
	i = 0
	sum = 0
	while i < 11:
		sum += int(lista[i])
		i += 1
		
	return sum/11

# legge i dati dal file
def encoding(team):
	lista = []
	#enconding molto importante
	with open('CompleteDataset.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
		# mette nella lista gli overall dei primi 11 giocatori, una squadra alla volta
			if row[8] == team and len(lista) < 11:
				lista.append(row[6])
	
	# mette nell'array di oggetti Team, il nome della squadra - la media dei valori dei giocatori
	all_team.append(Team(t, int(team_overall(lista))))

# metodo che restituisce l'overall della squadra, specificando il nome
def contains(name):
	for l in all_team:
		if name == l.name:
			return float(l.overall/10.0)
	return 0

# calcola la media di tutte le squadre
for t in team:
	encoding(t)

### stampa a video il nome e la media della squadra
for all in all_team:
	print(all.name, all.overall)

# -----------------------------------
#
#
# -------- RETE NEURALE -------------
#
#
# -----------------------------------

### stampa a video la predizione
def result(pred):
	if pred < 0.33:
		print("vittoria in casa")
	elif pred < 0.66:
		print("pareggio")
	else:
		print("vittoria fuori casa")

def RN(m1, m2):
	t = m1*w1 + m2*w2 + b
	return sigmoide(t)
	
def sigmoide(t):
	return 1 / (1 + mt.exp(-t))
	
w1 = rd.random()
w2 = rd.random()
b = rd.random()

#dataset = [ [contains("Juventus"), contains("Cagliari"), 0], [contains("Hellas Verona"), contains("Napoli"), 1], [contains("Atalanta"), contains("Roma"), 1], [contains("Sassuolo"), contains("Genoa"), 0.5], [contains("Lazio"), contains("Ferrara (SPAL)"), 0.5], [contains("Crotone"), contains("Milan"), 1], [contains("Sampdoria"), contains("Benevento Calcio"), 0], [contains("Bologna"), contains("Torino"), 0.5], [contains("Udinese"), contains("Chievo Verona"), 1], [contains("Inter"), contains("Fiorentina"), 0], [contains("Genoa"), contains("Juventus"), 1], [contains("Benevento Calcio"), contains("Bologna"), 1], [contains("Roma"), contains("Inter"), 1], [contains("Torino"), contains("Sassuolo"), 0], [contains("Chievo Verona"), contains("Lazio"), 1], [contains("Milan"), contains("Cagliari"), 0], [contains("Fiorentina"), contains("Sampdoria"), 1], [contains("Crotone"), contains("Hellas Verona"), 0.5], [contains("Ferrara (SPAL)"), contains("Udinese"), 0], [contains("Napoli"), contains("Atalanta"), 0] ]
juve_data = [ [contains("Chievo Verona"), contains("Juventus"), 1], [contains("Juventus"), contains("Lazio"), 0], [contains("Parma"), contains("Juventus"), 1], [contains("Juventus"), contains("Sassuolo"), 0], [contains("Frosinone"), contains("Juventus"), 1], [contains("Juventus"), contains("Bologna"), 0], [contains("Juventus"), contains("Napoli"), 0], [contains("Udinese"), contains("Juventus"), 0], [contains("Juventus"), contains("Genoa"), 0], [contains("Empoli"), contains("Juventus"), 1], [contains("Juventus"), contains("Cagliari"), 0], [contains("Milan"), contains("Juventus"), 1], [contains("Juventus"), contains("Spal (Ferrara)"), 0], [contains("Fiorentina"), contains("Juventus"), 1], [contains("Juventus"), contains("Inter"), 0], [contains("Torino"), contains("Juventus"), 1], [contains("Juventus"), contains("Roma"), 0], [contains("Atalanta"), contains("Juventus"), 0.5], [contains("Juventus"), contains("Sampdoria"), 0], [contains("Bologna"), contains("Juventus"), 1], [contains("Juventus"), contains("Chievo Verona"), 0], [contains("Lazio"), contains("Juventus"), 1], [contains("Juventus"), contains("Parma"), 0.5], [contains("Sassuolo"), contains("Juventus"), 1], [contains("Juventus"), contains("Frosinone"), 0], [contains("Bologna"), contains("Juventus"), 1], [contains("Napoli"), contains("Juventus"), 1], [contains("Juventus"), contains("Udinese"), 0], [contains("Genoa"), contains("Juventus"), 0], [contains("Juventus"), contains("Empoli"), 0], [contains("Cagliari"), contains("Juventus"), 1], [contains("Juventus"), contains("Milan"), 0] ]
spal_data = [ [contains("Bologna"), contains("Ferrara (SPAL)"), 1], [contains("Ferrara (SPAL)"), contains("Parma"), 0], [contains("Torino"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Atalanta"), 0], [contains("Fiorentina"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Sassuolo"), 1], [contains("Sampdoria"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Inter"), 1], [contains("Roma"), contains("Ferrara (SPAL)"), 1], [contains("Ferrara (SPAL)"), contains("Frosinone"), 1], [contains("Lazio"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Cagliari"), 0.5], [contains("Juventus"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Empoli"), 0.5], [contains("Genoa"), contains("Ferrara (SPAL)"), 0.5], [contains("Ferrara (SPAL)"), contains("Chievo Verona"), 0.5], [contains("Napoli"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Udinese"), 0.5], [contains("Milan"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Bologna"), 0.5], [contains("Parma"), contains("Ferrara (SPAL)"), 1], [contains("Ferrara (SPAL)"), contains("Torino"), 0.5], [contains("Atalanta"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Fiorentina"), 1], [contains("Sassuolo"), contains("Ferrara (SPAL)"), 0.5], [contains("Ferrara (SPAL)"), contains("Sampdoria"), 1], [contains("Inter"), contains("Ferrara (SPAL)"), 0], [contains("Ferrara (SPAL)"), contains("Roma"), 0], [contains("Frosinone"), contains("Ferrara (SPAL)"), 1], [contains("Ferrara (SPAL)"), contains("Lazio"), 0], [contains("Cagliari"), contains("Ferrara (SPAL)"), 0] ]

def sigmoide_p(t):
	return sigmoide(t) * (1 - sigmoide(t))
	
# w1 = in casa, w2 = fuori casa, b
def train(sett):
	w1 = rd.random()
	w2 = rd.random()
	b = rd.random()
	
	iterazioni = 1000
	learning_rate = 0.1
	
	for i in range(iterazioni):
		ri = rd.randint(0, len(sett) - 1)
		point = sett[ri]
		
		z = point[0] * w1 + point[1] * w2 + b
		pred = sigmoide(z)
			
		target = point[2]
		
		cost = (pred - target)**2
			
		dcost_dpred = 2 * (pred - target)
		dpred_dz = sigmoide_p(z)
			
		dz_dw1 = point[0]
		dz_dw2 = point[1]
		dz_db = 1
			
		dcost_dz = dcost_dpred * dpred_dz
			
		dcost_dw1 = dcost_dz * dz_dw1
		dcost_dw2 = dcost_dz * dz_dw2
		dcost_db = dcost_dz * dz_db
			
		w1 = w1 - learning_rate * dcost_dw1
		w2 = w2 - learning_rate * dcost_dw2
		b = b - learning_rate * dcost_db
		
	return w1, w2, b
		
w1, w2, b = train(juve_data)
w3, w4, b2 = train(spal_data)

print(w1, w2, b)
print(w3, w4, b2)

match = [contains("Juventus"), contains("Ferrara (SPAL)")]
print(contains("Juventus"), contains("Ferrara (SPAL)"))
z = w1 * match[0] + w4 * match[1] + (b + b2)
prediction = sigmoide(z)
print(prediction)
result(prediction)

match = [contains("Ferrara (SPAL)"), contains("Juventus")]
z = w3 * match[0] + w2 * match[1] + (b + b2)
prediction = sigmoide(z)
print(prediction)
result(prediction)