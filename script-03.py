s,j='',0
for i in range(1,20):
	s=""
	for j in range(1,i):
		s+=str(j)
		j+j-1
	while j > 0:
		s+=str(j)
		j-=1
	print(s.center(70));