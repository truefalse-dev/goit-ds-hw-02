import sqlite3


class DbConnection(object):
    _iInstance = None
    class Singleton:
        def __init__(self):
            # add singleton variables here
            self.connection = sqlite3.connect("data.db")
    def __init__( self):
        if DbConnection._iInstance is None:
            DbConnection._iInstance = DbConnection.Singleton()
        self._EventHandler_instance = DbConnection._iInstance

    def __getattr__(self, aAttr):
        return getattr(self._iInstance, aAttr)

    def __setattr__(self, aAttr, aValue):
        return setattr(self._iInstance, aAttr, aValue)
    
    def cursor(self):
        return self.connection