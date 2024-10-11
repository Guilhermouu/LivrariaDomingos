import pymongo
import random
from faker import Faker

def criar_livros(n):
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    banco = client["LivrariaDomingos"]
    collection_livros = banco["Livros"]

    fake = Faker()  # Cria uma instância do gerador Faker

    for i in range(n):
        num_avaliacoes = random.randint(1, 5)
        avaliacoes = [round(random.uniform(1, 5), 2) for _ in range(num_avaliacoes)]
        
        collection_livros.insert_one({
            "titulo": fake.catch_phrase(),  # Gera um título aleatório
            "autor": fake.name(),           # Gera um nome de autor aleatório
            "genero": random.choice(["Ficção", "Não-Ficção", "Fantasia", "Romance"]),
            "editora": fake.company(),      # Gera um nome de editora aleatório
            "avaliacoes": avaliacoes
        })

criar_livros(2)
