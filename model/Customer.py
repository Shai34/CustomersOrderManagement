from model.CustomerType import CustomerType
from model.Giftable import Giftable
from model.Item import Item


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type: CustomerType, customer_discount=None, favorite_items=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__delivery_address = delivery_address
        self.__customer_type = customer_type
        self.__customer_discount = customer_discount
        self.__favorite_items = favorite_items if favorite_items is not None else []
        self.__customer_gift = None

    @property
    def get_customer_id(self):
        return self.__customer_id

    @property
    def get_first_name(self):
        return self.__first_name

    @property
    def get_last_name(self):
        return self.__last_name

    @property
    def get_email(self):
        return self.__email

    @property
    def get_delivery_address(self):
        return self.__delivery_address

    @property
    def get_customer_type(self):
        return self.__customer_type

    @property
    def get_customer_discount(self):
        return self.__customer_discount

    @property
    def get_favorite_items(self):
        return self.__favorite_items

    @property
    def get_customer_gift(self):
        return self.__customer_gift

    def add_favorite_item(self, item: Item):
        if isinstance(item, Item):
            if item not in self.__favorite_items:
                self.__favorite_items.append(item)
        else:
            raise TypeError("item should be only from type: 'Item'")

    def remove_favorite_item(self, item: Item):
        if isinstance(item, Item):
            if item in self.__favorite_items:
                self.__favorite_items.remove(item)
        else:
            raise TypeError("item should be only from type: 'Item'")

    def take_gift(self, gift: Giftable):
        if isinstance(gift, Giftable):
            self.__customer_gift = gift

    def open_your_gift(self):
        if self.__customer_gift is not None:
            self.__customer_gift.open_gift()
        else:
            print("You don't have any gift, maybe another day :)")

    def print_favorite_list(self):
        item_list = []
        for item in self.get_favorite_items:
            item_list.append(item.get_name)

        print(item_list)
