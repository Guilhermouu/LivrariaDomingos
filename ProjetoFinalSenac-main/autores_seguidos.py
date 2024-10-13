import pymongo
def autores_mais_seguidos():
        client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")

        banco = client["LivrariaDomingos"]
        collection_usuários = banco["Usuários"]

        cursor= collection_usuários.aggregate([
        {"$unwind": "$seguindo"},
        {"$group": {"_id": "$seguindo", "totalSeguidores": {"$sum": 1}}},
        {"$sort": {"totalSeguidores": -1}}
    ])
        return list(cursor)
print(autores_mais_seguidos())