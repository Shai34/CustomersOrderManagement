from enum import Enum


class PaymentType(Enum):
    CREDIT_CARD = "credit_card"
    CASH = "cash"
    CHECK = "check"
    OTHER = "other"
