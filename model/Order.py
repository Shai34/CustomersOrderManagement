from abc import ABC, abstractmethod
from model import PaymentType
from datetime import date


class Order(ABC):

    @abstractmethod
    def __init__(self, order_id, name, delivery_address, list_of_items, order_customer, payment_type: PaymentType, order_date: date):
        self.__order_id = order_id
        self.__name = name
        self.__delivery_address = delivery_address
        self.__list_of_items = list_of_items
        self.__order_customer = order_customer
        self.__payment_type = payment_type
        self.__order_date = order_date

        self.add_items_to_customer_favorites()

    @property
    def get_order_id(self):
        return self.__order_id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_delivery_address(self):
        return self.__delivery_address

    @property
    def get_list_of_items(self):
        return self.__list_of_items

    @property
    def get_order_customer(self):
        return self.__order_customer

    @property
    def get_payment_type(self):
        return self.__payment_type

    @property
    def get_order_date(self):
        return self.__order_date

    @abstractmethod
    def calculate_total_price(self):
        pass

    def add_items_to_customer_favorites(self):
        for item in self.__list_of_items:
            self.__order_customer.add_favorite_item(item)
