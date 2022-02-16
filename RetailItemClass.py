class RetailItem:
    
    def __init__(self, description, inventory, price):
        self.__itemdescription = description
        self.__unitsininventory = inventory
        self.__price = price

    def get_description(self):
        return self.__itemdescription

    def get_inventory(self):
        return self.__unitsininventory

    def get_price(self):
        return self.__price
