data1 = [line.strip() for line in open("../data/An.prob")]
data2 = [line.strip() for line in open("../data/Bn.prob")]
def getAProb():
	dic = {}
	for line in data1:
		item = line.split()
		dic[item[0]]=float(item[1])
	return dic
def getBProb():
	dic = {}
	for line in data2:
		item = line.split()
		dic[item[0]]=float(item[1])
	return dic
def getTrans():
	dic = {}
	dic[00]=0.3
	dic[01]=0.7
	dic[11]=0.7
	dic[10]=0.3
	return dic
