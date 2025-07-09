from database.DB_connect import DBConnect
from model.orders import Order
from model.stores import Store

class DAO():

    def __init__(self):
        pass

    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select * 
                from stores s """
        cursor.execute(query,)
        for row in cursor:
            result.append(Store(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(storeID):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select *
                from orders o 
                where o.store_id = %s"""
        cursor.execute(query, (storeID,))
        for row in cursor:
            result.append(Order(**row))
        cursor.close()
        conn.close()
        return result