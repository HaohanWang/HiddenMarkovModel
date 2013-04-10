import HMM
import bestHMM 
import math

data = [line.strip() for line in open("../data/test1.txt")][0]
symbol = 'abcdefghijklmnopqrstuvwxyz '

#hmm=HMM.getHMM()
hmm=bestHMM.getHMM()
#print hmm

#def getLikeliHood(a, b, t, scale, k, direction):
#	#global scale
#	c = a*b
#	if c>=10e-6 or c==0.0:
#		scale[t][k]=scale[t-direction][k]
#		return c
#	else:
#		scale[t][k]=scale[t-direction][k]+1
#		c*=10e6
#		return c
def multiplyProbability(a, b):
	a = tuple(a)
	b = tuple(b)
	c = [1, 1]
	c[0]=a[0]*b[0]
	c[1]=a[1]+b[1]
	if c[0]>=1e-6 or c[0]==0.0:
		return tuple(c)
	else:
		c[1]+=1
		c[0]*=1e6
		return tuple(c)
def addProbability(a, b):
	a = tuple(a)
	b = tuple(b)
	if a[1]==b[1]:
		c = [a[0]+b[0], a[1]]
		if c[0]>=1e-6 or c[0]==0.0:
			return tuple(c)
		else:
			c[1]+=1
			c[0]*=1e6
			return tuple(c)
	if a[0]==0:
		return b
	if b[0]==0:
		return a
	if a[1]-b[1]>=3:
		return b
	if b[1]-a[1]>=3:
		return a
	if a[1]>b[1]:
		m=b
		n=a
	else:
		m=a
		n=b
	c=[1, 1]
	d=m[1]-n[1]
	e=[n[0]*pow(1e6, d), m[1]]
	c[0]=m[0]+e[0]
	c[1]=m[1]
	if c[0]>=1e-6 or c[0]==0.0:
		return tuple(c)
	else:
		c[1]+=1
		c[0]*=1e6
		return tuple(c)
def divideProbability(a, b):
	a = tuple(a)
	b = tuple(b)
	c = [1, 1]
	if a[0]==0:
		return (0, 0)
	c[0]=a[0]/b[0]
	c[1]=a[1]-b[1]
	while c[0]>10:
		c[1]-=1
		c[0]*=1e-6
	if c[0]>=1e-6 or c[0]==0.0:
		return tuple(c)
	else:
		c[1]+=1
	        c[0]*=1e6
	        return tuple(c)
def compareProbability(a, b):
	if a[1]>b[1]:
		return -1
	elif a[1]<b[1]:
		return 1
	elif a[0]<b[0]:
		return -1
	elif a[0]>b[0]:
		return 1
	else:
		return 0

def getTransitionProbability(i, j, hmm):
	key = 10*i+j
	return hmm[2][key]
def getEmissionProbability(s, c, hmm):
	if c==' ':
		c='space'
	return hmm[s][c]

def forward(data, hmm):
	alpha = [[[1,0],[0,0]]]
	t = 0
	for c in data:
		t+=1
		alpha.append([[0, 0],[0, 0]])
		for j in range(0, 2):
			sumj = [0.0, 0]
			for i in range(0,2):
				ptrans = getTransitionProbability(i, j, hmm)
				sumj = addProbability(sumj, multiplyProbability(alpha[t-1][i], ptrans))
			pemit = getEmissionProbability(j, c, hmm)
			prob = multiplyProbability(sumj, pemit)
#			print prob 
			alpha[t][j]=prob
#		print alpha[t]
		#print scale[t]
	return alpha 
def backward(data, hmm):
	data="#"+data 
	beta = []
	for k in range(len(data)-1):
		beta.append([[0,0],[0,0]])
	beta.append([[1,0],[1,0]])
	t = len(data)-1
	for k in range(len(data), 1, -1):
#		print t
		t-=1
		c=data[t+1]
		#print t
		for i in range(1, -1, -1):
			sumi=[0.0,0]
			for j in range(1, -1, -1):
				#print str(i)+" "+str(j)+" "+str(c)
				ptrans=getTransitionProbability(i, j, hmm)
				temp=multiplyProbability(beta[t+1][j], ptrans)
				pemit=getEmissionProbability(j, c, hmm)
				temp=multiplyProbability(temp, pemit)
				sumi=addProbability(sumi, temp) 
			beta[t][i]=sumi
#		print scale[t]
	data = data[1:]
	return beta
def getAvgLL(data, hmm):
	alpha = forward(data, hmm)
	#print alpha[len(data)][1]
	loglhdf=math.log(alpha[len(data)][1][0], 2)+math.log(1e-6, 2)*alpha[len(data)][1][1]
	avgllf = loglhdf/len(data)
	return avgllf

alpha = forward(data, hmm)
#print alpha[len(data)]
loglhdf=math.log(alpha[len(data)][1][0], 2)+math.log(1e-6, 2)*alpha[len(data)][1][1]
avgllf = loglhdf/len(data)
#print avgllf
print getAvgLL(data, hmm)
#print len(data)

beta = backward(data, hmm)
#print beta[0]
loglhdb=math.log(beta[0][0][0], 2)+math.log(1e-6, 2)*beta[0][0][1]
avgllb = loglhdb/len(data)
#print avgllb
