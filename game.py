from random import randint
import os
import platform
from player import Player, Health_bar
from enemies import Fight1_stats, Fight2_stats, Fight3_stats, Allfights
from storytelling import Story_telling
# Clear console to make our game prettier


def clear_console():
    # Detects the operating system and clears the console
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


print(Story_telling[0])
print(Story_telling[1])


def Menu(p):
    while True:
        if Player.base_hp < 0 and Fight3_stats.hp < 0:
            break
        print("1- Continue")
        print("2- Check Statistics")

        n = input("Go Traveller: ")

        try:

            if n == "1":
                Menu_Fight(Player)
            if n == "2":
                Menu_Statistics(Player)
            else:
                print("Will you choose?")
        except (NameError, SyntaxError):
            print("Choose traveller")


def Menu_Fight(p):
    j = 0

    while True > 0:
        print(Health_bar.healthbar)
        print(Player.base_hp, "\t", Player.base_dmg)
        print("---------------------")
        print("1 - Strike the enemy")
        # Not realised even close/ should be 2 types of healing
        print("2 - Heal")
        n = input("Choose faster traveller")

        if n == "1":
            if Allfights[j] == Fight1_stats:
                Player.base_dmg += randint(5, 10)
                Fight1_stats.hp = Fight1_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight1_stats.hp}")
                Player.base_hp -= Fight1_stats.dmg
                print(f"You was striked by enemy, your {Player.base_hp}")
            print("----------------------------------")
            if Allfights[j] == Fight2_stats:
                Player.base_dmg += randint(20, 30)
                Fight2_stats.hp = Fight2_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight2_stats.hp}")
                Player.base_hp -= Fight2_stats.dmg
                print(f"You was striked by enemy, your {Player.base_hp}")
            print("----------------------------------")

            if Allfights[j] == Fight3_stats:
                Player.base_dmg += randint(100, 200)
                Fight3_stats.hp = Fight3_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight3_stats.hp}")
                Player.base_hp -= Fight1_stats.dmg
                print(f"You was striked by enemy, your {Player.base_hp}")
            print("----------------------------------")

        if n == "2":
            Player.base_hp += randint(100, 200)
            if Player.base_hp > 100:
                Player.base_hp = 100
            print(f"You healed {Player.base_hp}")

        if Player.base_hp < 0:
            print("Here is end of your story traveller...")
            break
        if Fight1_stats.hp < 0 and j == 0:

            print(Story_telling[2])
            print(Story_telling[3])
            print(Story_telling[4])
            print(Story_telling[5])
            j = 1

        if Fight2_stats.hp < 0 and j == 1:

            print(Story_telling[6])
            print(Story_telling[7])
            print(Story_telling[8])
            print(Story_telling[9])

            j = 2

        if Fight3_stats.hp < 0 and j == 2:

            print(Story_telling[10])
            print(Story_telling[11])
            print(Story_telling[12])
            print(Story_telling[13])
            break


def Menu_Statistics(p):
    print(Player.base_hp)
    print(Player.base_dmg)


Menu(Player)
