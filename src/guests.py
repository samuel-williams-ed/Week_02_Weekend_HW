class Guest():
    def __init__(self, input_name, input_age, input_money, input_fav_song):
        self.name = input_name
        self.age = input_age
        self.checked_in = False
        self.money = input_money
        self.favourite_song = input_fav_song

# Methods:
    def cheer(self):
        return "Whoo!"