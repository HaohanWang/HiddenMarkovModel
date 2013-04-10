import HMM
import randomHmm as r
import avgll as a
import checker 

hmm = HMM.getHMM()

data = [line.strip() for line in open("../data/train.txt")][0]

def getXi(data, hmm):
	alpha = a.forward(data, hmm)
	beta = a.backward(data, hmm)
	#likelihood=beta[0][0]
	xi = [[[0,0],[0,0]]]
	beta.append([[1, 0], [1,0]])
	for t in range(len(data)):
		xi.append([[0,0],[0,0]])
	t = 0
	for h in range(len(data)):
		t+=1
		for i in range(0, 2):
			for j in range(0, 2):
				ptrans = a.getTransitionProbability(i, j, hmm)[0]
				if t<len(data)-1:
					pemit = a.getEmissionProbability(j, data[t+1], hmm)[0]
				else:
					pemit = 1
				#temp = a.multiplyProbability(alpha[t][i], ptrans)
				#temp = a.multiplyProbability(temp, pemit)
				#temp = a.multiplyProbability(temp, beta[t+1][j])
				#xi[t][i][j]=a.divideProbability(temp, likelihood)
				#print str(i)+" "+str(j)
				#print xi
				#print xi[t][i][j]
				xi[t][i][j]=alpha[t][i][0]*ptrans*pemit*beta[t+1][j][0]
#				xi[t][i][j]=temp
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
		demo = 0
		for j in range(0, 2):
			nume = 0
			t=0
			for c in data:
				t+=1
				nume+=xi[t][i][j]
				demo+=xi[t][i][j] 
			trans[i*10+j]=nume
#		for j in range(0, 2):
#			trans[i*10+j]=[trans[i*10+j]/demo, 0]
		trans[i*10+0]=[trans[i*10+0]/demo, 0]
		trans[i*10+1]=[1-trans[i*10+0][0], 0]
	for j in range(0, 2):
		demo = 0
		for s in symbol:
			nume=0
			for i in range(0, 2):
				t=0
				for c in data:
					t+=1
					if c == s:
						nume+=xi[t][i][j]
						demo+=xi[t][i][j]
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
					emiA[s]=[emiA[s]/demo, 0]
				else:
					emiA['space']=[emiA['space']/demo, 0]
			else:
				if s!=' ':
					emiB[s]=[emiB[s]/demo, 0]
				else:
					emiB['space']=[emiB['space']/demo, 0]
		if j==0:
			emiA['space']=[1,0]
		else:
			emiB['space']=[1,0]
		for s in symbol:
			if j==0:
				if s!=' ':
					emiA['space'][0]-=emiA[s][0]
			else:
				if s!=' ':
					emiB['space'][0]-=emiB[s][0]
	return (emiA, emiB, trans)
def train(data, hmm):
	change=1
	Avgll=a.getAvgLL(data, hmm)
	while change >10e-4:
		avgll=Avgll
		xi=getXi(data, hmm)
		hmm=reEstimation(xi, data)
		if checker.checkHmm(hmm)==False:
			print "$$$$$$$$$$$$$$$"
			print hmm[0]
			print hmm[1]
			print hmm[2]
			print "$$$$$$$$$$$$$$$"
		Avgll=a.getAvgLL(data, hmm)
		change=(Avgll-avgll)/abs(Avgll)
		print "---------------"
		print "new avgll\told avgll"
		print str(Avgll)+"\t"+str(avgll)
		print "avgll change ratio"
		print change
	return hmm
def run(data):
	hmm=r.randomHmm()
	#hmm=HMM.getHMM()
	hmm=train(data, hmm)

run(data)
