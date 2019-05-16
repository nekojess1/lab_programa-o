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

    def removerDoInicio(self):

        if not self.isVazia():
            if self._inicio is not self._fim:
                self._inicio.getProx().setAnt(None)
                self._inicio = self._inicio.getProx()
            else:
                self._inicio = self._fim = None

  
class Pilha(ListaEncadeada):

    def inserir(self, dado):
        super().inserirNoInicio(dado)

    def remover(self):
        super().removerDoInicio()

    def vazia(self):
        return super().isVazia()
         
    def pegar_primeiro(self):
        primeiro_elemento = self._inicio.getDado()
        return primeiro_elemento            
        


quantidade=int(input())

for i in range(quantidade):
    caracteres=input()
    validação=True
    expressao2 = Pilha()
    
    for t in caracteres:
        
        if t == ')':
            if (expressao2.vazia()):
                validação=False
                break
            else:
                a=expressao2.pegar_primeiro()
            
                if a=='(':
                    expressao2.remover()
                else:
                    validação=False
                    break
        
        elif t == '}':
            if (expressao2.vazia()):
                validação=False
                break
            else:
                a=expressao2.pegar_primeiro()
                if a=='{':
                    expressao2.remover()
                else:
                    validação=False
                    break
        
        
        
        elif t == ']':
            if (expressao2.vazia()):
                validação=False
                break
            else:
                a=expressao2.pegar_primeiro()
                if a=='[':
                    expressao2.remover()
                else:
                    validação=False
                    break
        

        else:
            expressao2.inserir(t)
            
  	

    val1 = expressao2.isVazia()
   
    if val1 and validação:
        print('S')

    else:
        print('N')