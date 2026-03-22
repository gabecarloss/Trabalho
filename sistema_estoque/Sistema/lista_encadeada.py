class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Nolista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo_no = No(valor)
        
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo   
            atual.proximo = novo_no


        def buscar_id (self, id):
            atual = self.head 
            while atual:
                if atual.valor.id == id:
                    return atual.valor 
                atual = atual.proximo
            