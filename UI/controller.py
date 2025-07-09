import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # Altro
        self._storeSelezionato = None

    def fillDDStore(self):
        stores = self._model._stores
        for store in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(key=store.store_id,
                                                                   text=store.store_name,
                                                                   data=store,
                                                                   on_click=self.readStore))

    def readStore(self, e):
        self._storeSelezionato = e.control.data

    def handleCreaGrafo(self, e):
        pass

    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
