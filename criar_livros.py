import pymongo
import pymongo.errors
import random
def criar_livros(n):
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_livros = banco["Livros"]

        for i in range(n):
            collection_livros.insert_one({
            "titulo": f"Livro {i + 1}",
            "autor": f"Autor {random.randint(1, 10)}",
            "genero": random.choice(["Ficção", "Não-Ficção", "Fantasia", "Romance"]),
            "editora": f"Editora {random.randint(1, 5)}",
            "avaliacoes": []
        })