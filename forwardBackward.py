import HMM
import avgll as a

hmm = HMM.getHMM()

data = [line.strip() for line in open("../data/train.txt")][0]

def getXi(data, hmm):
	alpha = a.forward(data, hmm)
	beta = a.backward(data, hmm)
	likelihood=beta[0][0]
	xi = [[[[0,0],[0,0]],[[0,0],[0,0]]]]
	for t in range(len(data)):
		xi.append([[[0,0],[0,0]],[[0,0],[0,0]]])
	t = 0
	for c in data:
		t+=1
		for i in range(0, 2):
			for j in range(0, 2):
				ptrans = a.getTransitionProbability(i, j, hmm)
				if t<len(data)-1:
					pemit = a.getEmissionProbability(j, data[t+1], hmm)
				else:
					pemit = [0, 0]
				temp = a.multiplyProbability(alpha[t][i], prans)
				temp = a.multiplyProbability(temp, pemit)
				temp = a.multiplyProbability(temp, beta[t+1][j])
				xi[t][i][j]=a.divideProbability(temp, likelihood)
	return xi
def reEstimation(xi, data):
	symbol = 'abcdefghijklmnopqrstuvwxyz '
	emiA = {}
	emiB = {}
	trans = {}
	for i in range(0, 2):
		demo = [0, 0]
		for j in range(0, 2):
			nume = [0, 0]
			t=0
			for c in data:
				t+=1
				nume=a.addProbability(nume, xi[t, i, j])
				demo=a.addProbability(nume, xi[t, i, j])
			trans[i*10+j]=nume
		for j in range(0, 2):
			trans[i*10+j]=a.divideProbability(trans[i*10+j], demo)
	
		
