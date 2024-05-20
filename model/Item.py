
class Item:
    def __init__(self, item_id, name, price):
        self.__item_id = item_id
        self.__name = name
        self.__price = price

    @property
    def get_item_id(self):
        return self.__item_id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    def __eq__(self, other):
        if isinstance(other, Item):  # To check that I don't compare Item class to another class that has also self.__name property
            return self.__name == other.__name
        return False
