import pymongo
import pymongo.errors
from faker import Faker

def criarperfil(n):

        client = pymongo.MongoClient(
            "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        print('Banco de dados conectado com sucesso...')

        banco = client["LivrariaDomingos"]
        collection_usuario = banco["Usuários"]

        faker=Faker()

        for i in range(n):
            nome=faker.name()
            email=faker.email()
            collection_usuario.insert_one({

                "nome": f"Usuário {i + 1}",
                "email": f"usuario{i + 1}@guizodasilva.com",
                "livrosLidos": [],
                "livrosFavoritos": [],
                "seguindo": [],
                "seguidores": []
            })


