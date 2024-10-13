import pymongo
def deletar_livro():
        client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_livros = banco["Livros"]

        nome_deletar=input('Informe qual livro deseja deletar: ')

        resultado=collection_livros.delete_one({"titulo": nome_deletar})
        if resultado.deleted_count > 0:
                print(f"Livro '{nome_deletar}' foi excluido com sucesso")
        else:
                    print(f"Nenhum dado foi deletado para '{nome_deletar}'.")    
deletar_livro()