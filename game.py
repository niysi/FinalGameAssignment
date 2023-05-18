from random import randint
from enemies import j
from player import Player, Health_bar
from enemies import Fight1_stats, Fight2_stats, Fight3_stats, Allfights
from storytelling import story_telling
import os
import platform
# Clear console to make our game prettier


def clear_console():
    # """ Detects the operating system and clears the console """
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")


print(story_telling[0])



def Menu(p):
    while True:
        print("1- Continue")
        print("2- Check Statistics")

        n = input("Go Traveller")

        try:

            if n == "1":
                Menu_Fight(p)
            if n == "2":
                # Hasn't finished yet.
                Menu_Statistics(p)
            else:
                print("Will you choose?")
        except (NameError, SyntaxError):
            print("Choose traveller")


def Menu_Fight(p):
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
                Player.hp -= Fight1_stats.dmg
                print(f"You was striked by enemy, your {Player.hp}")
            print("----------------------------------")
            if Allfights[j] == Fight2_stats:
                Fight2_stats.hp = Fight2_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight2_stats.hp}")
                Player.hp -= Fight2_stats.dmg
                print(f"You was striked by enemy, your {Player.hp}")
            print("----------------------------------")

            if Allfights[j] == Fight3_stats:
                Fight3_stats.hp = Fight3_stats.hp - Player.base_dmg
                print(f"You striked the enemy, he has {Fight3_stats.hp}")
                Player.hp -= Fight1_stats.dmg
                print(f"You was striked by enemy, your {Player.hp}")
            print("----------------------------------")

            if n == "2":
                Player.hp += randint(10, 20)
                if Player.hp > 100:
                    Player.hp = 100
                    print(f"You healed {Player.hp}")

        if Player.hp < 0:
            print("Here is end of your story traveller...")
            break
        j = 0
        if Fight1_stats.hp < 0 and j == 0:
            i = 2
            print(story_telling[i])
            j = 1
            break
        if Fight2_stats.hp < 0 and j == 1:
            i = 3
            print(story_telling[i])
            j = 2
            break
        if Fight3_stats.hp < 0 and j == 2:
            i = 4
            print(story_telling[i])
            break

# def Menu_Statistics(p)


Menu(Player)
