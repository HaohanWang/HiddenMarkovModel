tr = [line.strip() for line in open("../data/train.txt")]

a = "aeiouy "
b = "bcdfghjklmnpqrstuvwxz"
dic = {}
pa2b = 1.0
pb2a = 1.0
pa2a = 1.0
pb2b = 1.0
ca2b = 0.0
cb2a = 0.0
ca2a = 0.0
cb2b = 0.0
t=tr[0]
for i in range(len(t)-1):
	if t[i] in a:
		if t[i+1] in a:
			ca2a+=1
		else:
			ca2b+=1		
	else:
		if t[i+1] in a:
			cb2a+=1
		else:
			cb2b+=1
	if t[i] in dic:
		dic[t[i]]+=1
	else:
		dic[t[i]]=1
pa2a = float(ca2a)/float(ca2a+ca2b)
pa2b = float(ca2b)/float(ca2a+ca2b)
pb2a = float(cb2a)/float(cb2a+cb2b)
pb2b = float(cb2b)/float(cb2a+cb2b)
print "trasition probability:"
print str(float(pa2a))+"\t"+str(float(pa2b))
print str(float(pb2a))+"\t"+str(float(pb2b))
print "emission probability"
dica = {}
dicb = {}
ca = 0.0
cb = 0.0
for i in dic:
	if i in a:
		ca+=dic[i]
	else:
		cb+=dic[i]
dicbb = {}
for i in dic:
	if i in a:
		dica[i]=float(dic[i])/float(ca)
	else:
		dicb[i]=float(dic[i])/float(cb)
		dicbb[i]=int(dicb[i]*10000)
for i in dica:
	print str(i)+"\t"+str(dica[i])
for i in dicb:
	print str(i)+"\t"+str(dicb[i])
z = 10000
for i in dicbb:
	z = z - dicbb[i]
	print str(i)+"\t"+str(float(dicbb[i])/10000.0)
print "z"+"\t"+str(float(z)/10000.0)
	
