from model.Order import Order
from model.PaymentType import PaymentType
from model.CustomerType import CustomerType
from overrides import overrides


class VipOrder(Order):
    def __init__(self, order_id, name, delivery_address, list_of_items, order_customer, payment_type: PaymentType, order_date):
        super().__init__(order_id, name, delivery_address, list_of_items, order_customer, payment_type, order_date)
        self.__order_total_price = self.calculate_total_price()

    @property
    def get_order_total_price(self):
        return self.__order_total_price

    @overrides
    def calculate_total_price(self):
        if isinstance(self.get_order_customer.get_customer_type, CustomerType):
            if self.get_order_customer.get_customer_type == CustomerType.VIP:

                total_price = 0

                for item in self.get_list_of_items:
                    total_price += item.get_price

                if self.get_order_customer.get_customer_discount is not None:
                    price_after_discount = total_price - (total_price * self.get_order_customer.get_customer_discount)
                    return price_after_discount
                else:
                    return total_price

            else:
                raise Exception("Only VIP customer can make VIP orders")

        else:
            raise TypeError("customer_type property should be only from type: 'CustomerType'")
