import random


class CulinaryOverlordAndCommanderOfTheSacredFlame:

    def __init__(self, name, specialty, mood = 10, do_i_hate_my_life = False):
        self.do_i_hate_my_life = do_i_hate_my_life
        self.mood = mood
        self.name = name
        self.specialty = specialty

    def cök(self):
        if not self.do_i_hate_my_life:
            qualiteh = random.randint(1, 10) + self.mood
            return qualiteh
        else:
            qualiteh = random.randint(1, 10) + self.mood
            return qualiteh

    def judgy_judges(self, skillz):
        if skillz >= 18:
            self.mood += 5
            print("UwU... 👉👈")
        elif skillz in range(10, 18):
            self.mood += 2
            print("*minecraft villager noise*")
        elif skillz in range(5, 10):
            self.mood -= 2
            print("Nahh..")
        else:
            self.mood -= 5
            print("🤢🤢🤢")

    def weather(self):
        if self.mood >= 8:
            self.do_i_hate_my_life = False

        else: self.do_i_hate_my_life = True


soup_lord = CulinaryOverlordAndCommanderOfTheSacredFlame(
    name="Soupsan (he/him).",
    specialty="Dysphoric Consome",
    mood=12,
    do_i_hate_my_life=False
)


existential_baker = CulinaryOverlordAndCommanderOfTheSacredFlame(
    name="Crumbsworth",
    specialty="Cinnamon Rolls",
    mood=3,
    do_i_hate_my_life=True
)


foamy_mage = CulinaryOverlordAndCommanderOfTheSacredFlame(
    name="Lecster Lecitin",
    specialty="Deconstructed sadness foam",
    mood=7,
    do_i_hate_my_life=False
)


hyper_puff = CulinaryOverlordAndCommanderOfTheSacredFlame(
    name="Macaron McFrenzy",
    specialty="Espresso-infused tartlets",
    mood=15,
    do_i_hate_my_life=True
)


traumatized_demi = CulinaryOverlordAndCommanderOfTheSacredFlame(
    name="Chop Chop",
    specialty="Burnt toast and coping",
    mood=1,
    do_i_hate_my_life=False
)
