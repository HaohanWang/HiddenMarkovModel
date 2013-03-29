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
	dic["aa"]=0.3
	dic["ab"]=0.7
	dic["bb"]=0.7
	dic["ba"]=0.3
	return dic
