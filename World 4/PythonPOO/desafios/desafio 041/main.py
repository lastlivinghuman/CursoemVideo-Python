import os
import sqlite3
from datetime import datetime

def adicionar_amigos(cursor, conexao):
    try:
        amigos = [
            ("Maria", "1995-05-15"),
            ("Pedro", "1988-12-22"),
            ("Ana", "2000-07-30"),
            ("Lucas", "1992-03-10"),
            ("Carla", "1998-11-05"),
            ("Joao", "1990-01-01")
        ]
        for nome , nascimento in amigos:
           if not nascimento or nascimento == "":
               raise ValueError(f"Data de nascimento inválida para {nome}.")
           
           try:
               datetime.strptime(nascimento, "%Y-%m-%d")
           except ValueError:
                raise ValueError(f"Data de nascimento inválida para {nome}.")
        cursor.executemany(
            "INSERT INTO amigos (nome, nascimento) VALUES (?, ?)", amigos
        )
        conexao.commit()
        print("Amigos adicionados com sucesso!")
        
    except ValueError as ve:
            print("Erro ao adicionar amigos:", ve)
            
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
        adicionar_amigos(cursor, conexao)

    total = 0
    ano_atual = datetime.now().year
    cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))
    for total, amigo in enumerate(cursor, start=1):
        nascimento = datetime.strptime(amigo["nascimento"], "%Y-%m-%d")
        nascimento_formatada = nascimento.strftime("%d/%m/%Y")
        nascimento_ano = nascimento.year
        idade = ano_atual - nascimento_ano
        print("Nome:", amigo["nome"], "| Nascimento:", nascimento_formatada, "| Idade:", idade)

    if total == 0:
        print("Nenhum amigo encontrado.")
    else:
        print(f"Total de amigos encontrados: {total}")
