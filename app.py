from cardapio.sobremesa import Sobremesa
from modelos.restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import bebida
from cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

cafe = bebida("Café", 5.00, "300ml")
cafe.aplicar_desconto()
sanduiche = Prato("Sanduíche", 15.00, "Delicioso sanduíche de frango com alface e tomate")
sanduiche.aplicar_desconto()
bolo = Sobremesa("Bolo de Chocolate", 20.00, "Bolo de chocolate com cobertura de brigadeiro", "Doce", "Grande")
bolo.aplicar_desconto()

restaurante_praca.adicionar_item_ao_cardapio(cafe)
restaurante_praca.adicionar_item_ao_cardapio(sanduiche)
restaurante_praca.adicionar_item_ao_cardapio(bolo)



def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()