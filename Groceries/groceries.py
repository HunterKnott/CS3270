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
        return (
            f'Customer ID #{self.cust_id}:\n'
            f'{self.name}, ph. {self.phone}, email: {self.email}\n'
            f'{self.street}\n'
            f'{self.city}, {self.state} {self.postal_code}'
        )

    @staticmethod
    def read_customers(fname:str):
        global customers
        lines = file_helper(fname)
        customers = {line[0]: Customer(*line) for line in lines}

@dataclass
class LineItem():
    item_id: str
    qty: int

    def sub_total(self):
        return float(items[self.item_id].price) * int(self.qty)

@dataclass
class Item():
    item_id: str
    description: str
    price: float

    @staticmethod
    def read_items(fname:str):
        global items
        lines = file_helper(fname)
        items = {line[0]: Item(*line) for line in lines}

class Payment(ABC):
    def __init__(self, amount):
        float(amount)
        self.amount = amount

    @abstractmethod
    def __str__(self):
        return f'Amount: ${self.amount}'

class Credit(Payment):
    def __init__(self, card_number, exp_date):
        str(card_number)
        self.__card_number = card_number
        str(exp_date)
        self.__exp_date = exp_date

    def __str__(self):
        return f'Amount: ${self.amount}, Paid by Credit card {self.__card_number}, exp. {self.__exp_date}'

class PayPal(Payment):
    def __init__(self, paypal_id):
        str(paypal_id)
        self.__paypal_id = paypal_id

    def __str__(self):
        return f'Amount: ${self.amount}, Paid by Paypal ID: {self.__paypal_id}'

class WireTransfer(Payment):
    def __init__(self, bank_id, account_id):
        str(bank_id)
        self.__bank_id = bank_id
        str(account_id)
        self.__account_id = account_id

    def __str__(self):
        return f'Amount: ${self.amount}, Paid by Wire Transfer from Bank ID {self.__bank_id}, Account# {self.__account_id}'

@dataclass
class Order():
    order_id: str
    order_date: str
    cust_id: str
    line_items: list[LineItem]
    payment: Payment

    def __str__(self):
        order_header = (
            f'===========================\n'
            f'Order #{self.order_id}, Date: {self.order_date}\n'
            f'{self.payment}\n\n'
            f'{customers[self.cust_id]}\n\n'
            f'Order Details:\n'
        )

        order_item_list = '\n        '.join(
            f'Item {item.item_id}: "{items[item.item_id].description}", {item.qty} @ {items[item.item_id].price}'
            for item in self.line_items
        )
        return order_header + '        ' + order_item_list + '\n\n'

    @property
    def total(self):
        return self.payment.amount

    @staticmethod
    def read_orders(fname:str):
        global orders
        orders = {}
        lines = file_helper(fname)
        order_tuples = [(lines[i], lines[i+1]) for i in range (0, len(lines), 2)]
        for tuple in order_tuples:
            entries = [item.split('-') for item in tuple[0][3:]]
            order_items = [LineItem(entry[0], entry[1]) for entry in entries]
            order_items = sorted(order_items, key=lambda x: x.item_id)

            if tuple[1][0] == '1':
                payment = Credit(tuple[1][1], tuple[1][2])
            elif tuple[1][0] == '2':
                payment = PayPal(tuple[1][1])
            else:
                payment = WireTransfer(tuple[1][1], tuple[1][2])

            payment.amount = "{:.2f}".format(sum(float(item.sub_total()) for item in order_items))
            orders[tuple[0][1]] = Order(tuple[0][1], tuple[0][2], tuple[0][0], order_items, payment)

def file_helper(file_name:str):
    try:
        with open(file_name) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        message = 'The file ' + str(file_name) + ' does not exist'
        print(message)
    lines = [line.split(',') for line in lines]
    return lines

def main():
    Customer.read_customers('customers.txt')
    Item.read_items('items.txt')
    Order.read_orders('orders.txt')

    with open('order_report.txt', 'w') as report_file:
        [report_file.write(str(o)) for o in orders.values()]

if __name__ == "__main__":
    main()