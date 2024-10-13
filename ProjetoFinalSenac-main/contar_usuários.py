import pymongo

def contar_usuarios():
    client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    
    banco = client["LivrariaDomingos"]
    collection_usuario = banco["Usuários"]
    
    return collection_usuario.count_documents({})

# Adicione o print para exibir o resultado
print(contar_usuarios())
