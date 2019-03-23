import math as mt
import random as rd
import csv

rd.seed(1)

lista = []
team = ["Atalanta", "Benevento Calcio", "Bologna", "Cagliari", "Chievo Verona", "Crotone", "Fiorentina", "Genoa", "Inter", "Juventus", "Lazio", "Milan", "Napoli", "Roma", "Sampdoria", "Sassuolo", "Ferrara (SPAL)", "Torino", "Udinese", "Hellas Verona"]
overall_list = []

def control_team(current_team, team, name, overall):
	if current_team == team and len(lista) < 11:
		lista.append(overall)
		
def team_overall(lista):
	i = 0
	sum = 0
	while i < 11:
		sum += int(lista[i])
		i += 1
		
	return sum/11

def encoding(team):
	lista.clear()
	#enconding molto importante
	i = 0
	with open('CompleteDataset.csv', encoding='utf8') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			control_team(row[8], t, row[1], row[6])
			i += 1

class Team:
	def __init__(self, name, overall):
		self.name = name
		self.overall = overall
		
class Match:
	def __init__(self, home, away, result):
		self.home = home
		self.away = away
		self.result = result

def contains(name):
	for l in all_team:
		if name == l.name:
			return l.overall/10
	return 0

def RN(m1, m2):
	t = m1*w1 + m2*w2 + b
	return sigmoide(t)
	
def sigmoide(t):
	return 1 / (1 + mt.exp(-t))
	
w1 = rd.random()
w2 = rd.random()
b = rd.random()

all_team = []
for t in team:
	encoding(t)
	all_team.append(Team(t, int(team_overall(lista))))
	
for all in all_team:
	print(all.name, all.overall)
	
dataset = [ [contains("Juventus"), contains("Cagliari"), 0], [contains("Hellas Verona"), contains("Napoli"), 1], [contains("Atalanta"), contains("Roma"), 1], [contains("Sassuolo"), contains("Genoa"), 0.5], [contains("Lazio"), contains("Ferrara (SPAL)"), 0.5], [contains("Crotone"), contains("Milan"), 1], [contains("Sampdoria"), contains("Benevento Calcio"), 0], [contains("Bologna"), contains("Torino"), 0.5], [contains("Udinese"), contains("Chievo Verona"), 1], [contains("Inter"), contains("Fiorentina"), 0], [contains("Genoa"), contains("Juventus"), 1], [contains("Benevento Calcio"), contains("Bologna"), 1], [contains("Roma"), contains("Inter"), 1], [contains("Torino"), contains("Sassuolo"), 0], [contains("Chievo Verona"), contains("Lazio"), 1], [contains("Milan"), contains("Cagliari"), 0], [contains("Fiorentina"), contains("Sampdoria"), 1], [contains("Crotone"), contains("Hellas Verona"), 0.5], [contains("Ferrara (SPAL)"), contains("Udinese"), 0], [contains("Napoli"), contains("Atalanta"), 0] ]

def sigmoide_p(t):
	return sigmoide(t) * (1 - sigmoide(t))
	
def train():
	w1 = rd.random()
	w2 = rd.random()
	b = rd.random()
	
	iterazioni = 1000
	learning_rate = 0.1
	
	for i in range(iterazioni):
		ri = rd.randint(0, len(dataset) - 1)
		point = dataset[ri]
		
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
		
w1, w2, b = train()

match = [contains("Juventus"), contains("Genoa")]
# molto avvantaggiate le squadre fuori casa, forse perché mancano giornate nel dataset fra
print(contains("Juventus"), contains("Genoa"))
z = w1 * match[0] + w2 * match[1] + b
prediction = sigmoide(z)
print(prediction)


#pred = []
#for partita in dataset:
#	z = w1 * partita[0] + w2 * partita[1] + b
#	prediction = sigmoide(z)
#	print(prediction)
	
if prediction < 0.33:
	print("vittoria in casa")
elif prediction < 0.66:
	print("pareggio")
else:
	print("vittoria fuori casa")
		
#print(pred)