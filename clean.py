import sys

f = sys.argv[1]

text = [line.strip() for line in open("../data/"+f)]

r = ""

cha = "abcdefghijklmnopqrstuvwxyz"
chA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sp = False

for line in text:
	for c in line:
		if c in cha:
			r=r+c
			sp=False
		elif c in chA:
			r=r+c.lower()
			sp=False
		else:
			if not sp:
				r=r+" "
				sp=True
print r
