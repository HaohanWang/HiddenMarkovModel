import random as r

symbol = "abcdefghijklmnopqrstuvwxyz "

def randomHmm():
	emiA = {}
	emiB = {}
	trans = {}
	p=r.random()
	trans[00]=[p, 0]
	trans[01]=[1-p, 0]
	p=r.random()
	trans[10]=[p, 0]
	trans[11]=[1-p, 0]
	s1=0.0
	s2=0.0
	for c in symbol:
		if c == " ":
			c='space'
		emiA[c]=r.randint(1, 100)
		emiB[c]=r.randint(1, 100)
		s1+=emiA[c]
		s2+=emiB[c]
	for c in symbol:
		if c==" ":
			c='space'
		emiA[c]=[float(emiA[c])/float(s1), 0]
		emiB[c]=[float(emiB[c])/float(s2), 0]
	return (emiA, emiB, trans)

