import avgll as a
import bestHMM

hmm = bestHMM.getHMM()
data = [line.strip() for line in open('../data/decode.txt')][0]

def viterbi(data, hmm):
	alpha = [[[1,0],[0,0]]]
	t = 0
	track = [[],[]]
	for c in data:
		t+=1
		alpha.append([[0, 0],[0, 0]])
		for j in range(0, 2):
			cand = [[0.0, 0],[0.0,0]]
			for i in range(0,2):
				ptrans = a.getTransitionProbability(i, j, hmm)
				cand[i]=a.multiplyProbability(alpha[t-1][i], ptrans)
			if a.compareProbability(cand[0], cand[1])==1:
				better=cand[0]
				track[j].append(0)
			else:
				better=cand[1]
				track[j].append(1)
			pemit = a.getEmissionProbability(j, c, hmm)
			prob = a.multiplyProbability(better, pemit)
#			print prob 
			alpha[t][j]=prob
#		print alpha[t]
		#print scale[t]
	if a.compareProbability(alpha[t][0], alpha[t][1])==1:
		start=0
	else:
		start=1
	s = ''
#	print track[0]
	for i in range(len(track[0])-1, -1, -1):
		if start==0:
			s='A'+s
		else:
			s='B'+s
		start = track[start][i]
	return s
def MLdecode(data, hmm):
	s=''
	for c in data:
		emiA = a.getEmissionProbability(0, c, hmm)
		emiB = a.getEmissionProbability(1, c, hmm)
		if a.compareProbability(emiA, emiB)==1:
			s+='A'
		else:
			s+='B'
	return s

print MLdecode(data, hmm)
