import sys 
sys.path.append('/home/rafaelfabrichimidt/Documentos/projetos/python/estudando_orientacao_a_objeto')
from modelos.avaliacao import Avaliacao

class Restaurante():
    
    restaurantes = {}

    #metodo construtor __init__
    def __init__(self, nome, categoria):
    
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.ativo = ''
        
        self._avaliacao = []
        
        Restaurante.restaurantes[self.nome] = [self.categoria, self.ativo]
        
        
        
    #self referencia de dados naquele momento
    def __str__(self):
        
        return "{} | {}".format(self.nome, self.categoria)
                    
    
    
    #metodo referenciado a classe e nao a instancia (nao precisamos da instancia de objetos da classe)
    @classmethod
    def listar_restaurantes(cls):
        
        print(cls.restaurantes)
        
            


    def receber_avaliacao(self, cliente, nota):
        
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    def media_avaliacoes(self):
        
        if self._avaliacao is None:
            
            return 0
        
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        
        qtd_notas = len(self._avaliacao)
        
        media = soma / qtd_notas
        
        print(media)        
