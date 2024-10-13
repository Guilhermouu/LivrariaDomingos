import pymongo
def deletar_usuario():
        client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_usuario = banco["Usuários"]
      

        nome_deletar=input("Informe o usuário que deseja deletar: ")
            
        resultado=collection_usuario.delete_one({"nome": nome_deletar})
        if  resultado.deleted_count >   0:
            print(f"Usuário '{nome_deletar}' deletado com sucesso.")
        else:
                    print(f"Nenhum dado foi deletado para '{nome_deletar}'.")    
