from model.Order import Order
from model.PaymentType import PaymentType
from overrides import overrides


class RegularOrder(Order):
    def __init__(self, order_id, name, delivery_address, list_of_items, order_customer, payment_type: PaymentType, order_date):
        super().__init__(order_id, name, delivery_address, list_of_items, order_customer, payment_type, order_date)
        self.__order_total_price = self.calculate_total_price()

    @property
    def get_order_total_price(self):
        return self.__order_total_price

    @overrides
    def calculate_total_price(self):
        total_price = 0

        for item in self.get_list_of_items:
            total_price += item.get_price

        return total_price
