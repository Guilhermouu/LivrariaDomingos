import pymongo

def livros_mais_avaliados():
    client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    
    banco = client["LivrariaDomingos"]
    collection_livros = banco["Livros"]
    
    # A agregação retorna um cursor
    cursor = collection_livros.aggregate([
        {"$match": {"avaliacoes": {"$exists": True, "$ne": None}}},  # Filtrar apenas livros com avaliações
        {"$project": {  # Projeta os campos necessários e conta o número de avaliações
            "titulo": 1,
            "numAvaliacoes": {"$size": "$avaliacoes"}  # Conta o número de avaliações
        }},
        {"$sort": {"numAvaliacoes": -1}},  # Ordenar pelo número de avaliações, do maior para o menor
        {"$limit": 5}  # Limita a 5 resultados
    ])
    
    # Converter o cursor para uma lista
    return list(cursor)

# Exibir o resultado
for livro in livros_mais_avaliados():
    print(livro)
