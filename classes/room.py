class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.inside = []
        self.song_list = []

    def check_in(self, person):
        self.inside.append(person)

    def check_out(self, person):
        self.inside.remove(person)

    def add_song(self, song):
        self.song_list.append(song)
        
   