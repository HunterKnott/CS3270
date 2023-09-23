'''Hunter Knott, CS 3270, Utah Valley University'''
from abc import ABC, abstractmethod

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

def main():
    C = Credit('27468324628746', '01/01/2024')
    PP = PayPal('9448098420498')
    WT = WireTransfer('984834347', '8374682764')
    print(C)
    print(PP)
    print(WT)


if __name__ == "__main__":
    main()