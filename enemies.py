from random import randint


class Vampire_Thief:
    hp = randint(30, 50)
    dmg = randint(3, 5)


class Vampire_Knight:
    hp = randint(90, 200)
    dmg = randint(9, 15)


class Vampire_LordTheLastboss:
    hp = randint(430, 600)
    dmg = randint(90, 150)

# We have to make random generator for mobes we will have


class Fight1_stats:
    hp = 0
    dmg = 0
    for i in range(0, 3):
        hp += Vampire_Thief.hp
        dmg += Vampire_Thief.dmg


class Fight2_stats:
    hp = 0
    dmg = 0
    for i in range(0, 2):
        hp += Vampire_Thief.hp
        dmg += Vampire_Thief.dmg


class Fight3_stats:
    hp = 0
    dmg = 0
    for i in range(0, 2):
        hp += Vampire_Thief.hp
        dmg += Vampire_Thief.dmg
    hp += Vampire_LordTheLastboss.hp
    dmg += Vampire_LordTheLastboss.dmg


Allfights = [Fight1_stats, Fight2_stats, Fight3_stats]
