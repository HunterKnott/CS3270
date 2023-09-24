'''Hunter Knott, CS 3270, Utah Valley University'''
from abc import ABC, abstractmethod

class Order():
    def __init__(self, order_id, order_date, cust_id, payment):
        str(order_id)
        self.__order_id = order_id
        str(order_date)
        self.__order_date = order_date
        str(cust_id)
        self.__cust_id = cust_id
        # self.__line_items = LineItem()
        self.__payment = payment
    
    def __str__(self):
        return('')
    
    def total():
        # Float, @property
        pass

    # Static read_orders(fname:string)

class Customer():
    def __init__(self, cust_id, name, street, city, state, postal_code, phone, email):
        str(cust_id)
        self.__cust_id = cust_id
        str(name)
        self.__name = name
        str(street)
        self.__street = street
        str(city)
        self.__city = city
        str(state)
        self.__state = state
        str(postal_code)
        self.__postal_code = postal_code
        str(phone)
        self.__phone = phone
        str(email)
        self.__email = email
    
    def __str__(self):
        return('')
    
    # Static read_customers(fname:string)

class LineItem():
    def __init__(self, item_id, qty):
        str(item_id)
        self.__item_id = item_id
        int(qty)
        self.__qty = qty
    
    def sub_total():
        # Float
        pass

class Item():
    def __init__(self, item_id, description, price):
        str(item_id)
        self.__item_id = item_id
        str(description)
        self.__description = description
        float(price)
        self.__price = price
    
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

# Payment can't exist without Order. Order can only have 1 payment, and it needs 1
# Customer can exist without Order. Order can only have 1 customer, and it needs one
# LineItem can't exist without Order. Order can have many line items, and it needs at least 1
# Item can exist without LineItem. LineItem can have many items, and it needs at least 1

def main():
    WT = WireTransfer('63482484', '97432842')
    O = Order('9834792874224', '01/01/2023', '9184384', WT)


if __name__ == "__main__":
    main()