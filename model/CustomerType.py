# I have created this class to support more types of customers in the future

from enum import Enum


class CustomerType(Enum):
    REGULAR = "regular"
    VIP = "vip"
