while True:
	n,s,m=map(int,input().split())
	if n==s==m==0: break
	matriz=[]
	for i in range(n):
		matriz.append(input().split())
	passos=input()
	colecionador=0

	for x in range(len(matriz)):
		for i in range(len(matriz[i][0][i])):
			if matriz[i][0][i]=='N':
				pos=[i,0,i]
				direção='N'

			elif matriz[i][0][i]=='S':
				pos=matriz[i][0][i]
				direção='S'


			for i in passos:
				if i == 'F':
					if direção == "N":
						if int(pos[0])-1>=0 and (matriz[int(pos[0])][0][int(pos[2])])!='#':
							if matriz[int(pos[0])][0][int(pos[2])]=='*':
								colecionador+=1
								matriz[int(pos[0])][0][int(pos[2])]='.'
							pos[0]=int(pos[0])-1
							
					elif direção == 'S':
						if int(pos[0])+1<=n and (matriz[int(pos[0])][0][int(pos[2])])!='#':
							if matriz[int(pos[0])][0][int(pos[2])]=='*':
								colecionador+=1
								matriz[int(pos[0])][0][int(pos[2])]='.'
							pos[0]=int(pos[0])+1


					elif direção == 'L':
						if int(pos[2])+1<=m and (matriz[int(pos[1])][0][int(pos[2])])!='#':
							if matriz[int(pos[0])][0][int(pos[2])]=='*':
								colecionador+=1
							matriz[int(pos[0])][0][int(pos[2])]='.'
							pos[0][0][2]=int(pos[0][0][2])+1

					elif direção == 'O':
						if int(pos[2])-1>=0 and (matriz[int(pos[1])][0][int(pos[2])])!='#':
							if matriz[int(pos[0])][0][int(pos[2])]=='*':
								colecionador+=1
							matriz[int(pos[0])][0][int(pos[2])]='.'
							pos[0][0][2]=int(pos[0][0][2])-1

				elif i == 'E':
					direção='O'

				elif i == 'D':  
					direção='L'
