import pymongo
def deletar_usuario():
        client = pymongo.MongoClient(
        "mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_usuario = banco["Usuários"]
        collection_livros = banco["Livros"]

        escolha=input('O que voCê deseja deletar?')
        print('/n1. Usuário')
        print('2.   Livro')
        print('3.   Interação')
        deletar_usuario= input('Informe o que você deseja deletar:')
        if escolha == '1':
            resultado=collection_usuario.delete_one({"Usuários"}: deletar_usuario)

