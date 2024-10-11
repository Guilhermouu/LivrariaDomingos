import pymongo
import random
from datetime import datetime

def criar_interacoes(n):
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
     
        banco = client["LivrariaDomingos"]

        collection_usuario = banco["Usuários"]
        collection_interacoes= banco ["Interações"]
        collection_livros= banco["Livros"]
        usuarios = list(collection_usuario.find())
        livros = list(collection_livros.find())
    
        for _ in range(n):
            usuario = random.choice(usuarios)
            livro = random.choice(livros)
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
            collection_interacoes.insert_one({
            "tipo": random.choice(["curtida", "comentario"]),
            "usuario": usuario["_id"],
            "livro": livro["_id"],
            "data": data_atual
        })


criar_interacoes(1)