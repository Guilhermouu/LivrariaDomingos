import pymongo
from pymongo import ASCENDING
def criar_indices():
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_usuários = banco["Usuários"]
     
        collection_livros= banco["Livros"]

        collection_livros.create_index([("titulo", ASCENDING), ("avaliacoes.avaliacao", ASCENDING)])
        collection_usuários.create_index([("seguindo", ASCENDING)])

# Criar índices
criar_indices()

print("Índices criados com sucesso.")
    