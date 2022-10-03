import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('    <-- Cria uma tabela chamada clientes caso nao existir
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'    <-- Cria o Id de cada usuario
#                'nome TEXT,'                                <-- O nome do usuario, e o TEXT ta sendo referenciado como uma str
#                'peso REAL'                                  <-- O peso do usuario, e o REAL ta sendo usuado para registrar um peso em float
#                ')')


# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Roberto', 100))


# as duas tabelas estao sendo usuadas para registrar clientes
#   OBS: se for usar mais de uma linha para inserir o usuario na base de dados, caso nao alterado o nome e o valor do peso sera repetido

# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', ('Angelo', 46))


# conexao.commit()


# cursor.execute('UPDATE clientes SET peso=:peso WHERE id=:id',     <-- É responsavel por dar update nas informações dos usuarios
#                {'peso': 72.63, 'id': 6}
#                )


# conexao.commit()


# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     # aqui ele vai deletar um usuario chamado Test
#     {'id': 7}
# )

# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)

cursor.close()
conexao.close()
