import HMM
import randomHmm as r
import avgll as a

hmm = HMM.getHMM()

data = [line.strip() for line in open("../data/train.txt")][0]

def getXi(data, hmm):
	alpha = a.forward(data, hmm)
	beta = a.backward(data, hmm)
	likelihood=beta[0][0]
	xi = [[[[0,0],[0,0]],[[0,0],[0,0]]]]
	beta.append([[1, 0], [1,0]])
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
				temp = a.multiplyProbability(alpha[t][i], ptrans)
				temp = a.multiplyProbability(temp, pemit)
				temp = a.multiplyProbability(temp, beta[t+1][j])
				xi[t][i][j]=a.divideProbability(temp, likelihood)
	return xi
def reEstimation(xi, data):
	symbol = 'abcdefghijklmnopqrstuvwxyz '
	emiA = {}
	emiB = {}
	trans = {}
	for c in symbol:
		if c!=" ":
			emiA[c]=[0.0, 0]
			emiB[c]=[0.0, 0]
		else:
			emiA['space']=[0.0,0]
			emiB['space']=[0.0,0]
	for i in range(0, 2):
		demo = [0, 0]
		for j in range(0, 2):
			nume = [0, 0]
			t=0
			for c in data:
				t+=1
				nume=a.addProbability(nume, xi[t][i][j])
				demo=a.addProbability(demo, xi[t][i][j]) 
			trans[i*10+j]=nume
		for j in range(0, 2):
			trans[i*10+j]=a.divideProbability(trans[i*10+j], demo)
	for j in range(0, 2):
		demo = [0, 0]
		for s in symbol:
			nume=[0,0]
			for i in range(0, 2):
				t=0
				for c in data:
					t+=1
					if c == s:
						nume=a.addProbability(nume, xi[t][i][j])
						demo=a.addProbability(demo, xi[t][i][j])
			if j==0:
				if c!=' ':
					emiA[c]=nume
				else:
					emiA['space']=nume
			else:
				if c!=' ':
					emiB[c]=nume
				else:
				        emiB['space']=nume
		for s in symbol:
			if j==0:
				if c!=' ':
					emiA[c]=a.divideProbability(emiA[c], demo)
				else:
					emiA['space']=a.divideProbability(emiA['space'], demo)
			else:
				if c!=' ':
					emiB[c]=a.divideProbability(emiB[c], demo)
				else:
					emiB['space']=a.divideProbability(emiB['space'], demo)
	return (emiA, emiB, trans)
def train(data, hmm):
	emiA=hmm[0]
	emiB=hmm[1]
	trans=hmm[2]
	avgll=-2
	Avgll=-1
	while (Avgll-avgll)/abs(Avgll)>10e-4:
		avgll=a.getAvgLL(data, hmm)
		xi=getXi(data, hmm)
		hmm=reEstimation(xi, data)
		Avgll=a.getAvgLL(data, hmm)
		print "---------------"
		print str(Avgll)+"\t"+str(avgll)
	return hmm
def run():
	hmm=r.randomHmm()
	hmm=train(data, hmm)

run()
