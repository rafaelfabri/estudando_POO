class Restaurante():
    
    #metodo construtor __init__
    def __init__(self, nome, categoria):
    
        self.nome = nome
        self.categoria = categoria
        self.ativo = ''
        
    
restaurante_praca = Restaurante('vila', 'padaria')

print(vars(restaurante_praca))