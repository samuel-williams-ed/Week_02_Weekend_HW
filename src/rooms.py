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

    def check_in_guest(self, customer_object):
        #add test to check if there is space in the room
        if self.check_room_has_space():
            customer_object.checked_in = True
            self.guests_list.append(customer_object)
        else: 
            print("This room is full!")
    
    def check_out_guest(self, customer_object):
        customer_object.checked_in = False

    def add_song_to_room(self, song_object):
        self.songs_list.append(song_object)
        return 
    

