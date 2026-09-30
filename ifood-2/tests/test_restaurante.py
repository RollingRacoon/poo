import pytest
from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida


def test_adicionar_item_invalido_lanca_erro():
    restaurante = Restaurante('Casa da Vovó', 'Comida Caseira', 'Rua das Carmens, Sítio Loko', 3)
    with pytest.raises(ValueError):
        restaurante.adicionar_cardapio('Isso não é um item de cardápio')