from pymongo import MongoClient
from bson.objectid import ObjectId

class livro:
    def __init__(self, database):
        self.db = database

    def create_livro(self, titulo: str, autor: str, ano: str, preco: int):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"livro criado : {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"book found: {res}")
            return res
        except Exception as e:
            print(f"ocorreu um erro ao encontrar o livro: {e}")
            return None

    def update_livro(self, id: str, titulo: str, autor: str, ano: int, preco:int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "ano": ano, "autor": autor, "preco": preco}})
            print(f"livro atualizado: {res.modified_count}")
            return res.modified_count
        except Exception as e:
            print(f"ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"livro deletado: {res.deleted_count} ")
            return res.deleted_count
        except Exception as e:
            print(f"ocorreu um erro ao delatar o livro: {e}")
            return None