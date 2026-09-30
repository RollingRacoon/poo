from banco.db import conectar
from models.usuario import Usuario

def tabela_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(200) NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL
        )
    """
    )
    conexao.commit()
    conexao.close()

def criar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO usuarios(nome, email, senha_hash)
    VALUES (%s, %s, %s)
    """, (usuario.nome, usuario.email, usuario._senha_hash))
    conexao.commit()
    id_gerado = cursor.lastrowid
    conexao.close()

    usuario.id = id_gerado
    return id_gerado 

def buscar_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, senha_hash FROM usuarios WHERE email = %s",(email,)
    )
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return None
    id_usuario, nome, email, senha_hash = resultado
    usuario = Usuario(nome, email, senha_hash)
    usuario.id = id_usuario
    return usuario
 

def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM usuarios WHERE id = %s
    """, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado is None:
        return None
    else:
        id_usuario, nome, email, senha_hash = resultado
        usuario = Usuario(nome, email, senha_hash)
        usuario.id = id_usuario
        return usuario