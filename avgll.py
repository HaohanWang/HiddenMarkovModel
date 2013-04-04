import HMM
import math

data = [line.strip() for line in open("../data/train.txt")][0]
symbol = 'abcdefghijklmnopqrstuvwxyz '

hmm=HMM.getHMM()

def getLikeliHood(a, b, t, scale, direction):
	#global scale
	c = a*b
	if c>=10e-6:
		return c
	else:
		scale[t]=scale[t-direction]+1
		c*=10e6
		return c
def getTransitionProbability(i, j, hmm):
	key = 10*i+j
	return hmm[2][key]
def getEmissionProbability(s, c, hmm):
	if c==' ':
		c='space'
	return hmm[s][c]

def forward(data, hmm):
	alpha = [[1,0]]
	t = 0
	scale = [0]
	for c in data:
		t+=1
		alpha.append([0,0])
		scale.append(1)
		for j in range(0, 2):
			sumj = 0.0
			for i in range(0,2):
				sumj+=alpha[t-1][i]*getTransitionProbability(i, j, hmm)
			prob = getLikeliHood(sumj,getEmissionProbability(j, c, hmm), t, scale, 1)
			alpha[t][j]=prob
			#print scale[t]
	return (alpha, scale) 
def backward(data, hmm):
	beta = [[0, 0]]
	scale = [1]
	for k in range(len(data)):
		beta.append([0,0])
		scale.append(1)
	beta.append([0, 1])
	scale.append(1)
	t = len(beta)-1
	for k in range(len(data), 0, -1):
		c=data[k-1]
		t-=1
		for i in range(1, -1, -1):
			sumi=0.0
			for j in range(1, -1, -1):
				temp=beta[t+1][j]*getTransitionProbability(i, j, hmm)
				sumi += getLikeliHood(temp, getEmissionProbability(j, c, hmm), t, scale, -1)
			beta[t][i]=sumi
	return (beta, scale)
alpha, scale = forward(data, hmm)
print alpha[len(data)]
loglhdf=math.log(alpha[len(data)][1], 2)+math.log(10e-6, 2)*scale[len(data)]
avgllf = loglhdf/len(data)
print avgllf

beta, scale = backward(data, hmm)
print beta[1]
loglhdb=math.log(beta[1][0], 2)+math.log(10e-6, 2)*scale[1]
avgllb = loglhdb/len(data)
print avgllb
