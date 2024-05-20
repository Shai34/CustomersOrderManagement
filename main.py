from model.Item import Item
from model.RegularOrder import RegularOrder
from model.VipOrder import VipOrder
from model.PaymentType import PaymentType
from model.Customer import Customer
from model.CustomerType import CustomerType
from model.GiftTablecloth import GiftTablecloth
from model. GiftFlowerpot import GiftFlowerpot
from datetime import date


if __name__ == '__main__':

    # Items
    item1 = Item(1, "Laptop", 999.99)
    item2 = Item(2, "Smartphone", 599.99)
    item3 = Item(3, "Tablet", 399.99)
    item4 = Item(4, "Smartwatch", 199.99)
    item5 = Item(5, "Headphones", 149.99)
    item6 = Item(6, "Smartwatch", 100)
    item7 = Item(7, "Coffee Maker", 49.99)
    item8 = Item(8, "Television", 899.99)
    item9 = Item(9, "Blender", 39.99)
    item10 = Item(10, "Vacuum Cleaner", 149.99)
    item11 = Item(11, "Toaster", 29.99)
    item12 = Item(12, "Bed Sheets", 29.99)
    item13 = Item(13, "Coffee Table", 149.99)
    item14 = Item(14, "Cookware Set", 99.99)
    item15 = Item(15, "Exercise Bike", 299.99)
    item16 = Item(16, "Yoga Mat", 19.99)

    # VIP customers
    customer1 = Customer(1, "Alice", "Smith", "alice.smith@example.com", "456 Elm Street", CustomerType.VIP, customer_discount=0.1)
    customer2 = Customer(2, "Emily", "Brown", "emily.brown@example.com", "101 Maple Street", CustomerType.VIP, customer_discount=0.15)
    customer3 = Customer(3, "Sophia", "Martinez", "sophia.martinez@example.com", "303 Cedar Street", CustomerType.VIP)

    # Regular customers
    customer4 = Customer(4, "John", "Doe", "john.doe@example.com", "123 Main Street", CustomerType.REGULAR)
    customer5 = Customer(5, "Bob", "Johnson", "bob.johnson@example.com", "789 Oak Street", CustomerType.REGULAR)
    customer6 = Customer(6, "Michael", "Wilson", "michael.wilson@example.com", "202 Pine Street", CustomerType.REGULAR)

    # VIP orders
    vip_order1 = VipOrder(1, "VIP Order 1", customer1.get_delivery_address, [item4, item13, item16], customer1, PaymentType.CREDIT_CARD,  date(2024, 5, 20))
    vip_order2 = VipOrder(2, "VIP Order 2", customer2.get_delivery_address, [item3, item6, item14], customer2, PaymentType.CASH, date(2024, 5, 21))
    vip_order3 = VipOrder(3, "VIP Order 3", customer3.get_delivery_address, [item1], customer3, PaymentType.CHECK, date(2024, 5, 22))

    # Regulars orders
    regular_order1 = RegularOrder(4, "Regular Order 1", customer4.get_delivery_address, [item12, item11, item15, item10], customer4, PaymentType.CREDIT_CARD, date(2024, 5, 23))
    regular_order2 = RegularOrder(5, "Regular Order 2", customer5.get_delivery_address, [item2, item9], customer5, PaymentType.CASH, date(2024, 5, 24))
    regular_order3 = RegularOrder(6, "Regular Order 3", customer6.get_delivery_address, [item6, item13, item7, item5, item8], customer6, PaymentType.CHECK, date(2024, 5, 25))

    # Gifts
    gift1 = GiftTablecloth()
    gift2 = GiftFlowerpot()

    print("Test1 - Check if the operator '==' checking by the name:")
    print(item1 == item2)
    print(item6 == item4)

    print()
    print("Test2 - Check if favorite list being updated:")
    print("Customer 1 favorite list:")
    customer1.print_favorite_list()
    customer1.add_favorite_item(item8)
    customer1.print_favorite_list()
    customer1.add_favorite_item(item6)
    customer1.print_favorite_list()  # should not be added - same name like item4
    customer1.remove_favorite_item(item13)
    customer1.print_favorite_list()

    print()
    print("Test3 - Check the order total price working:")
    print(f"Order 1 price is: {vip_order1.get_order_total_price}")  # VIP with discount
    print(f"Order 3 price is: {vip_order3.get_order_total_price}")  # VIP no discount
    print(f"order 5 price is: {regular_order2.get_order_total_price}")  # Regular

    print()
    print("Test 5 - Gifts:")
    customer4.take_gift(gift1)
    customer4.open_your_gift()

    customer3.take_gift(gift2)
    customer3.open_your_gift()

    customer5.open_your_gift()

    print()
    print("Test 6 - Error:")
    # Regular customer making VIP order
    vip_order4 = VipOrder(7, "VIP Order 4", customer4.get_delivery_address, [item1], customer4, PaymentType.CHECK, "2024-05-22")

