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
    
    @staticmethod
    def read_customers(fname:str):
        global customers
        customers = {}
        try:
            with open(fname) as cust_file:
                lines = [line.strip() for line in cust_file.readlines()]
        except FileNotFoundError:
            message = 'The file ' + str(fname) + ' does not exist'
            print(message)
        for line in lines:
            line = line.split(',')
            # Read values to dictionary

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
    
    @staticmethod
    def read_items(fname:str):
        global items
        items = {}

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
    line_items: list[LineItem]
    payment: Payment
    
    def __str__(self):
        return('')
    
    @property
    def total():
        return Payment.amount

    @staticmethod
    def read_orders(fname:str):
        global orders
        orders = {}
        # set payment amount

def main():
    Customer.read_customers('customers.txt')
    Item.read_items('items.txt')
    Order.read_orders('orders.txt')

if __name__ == "__main__":
    main()