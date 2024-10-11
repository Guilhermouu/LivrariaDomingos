from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId



from datetime import datetime
import random

# Conexão com MongoDB Atlas
client = MongoClient("<your_connection_string>")
db = client["rede_social"]

# Coleções
usuarios_collection = db["usuarios"]
livros_collection = db["livros"]
interacoes_collection = db["interacoes"]






# Agregação
def contar_usuarios():
    return usuarios_collection.count_documents({})

def livros_mais_bem_avaliados():
    return livros_collection.aggregate([
        {"$unwind": "$avaliacoes"},
        {"$group": {"_id": "$titulo", "mediaAvaliacoes": {"$avg": "$avaliacoes.avaliacao"}}},
        {"$sort": {"mediaAvaliacoes": -1}},
        {"$limit": 5}
    ])

def autores_mais_seguidos():
    return usuarios_collection.aggregate([
        {"$unwind": "$seguindo"},
        {"$group": {"_id": "$seguindo", "totalSeguidores": {"$sum": 1}}},
        {"$sort": {"totalSeguidores": -1}}
    ])

# Exemplo de uso das agregações
print("Total de usuários:", contar_usuarios())
print("Livros mais bem avaliados:", list(livros_mais_bem_avaliados()))
print("Autores mais seguidos:", list(autores_mais_seguidos()))

# Criação de Índices
def criar_indices():
    livros_collection.create_index([("titulo", ASCENDING), ("avaliacoes.avaliacao", ASCENDING)])
    usuarios_collection.create_index([("seguindo", ASCENDING)])

# Criar índices
criar_indices()

print("Índices criados com sucesso.")
