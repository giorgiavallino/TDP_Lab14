import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._stores = DAO.getStores()
        self._graph = nx.Graph()
        self._idMapOrders = {}

    def buildGraph(self, storeID):
        self._graph.clear()
        orders = DAO.getNodes(storeID)
        self._graph.add_nodes_from(orders)
        self._createIdMapOrders(orders)

    def _createIdMapOrders(self, listOrders):
        for order in listOrders:
            self._idMapOrders[order.order_id] = order

    def getNumNodes(self):
        return self._graph.number_of_nodes()

