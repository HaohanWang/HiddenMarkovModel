import avgll as a

def checkHmm(hmm):
	trans = hmm[2]
	t = [0.0, 0]
	t = a.addProbability(t, trans[01])
	t = a.addProbability(t, trans[00])
	if checkProbability(t)==False:
		return False
	t = [0.0, 0]
	t = a.addProbability(t, trans[01])
	t = a.addProbability(t, trans[00])
	if checkProbability(t)==False:
		return False	
	symbol = 'abcdefghijklmnopqrstuvwxyz '
	s=[0.0, 0]
	t=[0.0, 0]
	for c in symbol:
		if c ==' ':
			c='space'
		s=a.addProbability(s, hmm[0][c])
		t=a.addProbability(t, hmm[1][c])
	if checkProbability(s)==False or checkProbability(t)==False:
		return False
	return True
	
def checkProbability(p):
	if round(p[0], 4)==1 and p[1]==0:
		return True
	else:
		return False
