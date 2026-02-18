import random

class Parrot:
    def __init__(self, initial_phrase):
        self.phrases = [initial_phrase]
    def learn(self, new_phrase):
        self.phrases.append(new_phrase)    
    def say(self, repeat=1): 
        if not self.phrases:
            print("...")
            return
        chosen_phrase = random.choice(self.phrases) 
        print(" ".join([chosen_phrase]*repeat))   
p = Parrot("Ку-ку!")
p.say()
p.learn("МЯУ!")
p.say(3)
p.learn("ХИ-ХИ!")
p.say(2)