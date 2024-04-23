class Pilhas:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def vazia(self):
        return len(self.items) == 0

    def topo(self):
        return self.items[-1]
    
