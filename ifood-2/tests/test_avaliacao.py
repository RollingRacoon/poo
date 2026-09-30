import pytest
from models.avaliacoes import Avaliacoes

def test_avaliacao_esta_certa():
    avaliacao = Avaliacoes("Gerson", 5.0)
    assert avaliacao._cliente == "Gerson"
    assert avaliacao._nota == 5.0