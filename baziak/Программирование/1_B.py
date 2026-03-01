class Parrot:
    def __init__(self, phrase):
        self.phrase = phrase
    def say(self):
        print(self.phrase)
p1 = Parrot("Ку-ку")
p2 = Parrot("Бэээ")
p1.say()
p2.say()
