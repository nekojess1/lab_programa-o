while True:
	n,s,m=map(int,input().split())
	if n==s==m==0: break
	matriz=[]
	for i in range(n):
		matriz.append(input().split())
	passos=input()

	for x in range(len(matriz)):
		for i in range(len(matriz[i][0][i])):
			if matriz[i][0][i]=='N':
				pos=[i,0,i]
				for i in passos:
					if i == 'F':
						if int(pos[0])-1>=0:
							pos[0]=int(pos[0]-1)
							


					elif i == 'E':


					elif i == 'D':

			elif matriz[i][0][i]=='S':
				pos=matriz[i][0][i]
				for i in passos:
					if i == 'F':
						if int(pos[0])+1<=n:


					elif i == 'E':

					elif i == 'D':

			elif matriz[i][0][i]=='O':
				pos=matriz[i][0][i]
				for i in passos:
					if i == 'F':
						if int(pos[2])-1>=0:


					elif i == 'E':

					elif i == 'D':

			elif matriz[i][0][i]=='L':
				pos=matriz[i][0][i]
				for i in passos:
					if i == 'F':
						if int(pos[2])+1<=n-1:

					elif i == 'E':

					elif i == 'D':


