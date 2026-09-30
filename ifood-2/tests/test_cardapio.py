import pytest
from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida
from models.cardapio.itemcardapio import ItemCardapio

def test_prato_e_item_cardapio():
    gerson_gamerplays = Prato("Cacetinho", 12.99, "Cacetinho quentinho, chega manteiga derrete!")
    assert isinstance(gerson_gamerplays, ItemCardapio)
    assert gerson_gamerplays._nome == "Cacetinho"
    assert gerson_gamerplays._preco == 12.99
    assert gerson_gamerplays.descricao == "Cacetinho quentinho, chega manteiga derrete!"

def test_exibir_cardapio_restaurante_vazio_nao_quebra(capsys):
    restaurante = Restaurante("Casa da Vovó", "Rua das Carmens, Sítio Loko", "Comida Caseira", 3)
    restaurante.exibir_cardapio()
    saida = capsys.readouterr().out()
    assert "Cardápio do Restaurante: Casa da Vovó" in saida