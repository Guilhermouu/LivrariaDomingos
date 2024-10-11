import pymongo
from pymongo import ObjectId
from datetime import datetime

def atualizar_usuario(email):
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    print('Banco de dados conectado com sucesso...')

    banco = client["LivrariaDomingos"]
    collection_usuario = banco["Usuários"]

    # Verifica se o usuário existe
    usuario = collection_usuario.find_one({"email": email})
    if not usuario:
        print("Usuário não encontrado.")
        return

    print("O que você deseja atualizar?")
    print("1. Adicionar livro lido")
    print("2. Outra opção (implementação futura)")

    escolha = input("Escolha uma opção (1/2): ")

    if escolha == "1":
        livro_id = input("Digite o ID do livro: ")
        avaliacao = float(input("Digite a avaliação (0 a 5): "))
        
        resultado = collection_usuario.update_one(
            {"email": email},
            {"$push": {"livrosLidos": {"livroId": ObjectId(livro_id), "avaliacao": avaliacao, "dataLeitura": datetime.now()}}}
        )

        if resultado.modified_count > 0:
            print("Livro lido adicionado com sucesso.")
        else:
            print("Nenhuma alteração foi feita.")
    else:
        print("Opção não implementada.")

# Exemplo de chamada da função
email = input("Digite o e-mail do usuário que deseja atualizar: ")
atualizar_usuario(email)
