class Room():
    def __init__(self, input_number, input_capacity, input_price):
        self.number = input_number
        self.capacity = input_capacity
        self.price = input_price
        self.guests_list = []
        self.songs_list = []
    
    # Methods:
    def return_if_customer_is_checked_in(self, customer_object): #might make more sense to make this a guest method
        return customer_object.checked_in #False value by default

    def check_room_has_space(self):
        if self.capacity > len(self.guests_list):
            return True
        return False

    def check_playlist_for_customer_fav(self, customer_object):
        for song in self.songs_list:
            if song  == customer_object.favourite_song:
                print(customer_object.cheer())
                return True
        return False

    def customer_can_afford(self, customer_object):
        if customer_object.money >= self.price:
            return True
        return False
    
    def charge_customer(self, customer_object):
        customer_object.money -= self.price

    def test_guest_can_check_in(self, customer_object):
        if not self.check_room_has_space():
            print("This room is full!")
            return False
        elif not self.customer_can_afford(customer_object):
            print("Customer can't afford to get in!")
            return False
        return True

    def check_in_guest(self, customer_object):
        if self.test_guest_can_check_in(customer_object):
            customer_object.checked_in = True
            self.guests_list.append(customer_object)
            self.charge_customer(customer_object)
            self.check_playlist_for_customer_fav(customer_object)
    
    def check_out_guest(self, customer_object):
        customer_object.checked_in = False

    def add_song_to_room(self, song_object):
        self.songs_list.append(song_object)
        return 
    

