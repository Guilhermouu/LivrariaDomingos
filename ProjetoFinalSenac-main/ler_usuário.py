import pymongo 

def ler_usuario(email):
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")


    banco = client["LivrariaDomingos"]
    collection_usuario = banco["Usuários"]

    usuario = collection_usuario.find_one({"email": email})
    return usuario

# Exemplo de chamada da função com um e-mail
email =input("Informe o e-mail que deseja consultar:")  # Substitua pelo e-mail que deseja consultar
usuario = ler_usuario(email)

if usuario:
    print("Usuário encontrado:", usuario)
else:
    print("Usuário não encontrado.")
