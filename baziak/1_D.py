class Parrot:
    def __init__(self, phrase):
        self.phrase = phrase
    def newtext(self, new_phrase):
        self.phrase = new_phrase    
    def say(self, repeat=1):
        print(" ".join([self.phrase]*repeat))
p = Parrot("Ку-ку")
p.say()
p.newtext("МЯУ!")
p.say(3)