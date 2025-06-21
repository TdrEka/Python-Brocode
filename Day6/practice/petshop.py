# PETS?


class FluffUnit:

    def __init__(self, name, species, age, onomatopoeia, hunger = 0, moody = 5, playful = True):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.moody = moody
        self.playful = playful
        self.onomatopoeia = onomatopoeia

    def nomnoms(self):
        if self.moody > 5:
            return f"meh.. {self.onomatopoeia}"
        else:
            self.hunger = max(0, self.hunger - 3)
            if self.hunger < 6:
                self.moody = max(0, self.moody - 3)
                if self.moody > 8: self.playful = False
            return f"*devours food with vengeance* {self.onomatopoeia.upper()}!!"

    def patpats(self):
        if self.moody > 5 and not self.playful:
            self.hunger = max(0, self.hunger + 1)
            if self.hunger > 9: self.playful = False
            return f"I'm about to {self.onomatopoeia} yo ass."
        else:
            self.moody = max(0, self.moody - 3)
            if self.moody < 8: self.playful = True
            return f"Pi Ka Ch.. I mean: {self.onomatopoeia}"

    def uokpetto(self):
        if self.playful and self.moody > 5 and self.hunger < 5:
            return "I'm chilling.. "
        else:
            return f"fuck you and your family owner {self.onomatopoeia}"

    def speak(self):
        return f"{self.onomatopoeia} is that what you wanted? you done humiliating me now? can i get back to my cell?"

