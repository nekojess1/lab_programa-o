# todo nó vai ter um dado os filhos do lado esq sao menores ou iguais ao pai e os da direita são maiores que o pai
class No:
    def __init__(self,dado):
        self.dado=dado
        self._pai=None
        self._esquerdo = None
        self._direito= None

    def getDado(self):
        return self.dado

    def getPai(self):
        return self._pai

    def getEsquerdo(self):
        return self._esquerdo

    def getDireito(self):
        return self._direito

    def setDado(self,dado):
        self._dado = dado

    def setPai(self,pai):
        self._pai=pai

    def setEsquerdo(self,esquerdo):
        self._esquerdo= esquerdo

    def setDireito(self,direito):
        self._direito=direito

    def __str__(self):
        return str(str(self.getDado()))

class ArvoreBinaria:
    def __init__(self):
        self._raiz=None

    def getRaiz(self):
        return self._raiz
    def setRaiz(self, raiz):
        self._raiz = raiz

    def isVazia(self):
        return self._raiz is None

    def inserir(self,dado):
        novono= No(dado) # nóq acabei de alocar
        direcao = "esquerda"
        if self.isVazia():
            self._raiz =novono
            return novono
        i = self._raiz
        pai = None # == self._raiz.getPai()
        while i is not None:
            pai = i # pai vai ser sempre o nó raiz anterior
            if dado <= i.getDado():
                i = i.getEsquerdo()
                direcao= True
            else:
                i= i.getDireito()
                direcao = False
        novono.setPai(pai)
        if direcao:
            pai.setEsquerdo(novono)
           
        else:
            
            pai.setDireito(novono)
        return novono



    def minimo(self,no): # errado
        while no is not None:
            if no.getEsquerdo() is None:
                return no
            no = no.getEsquerdo()

    def maximo(self,no): #errado
        while no is not None:
            if no.getDireito() is None:
                return no
            no = no.getDireito()

    def sucessor(self,no):
        if no is not None:
            if no.getDireito() is not None: # se entrar nesse if é pq tem filho direito
                return self.minimo(no.getDireito())
            else:
                pai = no.getPai()
                while pai is not None and pai.getDireito() is no: # enquanto no for filho dir de pai ... sobe
                    no = pai
                    pai = no.getPai()
                return pai

    def antecessor(self,no):
        if no is not None:
            fiesquerdo = no.getEsquerdo()
            if fiesquerdo==None:
                pai = no.getPai()
                while pai is not None and pai.getEsquerdo() is no: # enquanto no for filho esquerdo de pai ... sobe
                    no = pai
                    pai = no.getPai()
                return pai

            else:
                dado = no.getDado()
                fiesquerdo=fiesquerdo.getDado()
                
                if fiesquerdo == dado: # se entrar nesse if é pq tem filho esquerdo
 
                    return self.antecessor(no.getEsquerdo())
                else:
                    return self.maximo(no.getEsquerdo())
        
                

    def buscar(self,no,dado): #função recursiva ... vai procurar um dado em nó (árvore binaria de busca)
        if no is None or dado == no.getDado():
            return no
        else:
            if dado < no.getDado():
                return self.buscar(no.getEsquerdo(),dado)
            else:
                return self.buscar(no.getDireito(), dado)

    def remover(self,dado):
        raiz=self.getRaiz()
        
        if raiz == None:
            return False 
        var = self.buscar(raiz, dado)

        if var ==None:
            return False

        pai = var.getPai()
        filhoD = var.getDireito()
        filhoE = var.getEsquerdo()

        
        if var.getEsquerdo() == None and var.getDireito() == None:
            if pai== None:
                raiz.setDado(None) 
            else:
                if var.getDado()>pai.getDado():
                    pai.setDireito(None)
                else:
                    pai.setEsquerdo(None)

        elif var.getEsquerdo() == None and var.getDireito() != None:
            if pai== None:
                raiz.setDado(filhoD)    
            else:
                if var.getDado()>pai.getDado():
                    pai.setDireito(filhoD)
                else:
                    pai.setEsquerdo(filhoD)
        
        elif var.getEsquerdo() != None and var.getDireito() == None:
            if pai== None:
                raiz.setDado(filhoE)  
            else:    
                if var.getDado()>pai.getDado():
                    pai.setDireito(filhoE)
                    filhoE.setPai(pai)
                else:
                    pai.setEsquerdo(filhoE)
                    filhoE.setPai(pai)

        elif var.getEsquerdo() != None and var.getDireito() != None:
            sucessor=self.sucessor(var)
            if pai== None:
                setRaiz(sucessor)
                raiz.setDado(sucessor) 
            else:
                if var.getDado()>pai.getDado():
                    pai.setDireito(sucessor)
                else:
                    pai.setEsquerdo(sucessor)
            pais=sucessor.getPai()
            sucessor.setEsquerdo(filhoE)
            sucessor.setDireito(filhoD)
            if sucessor.getDado()>pais.getDado():
                pais.setDireito(None)
            else:
                pais.setEsquerdo(None)


    def inordem(self, no):
        if no != None:
            filhoD = no.getDireito()
            filhoE = no.getEsquerdo()
            self.inordem(filhoE)
            print(no.getDado(),end=" ")
            self.inordem(filhoD)
  
    def preordem(self, no):
        if no != None:
            filhoD = no.getDireito()
            filhoE = no.getEsquerdo()
            print(no.getDado(),end=" ")
            self.preordem(filhoE)
            self.preordem(filhoD)
       
    def posordem(self, no):
        if no != None:    
            filhoD = no.getDireito()
            filhoE = no.getEsquerdo()
            self.posordem(filhoE)
            self.posordem(filhoD)
            print(no.getDado(),end=" ")

    def ant(self,dado):
        raiz=super().getRaiz()
        if raiz == None:
            
            return 0 
        var = super().buscar(raiz, dado)
        if var.getDado()==None:
            return 0
        else:
            return super().antecessor(var)
    





count=1  
while True:
    try:
        print('Caso {}:'.format(count))
        qtd = int(input())
        minhaArvore = ArvoreBinaria()
        count+=1
        for i in range(qtd):
            
            comandos = input().split()

            if comandos[0] == 'A':
                minhaArvore.inserir(int(comandos[1]))

            elif comandos[0] == 'B':
                minhaArvore.remover(int(comandos[1]))

            elif comandos[0] == 'C':
                ant = minhaArvore.ant(int(comandos[1]))
                if ant==None:
                    print('0')
                else:
                    print(ant)

            elif comandos[0] == 'PRE':
                if minhaArvore.isVazia():
                    print('0')
                else:
                    raiz= minhaArvore.getRaiz()
                    minhaArvore.preordem(raiz)
                    print()


            elif comandos[0] == 'IN':
                if minhaArvore.isVazia():
                    print('0')
                else:
                    raiz= minhaArvore.getRaiz()
                    minhaArvore.inordem(raiz)
                    print()

            elif comandos[0] == 'POST':
                if minhaArvore.isVazia():
                    print('0')
                else:
                    raiz= minhaArvore.getRaiz()
                    minhaArvore.posordem(raiz)
                    print()


    except EOFError:
        break