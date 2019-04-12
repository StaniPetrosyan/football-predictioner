import csv
from models.neural_network import Net
from models.team import Team
from models.match import Match

# init
network = Net()

all_team = []
team = ["Atalanta", "Parma", "Bologna", "Cagliari", "Chievo Verona", "Frosinone", "Fiorentina", "Genoa", "Inter", "Juventus", "Lazio", "Milan", "Napoli", "Roma", "Sampdoria", "Sassuolo", "Ferrara (SPAL)", "Torino", "Udinese", "Empoli"]	

def avg_overall(lista):
	sum = 0
	for i in range(11):
		sum += int(lista[i])
	return sum/11

def encoding(team):
	lista = []
	with open('CompleteDataset.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			if row[8] == team and len(lista) < 11:
				lista.append(row[6])
	
	all_team.append(Team(t, float(avg_overall(lista) / 10.0)))


for t in team:
	encoding(t)

## ----- end init ------

def getTeam(name):
	for l in range(20):
		if name == all_team[l].name:
			return all_team[l]
	return -1

def getOverall(name):
	return getTeam(name).overall

#dataset = [ [getOverall("Juventus"), getOverall("Cagliari"), 0], [getOverall("Hellas Verona"), getOverall("Napoli"), 1], [getOverall("Atalanta"), getOverall("Roma"), 1], [getOverall("Sassuolo"), getOverall("Genoa"), 0.5], [getOverall("Lazio"), getOverall("Ferrara (SPAL)"), 0.5], [getOverall("Crotone"), getOverall("Milan"), 1], [getOverall("Sampdoria"), getOverall("Benevento Calcio"), 0], [getOverall("Bologna"), getOverall("Torino"), 0.5], [getOverall("Udinese"), getOverall("Chievo Verona"), 1], [getOverall("Inter"), getOverall("Fiorentina"), 0], [getOverall("Genoa"), getOverall("Juventus"), 1], [getOverall("Benevento Calcio"), getOverall("Bologna"), 1], [getOverall("Roma"), getOverall("Inter"), 1], [getOverall("Torino"), getOverall("Sassuolo"), 0], [getOverall("Chievo Verona"), getOverall("Lazio"), 1], [getOverall("Milan"), getOverall("Cagliari"), 0], [getOverall("Fiorentina"), getOverall("Sampdoria"), 1], [getOverall("Crotone"), getOverall("Hellas Verona"), 0.5], [getOverall("Ferrara (SPAL)"), getOverall("Udinese"), 0], [getOverall("Napoli"), getOverall("Atalanta"), 0] ]
juve_data = [ [getOverall("Chievo Verona"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Lazio"), 0], [getOverall("Parma"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Sassuolo"), 0], [getOverall("Frosinone"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Bologna"), 0], [getOverall("Juventus"), getOverall("Napoli"), 0], [getOverall("Udinese"), getOverall("Juventus"), 0], [getOverall("Juventus"), getOverall("Genoa"), 0], [getOverall("Empoli"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Cagliari"), 0], [getOverall("Milan"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Juventus"), 0], [getOverall("Fiorentina"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Inter"), 0], [getOverall("Torino"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Roma"), 0], [getOverall("Atalanta"), getOverall("Juventus"), 0.5], [getOverall("Juventus"), getOverall("Sampdoria"), 0], [getOverall("Bologna"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Chievo Verona"), 0], [getOverall("Lazio"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Parma"), 0.5], [getOverall("Sassuolo"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Frosinone"), 0], [getOverall("Bologna"), getOverall("Juventus"), 1], [getOverall("Napoli"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Udinese"), 0], [getOverall("Genoa"), getOverall("Juventus"), 0], [getOverall("Juventus"), getOverall("Empoli"), 0], [getOverall("Cagliari"), getOverall("Juventus"), 1], [getOverall("Juventus"), getOverall("Milan"), 0] ]
spal_data = [ [getOverall("Bologna"), getOverall("Ferrara (SPAL)"), 1], [getOverall("Ferrara (SPAL)"), getOverall("Parma"), 0], [getOverall("Torino"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Atalanta"), 0], [getOverall("Fiorentina"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Sassuolo"), 1], [getOverall("Sampdoria"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Inter"), 1], [getOverall("Roma"), getOverall("Ferrara (SPAL)"), 1], [getOverall("Ferrara (SPAL)"), getOverall("Frosinone"), 1], [getOverall("Lazio"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Cagliari"), 0.5], [getOverall("Juventus"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Empoli"), 0.5], [getOverall("Genoa"), getOverall("Ferrara (SPAL)"), 0.5], [getOverall("Ferrara (SPAL)"), getOverall("Chievo Verona"), 0.5], [getOverall("Napoli"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Udinese"), 0.5], [getOverall("Milan"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Bologna"), 0.5], [getOverall("Parma"), getOverall("Ferrara (SPAL)"), 1], [getOverall("Ferrara (SPAL)"), getOverall("Torino"), 0.5], [getOverall("Atalanta"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Fiorentina"), 1], [getOverall("Sassuolo"), getOverall("Ferrara (SPAL)"), 0.5], [getOverall("Ferrara (SPAL)"), getOverall("Sampdoria"), 1], [getOverall("Inter"), getOverall("Ferrara (SPAL)"), 0], [getOverall("Ferrara (SPAL)"), getOverall("Roma"), 0], [getOverall("Frosinone"), getOverall("Ferrara (SPAL)"), 1], [getOverall("Ferrara (SPAL)"), getOverall("Lazio"), 0], [getOverall("Cagliari"), getOverall("Ferrara (SPAL)"), 0] ]

w1, w2, b = network.train(juve_data, 1000, 0.1)
w3, w4, b2 = network.train(spal_data, 1000, 0.1)


match = [getOverall("Juventus"), getOverall("Ferrara (SPAL)")]
z = w1 * match[0] + w4 * match[1] + (b + b2)
prediction = network.sigmoide(z)
network.result(prediction)

match = [getOverall("Ferrara (SPAL)"), getOverall("Juventus")]
z = w3 * match[0] + w2 * match[1] + (b + b2)
prediction = network.sigmoide(z)
network.result(prediction)

	