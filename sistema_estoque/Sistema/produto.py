class Produto:

    def __init__(self, id_produto, nome, quantidade, preco):
        self.id = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __repr__(self):
        return f"Produto(id={self.id!r}, nome={self.nome!r}, quantidade={self.quantidade}, preco={self.preco})"

    def cadastrar_produto(self, lista_produtos):
        lista_produtos.inserir(self)
    
    def listar_produtos(self, lista_produtos):
        produtos = []
        atual = lista_produtos.head
        while atual:
            produtos.append(atual.valor)
            atual = atual.proximo
        return produtos

    def vendas_realizadas(self, lista_vendas):
        vendas = []
        atual = lista_vendas.head
        while atual:
            venda = atual.valor
            if venda.produto.id == self.id:
                vendas.append(venda)
            atual = atual.proximo
        return vendas

    def quantidade_de_produtos(self, lista_vendas):
        total = 0
        atual = lista_vendas.head
        while atual:
            venda = atual.valor
            if venda.produto.id == self.id:
                total += venda.quantidade
            atual = atual.proximo
        return total