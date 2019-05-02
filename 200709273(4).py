import sys
sys.setrecursionlimit(10000)

def verifica(L,C):

	if L-1>=0:
		if matriz[L-1][C]!='#':
			partes.append(matriz[L-1][C])
			matriz[L-1][C]='#'
			verifica(L-1,C)
				
	if L+1<=N-1:
		if matriz[L+1][C]!='#':
			partes.append(matriz[L+1][C])
			matriz[L+1][C]='#'
			verifica(L+1,C)
			
	if C-1>=0:
		if matriz[L][C-1]!='#':
			partes.append(matriz[L][C-1])
			matriz[L][C-1]='#'
			verifica(L,C-1)
	if C+1<=M-1:
		if matriz[L][C+1]!='#':
			partes.append(matriz[L][C+1])
			matriz[L][C+1]='#'
			verifica(L,C+1)

ovelhas=0
lobos=0

N,M = map(int,input().split())
matriz=[] ;  cercados=[]
for i in range(N):
	a=input()
	lista=[]
	for i in a:
		lista.append(i)
	matriz.append(lista)

for L in range(len(matriz)):
	for C in range(len(matriz[L])):
		partes=[]
		if matriz[L][C] != '#':
			partes.append(matriz[L][C])
			matriz[L][C] = '#'
			verifica(L,C)
			cercados.append(partes)

for x in range(len(cercados)):
	o=0 ; l=0
	for t in range(len(cercados[x])):
		if cercados[x][t] == 'v':
			l+=1
		if cercados[x][t] == 'k':
			o+=1
	if o>l:
		ovelhas+=o
	elif l>o:
		lobos+=l
	elif o==l:
		lobos+=l

print('{} {}'.format(ovelhas,lobos))