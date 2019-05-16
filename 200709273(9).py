class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None
        self.__ant = None

    def getDado(self):
        return self.__dado

    def getProx(self):
        return self.__prox

    def getAnt(self):
        return self.__ant

    def setDado(self, dado):
        self.__dado = dado

    def setProx(self, prox):
        self.__prox = prox

    def setAnt(self, ant):
        self.__ant = ant


class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

    def setInicio(self, inicio):
        self._inicio = inicio

    def setFim(self, fim):
        self._fim = fim

    def buscar(self, dado):
        i = self._inicio
        while i is not None:
            if i.getDado() == dado:
                return i
            i = i.getProx()
        return i #nao achou

    def isVazia(self):
        return self._inicio is None

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if self.isVazia():
            self._inicio = novono
            self._fim = self._inicio
        else:
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
            self._inicio = novono

    def removerDado(self, dado):
        noRemovido = self.buscar(dado) # ponteiro para o resultado da busca
        # o elemento foi encontrado
        if noRemovido is not None:
            prox = noRemovido.getProx()
            ant = noRemovido.getAnt()
            # a lista tinha um elemento
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            # o elemento é o início da lista
            elif noRemovido is self._inicio:
                prox.setAnt(None)
                self._inicio = prox
            # o elemento é o fim da lista
            elif noRemovido is self._fim:
                ant.setProx(None)
                self._fim = ant
            # o elemento está no meio da lista
            else:
                ant.setProx(prox)
                prox.setAnt(ant)
        return noRemovido

    def removerDoInicio(self):
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._inicio.getProx().setAnt(None)
                self._inicio = self._inicio.getProx()
            else:
                self._inicio = self._fim = None

    def removerDoFim(self):
        i = self._fim
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._fim.getAnt().setProx(None)
                self._fim = self._fim.getAnt()
            else:
                self._inicio = self._fim = None
        return i

    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado()) + "|"
            i = i.getProx()
        if s is "":
            s = "Lista vazia coitada"
        return s


class Fila(ListaEncadeada):
    

    def inserir(self, dado):
        super().inserirNoInicio(dado)

    def remover(self):
        return super().removerDoFim()

    
    def vazia(self):
        return super().isVazia()

    def pegar_primeiro(self):
        primeiro_elemento = self._fim.getDado()
        return primeiro_elemento


    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado())
            i = i.getProx()
            if i is not None:
                s += "->"
        if s is "":
            return "É bom ficar sem Fila"
        return "último a chegar-> "+s+"->primeiro a chegar"

festas = int(input())
if festas  > 1 and festas <= 10**5:
    while festas>0:
        lista=[] ; resultado = ''
        baralho = Fila()
        cartas=input().split()

        for i in cartas:
            baralho.inserir(int(i))

        while True:
            cartinhas=Fila()
            a=input().split()
            if int(a[0])==-1:
                break
            for i in a:
                cartinhas.inserir(int(i))
            lista.append(cartinhas)

        x = 1
        while x <=1000:

            if x == 1000:
                resultado=0
                break


            a = baralho.pegar_primeiro()
            for i in lista:
                if i.vazia():
                    x=1000
                    resultado = (lista.index(i))+1
                    break
                b = i.pegar_primeiro()

                if b==a:
                    i.remover()
                else: 
                    i.remover()
                    i.inserir(b)
            baralho.remover()

            baralho.inserir(a)
            x+=1

            if x == 1000:
                resultado=0
                break


    
        print(resultado)
        festas-=1