import pymongo
from faker import Faker
import random

def criar_usuarios(n):
   
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

    
    banco = client["LivrariaDomingos"]
    collection_usuario = banco["Usuários"]
    
    fake = Faker()  

    for i in range(n):
      
        nome = fake.name() 
        email = fake.email() 
        livros_lidos = [fake.catch_phrase() for _ in range(random.randint(1, 5))]  
        livros_favoritos = [fake.catch_phrase() for _ in range(random.randint(1, 5))] 
        seguindo = [f"Usuario{random.randint(1, n)}" for _ in range(random.randint(0, 3))]  
        seguidores = [f"Usuario{random.randint(1, n)}" for _ in range(random.randint(0, 3))]  
        
        # Inserindo o usuário
        collection_usuario.insert_one({
            "nome": nome,
            "email": email,
            "livrosLidos": livros_lidos,
            "livrosFavoritos": livros_favoritos,
            "seguindo": seguindo,
            "seguidores": seguidores            
        })

# Chame a função para criar, por exemplo, 3 usuários
criar_usuarios(3)
