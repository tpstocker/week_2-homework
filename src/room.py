class Room:

    def __init__(self, name, capacity, guest_list, playlist, price):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.playlist = []
        self.price = price

    def add_to_guest_list(self, guest):
        self.guest_list.append(guest)
        if len(self.guest_list) >= self.capacity:
            return "There's still space"
        else:
            return "Sorry, no more room!"

    def remove_from_guest_list(self, guest):
        self.guest_list.remove(guest)

    def add_to_playlist(self, song):
        self.playlist.append(song)



