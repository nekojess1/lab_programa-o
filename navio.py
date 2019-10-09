class Campo:
    def __init__(self):
        self.navio = [] # é uma lista de lists == matriz

    def lerCampo(self, l, i, j, b = False):
        achou = b
        if l[i][j] != '#':
            return
        else:
            if achou == False: #comeca com falso e muda pra vdd pq achou o navio
                achou = True
                self.navio.append([])
            l[i][j] = 'x' # ta mudando o navio hastag pra x
            self.navio[len(self.navio) - 1].append((i, j)) #usou o -1 pq a ultima posicao da lista de navios é um a menos
        
        self.lerCampo(l, i, j + 1, achou)  # direita
        self.lerCampo(l, i - 1, j,achou)  # baixo
        self.lerCampo(l, i, j - 1,achou)  # esquerda
        self.lerCampo(l, i + 1, j,achou)  # cima
        

lc_matriz= input().split() #lc_matriz[0]=linha lc_matriz[1]=coluna
linha, coluna=int(lc_matriz[0]),int(lc_matriz[1])
l,borda_paralela,troca = [],[],"@"
for a in range(coluna+1):
    borda_paralela.append(troca)
l.append(borda_paralela)

for b in range(linha):
    caractere=list(troca+input()+troca)
    l.append(caractere)
l.append(borda_paralela)

campo = Campo()
for i in range(linha + 1):
    for j in range(coluna + 1):
        campo.lerCampo(l, i, j)

lista_tiro=[]
num_tiros=int(input())
for y in range(num_tiros):
    tiro = input().split()
    x = int(tiro[0]), int(tiro[1])
    lista_tiro.append(x)

for i in campo.navio: # i == a 1 navio da lista de navio
    for j in range(len(i)): #j == a posicao dos pedacos do navio
        for k in lista_tiro:
            if k == i[j]: # se a pos tiro == pos do pedaco do navio ele troca pra um X
                i[j]="X"

navios_destruidos=0
for i in campo.navio:
    achou_navio= True
    for j in i:
        if j != "X":
            achou_navio=False # se dentro da lista de pedacos do navio n tiver todos elementos com X ele n achou o navio destruido
            break
    if achou_navio:
        navios_destruidos+=1 #Tudo foi X == navio destruidissimo

print(navios_destruidos)
