import pymongo
def deletar_interacoes():
        client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_interacoes = banco["Interações"]

        nome_deletar=input('Informe o que deseja deletar, curtida ou comentário: ')

        resultado=collection_interacoes.delete_one({"tipo": nome_deletar})
        if resultado.deleted_count > 0:
                print(f"Sua Interação '{nome_deletar}' foi excluida com sucesso")
        else:
                    print(f"Nenhum dado foi deletado para '{nome_deletar}'.")    
deletar_interacoes()