import pymongo
from bson.objectid import ObjectId
from datetime import datetime


def atualizar_usuario(email, titulo):
    client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

    banco = client["LivrariaDomingos"]
    collection_usuario = banco["Usuários"]
    collection_livros = banco["Livros"]

    # Verifica se o usuário existe
    usuario = collection_usuario.find_one({"email": email})
    if not usuario:
        print("Usuário não encontrado.")
        return

    # Busca o livro pelo título
    livro = collection_livros.find_one({"titulo": titulo})
    if not livro:
        print("Livro não encontrado.")
        return

    print("O que você deseja atualizar?")
    print("1. Adicionar livro lido")
    print("2. Adicionar nova avaliação")

    escolha = input("Escolha uma opção 1/2: ")

    if escolha == "1":
        livros_lidos=input('Digite os Livros Lidos aqui: ')

        resultado = collection_usuario.update_one(
            {"email": email},
            {"$push": {
                "livrosLidos": livros_lidos, "dataLeitura": datetime.now()
            }}
        )

        if resultado.modified_count > 0:
            print("Livro lido adicionado com sucesso.")
        else:
            print("Nenhuma alteração foi feita.")

    elif escolha == '2':
        avaliacao_livro = float(input("Digite a nova avaliação (0 a 5): "))
       

    # Adiciona nova avaliação
        resultado = collection_livros.update_one(
        {"titulo": titulo},
        {"$push": {
            "avaliacoes": avaliacao_livro    
        }}
        )

   


# Exemplo de chamada da função
email = input("Digite o e-mail do usuário que deseja atualizar: ")
titulo = input("Digite o título do livro: ")
atualizar_usuario(email, titulo)
