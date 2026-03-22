class Venda:
    def init(self, id_venda, cliente, produto, quantidade, valor_total):
        self.id = int(id_venda)
        self.cliente = cliente
        self.produto = produto
        self.quantidade = int(quantidade)
        self.valor_total = float(valor_total)