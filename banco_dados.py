def conectar_banco():
    import pymongo 
    import pymongo.errors
    try:
        
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
        print('Banco de dados conectado com sucesso...')

        banco = client["LivrariaDomingos"]

        collection_usuario = banco["Usuários"]
        collection_interacoes= banco ["Interações"]
        collection_livros= banco["Livros"]

        return collection_usuario, collection_interacoes, collection_livros
    except pymongo.errors as e:
        print("Foi um Erro aí e deu ruim", e)

