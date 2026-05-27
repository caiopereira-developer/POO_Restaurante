from modelos.restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

cafe = bebida("Café", 5.00, "300ml")
sanduiche = Prato("Sanduíche", 15.00, "Delicioso sanduíche de frango com alface e tomate")



def main():
    print(cafe)
    print(sanduiche)
    

if __name__ == '__main__':
    main()