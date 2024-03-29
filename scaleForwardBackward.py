import HMM
import randomHmm as r
import avgll as a
import checker 

hmm = HMM.getHMM()

data = [line.strip() for line in open("../data/trainnew.txt")][0]

def getXi(data, hmm):
	alpha = a.forward(data, hmm)
	beta = a.backward(data, hmm)
	likelihood=beta[0][0]
	xi = [[[[0,0],[0,0]],[[0,0],[0,0]]]]
	for t in range(len(data)-1):
		xi.append([[[0,0],[0,0]],[[0,0],[0,0]]])
	data = '#'+data	
	t = 0
	for h in range(len(data)-1):
		for i in range(0, 2):
			for j in range(0, 2):
				ptrans = a.getTransitionProbability(i, j, hmm)
				pemit = a.getEmissionProbability(j, data[t+1], hmm)
				temp = a.multiplyProbability(alpha[t][i], ptrans)
				temp = a.multiplyProbability(temp, pemit)
				temp = a.multiplyProbability(temp, beta[t+1][j])
				xi[t][i][j]=a.divideProbability(temp, likelihood)
		t+=1
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
			for c in range(len(data)):
				nume=a.addProbability(nume, xi[t][i][j])
				demo=a.addProbability(demo, xi[t][i][j]) 
				t+=1
			trans[i*10+j]=nume
		for j in range(0, 2):
			trans[i*10+j]=a.divideProbability(trans[i*10+j], demo)
	for j in range(0, 2):
		demo = [0, 0]
		for s in symbol:
			nume=[0,0]
			for i in range(0, 2):
				t=0
				for c in range(len(data)):
					if data[t] == s:
						nume=a.addProbability(nume, xi[t][i][j])
						demo=a.addProbability(demo, xi[t][i][j])
					t+=1
			if j==0:
				if s!=' ':
					emiA[s]=nume
				else:
					emiA['space']=nume
			else:
				if s!=' ':
					emiB[s]=nume
				else:
				        emiB['space']=nume
		for s in symbol:
			if j==0:
				if s!=' ':
					emiA[s]=a.divideProbability(emiA[s], demo)
				else:
					emiA['space']=a.divideProbability(emiA['space'], demo)
			else:
				if s!=' ':
					emiB[s]=a.divideProbability(emiB[s], demo)
				else:
					emiB['space']=a.divideProbability(emiB['space'], demo)
	return (emiA, emiB, trans)
def train(data, hmm):
	change=1
	Avgll=a.getAvgLL(data, hmm)
	while change >1e-4:
		avgll=Avgll
		xi=getXi(data, hmm)
		hmm=reEstimation(xi, data)
		Avgll=a.getAvgLL(data, hmm)
		change=(Avgll-avgll)/abs(Avgll)
		#print "---------------"
		#print "current avgll\tformal avgll"
		#print str(Avgll)+"\t"+str(avgll)
		#print "avgll change ratio"
		#print change
	print "-----------------"
	print Avgll
	print hmm[0]
	print hmm[1]
	print hmm[2]
	print '-----------------'
	return hmm
def run(data):
	hmm=r.randomHmm()
	#hmm=HMM.getHMM()
	hmm=train(data, hmm)

for i in range(10):
	run(data)
