import naturalTrain as n


symbol = "abcdefghijklmnopqrstuvwxyz"
def getHMM():
	emiA={}
	emiB={}
	tran={}
	for i in symbol:
		emiA[i]=[0.0,0]
		emiB[i]=[0.0,0]
	emiA['space']=[0.0,0]
	emiB['space']=[0.0,0]
	getA = n.getAProb()
	getB = n.getBProb()
	getT = n.getTrans()
	for i in getA:
		emiA[i]=getA[i]
	for i in getB:
		emiB[i]=getB[i]
	for i in getT:
		tran[i]=getT[i]
	r = (emiA, emiB, tran)
	return r
