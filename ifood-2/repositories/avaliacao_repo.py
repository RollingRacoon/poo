from banco.db import conectar
from models.restaurante import Restaurante
from models.avaliacoes import Avaliacoes

def tabela_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    tabela_avaliacoes = """
        CREATE TABLE IF NOT EXISTS avaliacoes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(100) NOT NULL,
            nota FLOAT(2,1) NOT NULL,
            id_restaurante INT NOT NULL,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
        )
    """
    cursor.execute(tabela_avaliacoes)
    conexao.commit()
    conexao.close()

def criar_avaliacao(id_restaurante, avaliacao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO avaliacoes(id_restaurante, nome_usuario, nota)
    VALUES (%s, %s, %s)
    """, (id_restaurante, avaliacao.cliente, avaliacao.nota))
    conexao.commit()
    conexao.close()

def listar_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT restaurantes.nome, avaliacoes.nome_usuario, avaliacoes.nota FROM avaliacoes
        INNER JOIN restaurantes ON avaliacoes.id_restaurante = restaurantes.id
    """)
    avaliacoes = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return [Avaliacoes (cliente, nota) for cliente, nota in avaliacoes]

def listar_por_restaurante(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM avaliacoes WHERE id_restaurante = %s", (id,))
    resultado = cursor.fetchall()
    conexao.close()
    avaliacoes = []
    for cliente, nota in resultado:
        avaliacoes.append(Avaliacoes(cliente, float(nota)))
    return avaliacoes