import sys 

sys.path.append('/home/rafaelfabrichimidt/Documentos/projetos/python/estudando_orientacao_a_objeto')

from modelos.restaurante import Restaurante



def main():

    restaurante_praca = Restaurante('vila', 'padaria')
    restaurante_ali = Restaurante('logo_ali', 'sucos')
    
    restaurante_praca.receber_avaliacao('Rafa', 10)
    restaurante_praca.receber_avaliacao('Rafa', 5)
    restaurante_praca.receber_avaliacao('Rafa', 10)

    restaurante_praca.media_avaliacoes()
    
    Restaurante.listar_restaurantes()


if __name__=="__main__":
    
    main()