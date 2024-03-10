#Heranca 

#a class Prato vai herdar informacoes da classe ItemCardapio
import sys
sys.path.append('/home/rafaelfabrichimidt/Documentos/projetos/python/estudando_orientacao_a_objeto')

from modelos.cardapio.item_cardapio import ItemCardapio


#classe Prato vai utilizar informacoes da classe principal ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        
        #super vai permitir que acess info de outras classes
        super().__init__(nome, preco)
        
        self.descricao = descricao
        
    
    def __str__(self):
        return self._nome