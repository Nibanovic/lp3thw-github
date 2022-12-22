class Ass(object):

    def __init__(self):
        print("I've created an ass.")

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.ass = Ass()
        input('>')

    def sing(self):
        for line in self.lyrics:
            print(line)


bday_lyrics = ["Happy birthday to you,",
               "hope you dont get sued",
               "So I'll stop right there."]

BoP_lyrics = ["They rally around tha family",
              "With pockets full of shells"]

happy_Bday = Song(bday_lyrics)

bulls_on_parade = Song(BoP_lyrics)

happy_Bday.sing()
bulls_on_parade.sing()




