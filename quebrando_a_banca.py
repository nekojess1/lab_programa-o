while True:
	try:
		a,b=map(int,input().split())    
		numeros=input()
		lista=[]                               # lista para guardar os numeros
		for x in numeros:lista.append(x)       # transforma os números em lista
		resultado=[]                           # lista dos resultados 
		x=a-b-1                                # Índice limite da lista percorrida
		while True:
			if x==-1:                          # Quando o programa percorre a lista todinha
				break
			if x==0:
				lista1=lista[:]                # o resto da lista
			else:
				lista1=lista[:-x]              # lista de tal indice até x
			lista1.sort()                      # ordenação da lista
			a=lista1[-1]                       # maior número dessa lista
			resultado.append(a)                # adicionando o número ao resultado
			del(lista[0:lista.index(a)+1])     # excluindo números inutilizaveis 
			x-=1 							   # Outro índice limite
			
		final=''                               # variável do resultado
		for i in resultado:final+=i            # conversão para string
		print(final)                           # exibe o resultado

	except EOFError:
		break