class Parrot:
    def __init__(self, phrase):
        self.phrase = phrase
    def newtext(self, new_phrase):
        self.phrase = new_phrase    
    def say(self):
        print(self.phrase)
p = Parrot("Ку-ку")
p.say()
p.newtext("МЯУ!")
p.say()