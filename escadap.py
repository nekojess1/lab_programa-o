N = int(input())                # Número de pilhas de pedra
soma = 0                        # Soma da quantidade de cubos de pedra
qtd_cubos=input().split()		# Pegar qtd de cubos/pilha
for i in qtd_cubos:				# Fazer a soma da qtd
	soma+=int(i)

last = ((((2*soma)/N)+(N-1))/2) # Pegar o último valor
first = 1+last-N				# Pegar o menor valor 
movimentos=x=0				    # Qtd de movimentos/contador

for j in range(len(qtd_cubos)): # Loop para calcular os passos dados para EP
    if int(first) != first:     # Não pode quebrar tijolo, logo sem ponto flutuante hein
    	x=1
    	break
    x+=(int(qtd_cubos[j]))-(j+first) # Começa do menor para o maior
    if (int(qtd_cubos[j])>j+first):      # Se o valor for maior, tivemos movimento 
        movimentos+=(int(qtd_cubos[j])-(j+first))   # Soma 1 em movimentos

  

if x==0:                               # Se a escada ficou perfeita 
    print(int(movimentos))
else:											
    print('-1')
            
