class Room():
    def __init__(self, input_number, input_capacity, input_price):
        self.number = input_number
        self.capacity = input_capacity
        self.price = input_price
        self.songs_list = []
    
    # Methods:
    def return_if_customer_is_checked_in(self, customer_object): #might make more sense to make this a guest method
        return customer_object.checked_in #False value by default

    def check_in_guest(self, customer_object):
        customer_object.checked_in = True
    
    def check_out_guest(self, customer_object):
        customer_object.checked_in = False

    def add_song_to_room(self, song_object):
        self.songs_list.append(song_object)
        return 
    

