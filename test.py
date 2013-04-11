import avgll as a
import math
def get(tup):
	return math.log(tup[0], 2)+tup[1]*math.log(1e-6, 2)

m = [[0.1, 0], [0.0003, 0], [0.007, 1], [0.224, 5], [0.33, 2], [0.44, 4]]

for i in m:
	for j in m:
		#print str(i)+"\t/\t"+str(j)+"\t=",
		result = a.divideProbability(i, j)
		#check1 = get(i)-get(j)
		#check2 = get(result)
		#if round(check1, 8)==round(check2,8):
		#	print True
		#else:
		#	print i,
		#	print j,
		#	print result
#
#			print check1,
#			print check2
		result = a.getMaxProbability(i, j)
		print str(i)+"\t \t"+str(j)+"\t=",
		print result
