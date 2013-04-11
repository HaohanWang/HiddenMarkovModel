import operator
def getHMM():
	text = [line.strip() for line in open("../data/t.txt")]
	symbol = 'abcdefghijklmnopqrstuvwxyz '
	emiA = {}
	emiB = {}
	trans = {}
	for s in symbol:
		if s == ' ':
			s = 'space'
		emiA[s]=(0, 0)
		emiB[s]=(0, 0)
	trans[01]=(0,0)
	trans[00]=(0,0)
	trans[10]=(0,0)
	trans[11]=(0,0)
	probA = text[0][:-2].split('),')
	for item in probA:
		it = item[1:].split(":")
		emiA[it[0][1:-1]]=getProbability(it[1])		
	probB= text[1][:-2].split('),')
	for item in probB:
		it = item[1:].split(":")
		emiB[it[0][1:-1]]=getProbability(it[1])		
	probT= text[2][:-2].split('),')
	for item in probT:
		it = item[1:].split(":")
		trans[int(it[0])]=getProbability(it[1])
#	Alist = sorted(emiA.iteritems(), key=operator.itemgetter(1))
#	Blist = sorted(emiB.iteritems(), key=operator.itemgetter(1))
#	print Alist
#	print Blist
	return (emiA, emiB, trans)
		

def getProbability(line):
	tup = line[2:].split(',')
	return tuple((float(tup[0]), float(tup[1])))

