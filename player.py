from items import Sword
from items import Crossbow
from items import Staff


class Player(object):
    base_dmg = 5
    base_hp = 100
    strength = 1  # demo
    agility = 1  # demo
    faith = 1  # demo
    gold = 0  # demo
# Changes test


class Health_bar(object):
    health_bar = 20
    health_heart = 'O'
    drawhealthbar = int(Player.base_hp / health_bar)
    healthbar = drawhealthbar * health_heart
