class Jukebox():
    def __init__(self):
        self.songs = []
        self.play_index = None

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def play(self, index):
        return self.songs[index]

    def play_next(self):
        self.play_index += 1

    def shuffle(self):
        self.songs.shuffle()
