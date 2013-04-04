import HMM
import avgll as a

hmm = HMM.getHMM()

data = [line.strip() for line in open("../data/train.txt")][0]

def getXi(data, hmm):
	alpha, scaleA = a.forward(data, hmm)
	beta, scaleB = a.forward(data, hmm)
	likelihood = beta[1][0]
	xi = [[0,0],[0,0]]
	for t in range(len(data)):
		xi.append([[0,0],[0,0]])
	t = 0
	for c in data:
		t+=1
		for i in range(0, 2):
			for j in range(0, 2):
				ptrans = a.getTransitionProbability(i, j, hmm)
				if t<len(data)-1:
					pemit = a.getEmissionProbability(j, data[t+1], hmm)
				else:
					pemit = 0
				xi[t][i][j]=(alpha[t][i]*prans*pemit*beta[t+1][j])/likelihood
	return xi
def reEstimation(xi):
	symbol = 'abcdefghijklmnopqrstuvwxyz '

