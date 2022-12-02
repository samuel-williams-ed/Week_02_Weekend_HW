class Bar():
    def __init__(self, input_name, input_cash, input_drinks_list):
        self.name = input_name
        self.cash = input_cash
        self.menu = input_drinks_list

    # Methods:
    def get_drink_price(self, drink_entry): # passed input - {"Beer" : 5.50}
        values_list = list(drink_entry.values()) # values() returns a 'view object' so need to wrap as a list
        return values_list[0]

        # from string drink_name return the dictionary entry (drink_entry)
        # find entry with matching name and return entry at that index
        # may break if no name match!
    def choose_drink(self, drink_name):
        entry_index = 0
        for drink_entry in self.menu:
            if drink_name in drink_entry.keys(): break
            entry_index += 1
        return self.menu[entry_index]

    def charge_customer(self, customer_object, drink_entry):
        amount = self.get_drink_price(drink_entry)
        customer_object.money -= amount
    
