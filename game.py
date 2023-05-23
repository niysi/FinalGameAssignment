from random import randint
import os
import platform
from player import Player, Health_bar
from enemies import Fight1_stats, Fight2_stats, Fight3_stats, Allfights
from storytelling import story_telling
# Clear console to make our game prettier


def clear_console():
    # """ Detects the operating system and clears the console """
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


print(story_telling[0])


# asda
def Menu(p):
    while True:
        print("1- Continue")
        print("2- Check Statistics")

        n = input("Go Traveller: ")

        try:

            if n == "1":
                Menu_Fight(p)
            if n == "2":
                # Hasn't finished yet.
                Menu_Statistics()
            else:
                print("Will you choose?")
        except (NameError, SyntaxError):
            print("Choose traveller")


def Menu_Fight(p):
    j = 0
    i = 1
    while Player.base_hp > 0:
        print(Health_bar.healthbar)
        print(Player.base_hp, "\t", Player.base_dmg)
        print("---------------------")
        print("1 - Strike the enemy")
        # Not realised even close/ should be 2 types of healing
        print("2 - Heal")
        n = input("Choose faster traveller")

        if n == "1":
            if Allfights[j] == Fight1_stats:
                Fight1_stats.hp = Fight1_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight1_stats.hp}")
                Player.base_hp -= Fight1_stats.dmg
                print(f"You was striked by enemy, your {Player.base_hp}")
            print("----------------------------------")
            if Allfights[j] == Fight2_stats:
                Fight2_stats.hp = Fight2_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight2_stats.hp}")
                Player.base_hp -= Fight2_stats.dmg
                print(f"You was striked by enemy, your {Player.base_hp}")
            print("----------------------------------")

            if Allfights[j] == Fight3_stats:
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
            i = 2
            # print(story_telling[i])
            j = 1

        if Fight2_stats.hp < 0 and j == 1:
            i = 3
            # print(story_telling[i])
            j = 2

        if Fight3_stats.hp < 0 and j == 2:
            i = 4
            # print(story_telling[i])


def Menu_Statistics():
    print("This is not working")


# This is not working
Menu(Player)
