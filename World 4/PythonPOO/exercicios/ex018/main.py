import os
import sqlite3


def adicionar_amigos():
    try:
        amigos = [
            ("Maria", "1995-05-15"),
            ("Pedro", "1988-12-22"),
            ("Ana", "2000-07-30"),
            ("Lucas", "1992-03-10"),
            ("Carla", "1998-11-05"),
            ("Joao", "1990-01-01")
        ]
        cursor.executemany(
            "INSERT INTO amigos (nome, nascimento) VALUES (?, ?)", amigos
        )
        conexao.commit()
        print("Amigos adicionados com sucesso!")
    except Exception as e:
        print("Erro ao adicionar amigos:", e)

busca = input("Digite o nome do amigo que deseja buscar: ").strip()
base_dir = os.path.dirname(os.path.abspath(__file__))
banco_path = os.path.join(base_dir, "meubanco.db")

with sqlite3.connect(banco_path) as conexao:
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS amigos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nascimento TEXT
        )
        """
    )
    conexao.commit()

    if cursor.execute("SELECT COUNT(*) FROM amigos").fetchone()[0] == 0:
        adicionar_amigos()
    total = 0
    cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
    for total, amigo in enumerate(cursor):

        print("Nome:", amigo["nome"], "| Nascimento:", amigo["nascimento"])
    print(f"Total de amigos encontrados: {total}")
