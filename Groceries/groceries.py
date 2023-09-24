'''Hunter Knott, CS 3270, Utah Valley University'''
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Customer():
    cust_id: str
    name: str
    street: str
    city: str
    state: str
    postal_code: str
    phone: str
    email: str
    
    def __str__(self):
        return('')
    
    # Static read_customers(fname:string)

@dataclass
class LineItem():
    item_id: str
    qty: int
    
    def sub_total():
        # Float
        pass

@dataclass
class Item():
    item_id: str
    description: str
    price: float
    
    # Static read_items(fname:string)

class Payment(ABC):
    def __init__(self, amount):
        float(amount)
        self.__amount = amount
    
    @abstractmethod
    def __str__(self):
        return f"{self.__amount}"

class Credit(Payment):
    def __init__(self, card_number, exp_date):
        str(card_number)
        self.__card_number = card_number
        str(exp_date)
        self.__exp_date = exp_date
    
    def __str__(self):
        return('')

class PayPal(Payment):
    def __init__(self, paypal_id):
        str(paypal_id)
        self.__paypal_id = paypal_id
    
    def __str__(self):
        return('')

class WireTransfer(Payment):
    def __init__(self, bank_id, account_id):
        str(bank_id)
        self.__bank_id = bank_id
        str(account_id)
        self.__account_id = account_id
    
    def __str__(self):
        return('')

@dataclass
class Order():
    order_id: str
    order_date: str
    cust_id: str
    line_items: LineItem()
    payment: Payment()
    
    def __str__(self):
        return('')
    
    def total():
        # Float, @property
        pass

    # Static read_orders(fname:string)

# Payment can't exist without Order. Order can only have 1 payment, and it needs 1
# Customer can exist without Order. Order can only have 1 customer, and it needs one
# LineItem can't exist without Order. Order can have many line items, and it needs at least 1
# Item can exist without LineItem. LineItem can have many items, and it needs at least 1

def main():
    WT = WireTransfer('63482484', '97432842')
    O = Order('9834792874224', '01/01/2023', '9184384', WT)


if __name__ == "__main__":
    main()