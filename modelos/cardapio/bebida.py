#Heranca

#a class Prato vai herdar informacoes da classe ItemCardapio
import sys
sys.path.append('/home/rafaelfabrichimidt/Documentos/projetos/python/estudando_orientacao_a_objeto')

from modelos.cardapio.item_cardapio import ItemCardapio


#classe Prato vai utilizar informacoes da classe principal ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        
        #super vai permitir que acess info de outras classes
        super().__init__(nome, preco)
        
        self.tamanho = tamanho
        
    def __str__(self):
        return self._nome