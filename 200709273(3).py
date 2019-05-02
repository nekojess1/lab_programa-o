def verifica(L,C):

	if L-1>=0:
		if matriz[L-1][C]=='#':
			partes.append((L,C+1))
			matriz[L-1][C]='x'
			verifica(L-1,C)
				
	if L+1<=N-1:
		if matriz[L+1][C]=='#':
			partes.append((L+2,C+1))
			matriz[L+1][C]='x'
			verifica(L+1,C)
			
	if C-1>=0:
		if matriz[L][C-1]=='#':
			partes.append((L+1,C))
			matriz[L][C-1]='x'
			verifica(L,C-1)
	if C+1<=M-1:
		if matriz[L][C+1]=='#':
			partes.append((L+1,C+2))
			matriz[L][C+1]='x'
			verifica(L,C+1)

N,M = map(int,input().split())
matriz=[] ;  navios=[]
for i in range(N):
	a=input()
	lista=[]
	for i in a:
		lista.append(i)
	matriz.append(lista)

for L in range(len(matriz)):
	for C in range(len(matriz[L])):
		partes=[]
		if matriz[L][C] == '#':
			partes.append((L+1,C+1))
			matriz[L][C] = 'x'
			verifica(L,C)
			navios.append(partes)
			
jogadas=int(input())
second=navios[:]
for j in range(jogadas):
	L,C=map(int,input().split())
	for x in range(len(navios)):
		for p in range(len(navios[x])):
			if (navios[x][p])==((L,C)):
				del second[x][p]
				break
c=0
for i in second:
	if not i:
		c+=1
print(c)
