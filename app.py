import sys 

sys.path.append('/home/rafaelfabrichimidt/Documentos/projetos/python/estudando_orientacao_a_objeto')

from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante



def primeira_parte_curso_poo():

    restaurante_praca = Restaurante('vila', 'padaria')
    restaurante_ali = Restaurante('logo_ali', 'sucos')
    
    restaurante_praca.receber_avaliacao('Rafa', 10)
    restaurante_praca.receber_avaliacao('Rafa', 5)
    restaurante_praca.receber_avaliacao('Rafa', 10)

    restaurante_praca.media_avaliacoes()
    
    Restaurante.listar_restaurantes()
    
    
def segunda_parte_curso_poo():

    restaurante_praca = Restaurante('paozinho', 'padaria')
    bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
    prato_paozinho = Prato('Paozinho', 2.0, 'grande')

    restaurante_praca.adicionar_item_cardapio(bebida_suco)
    restaurante_praca.adicionar_item_cardapio(prato_paozinho)

    print(bebida_suco)
    print(prato_paozinho)

    restaurante_praca.exibir_cardapio

    
if __name__=="__main__":
    
    #primeira_parte_curso_poo()
    
    segunda_parte_curso_poo()