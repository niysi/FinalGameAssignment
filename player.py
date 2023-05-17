from items import Sword
from items import Crossbow
from items import Staff


class Player:
    base_dmg = 5
    base_hp = 100
    strength = 1  # demo
    agility = 1  # demo
    faith = 1  # demo
    gold = 0  # demo
# Changes test


class Health_bar:
    health_bar = 20
    health_heart = "O"
    drawhealthbar = Player.base_hp / health_bar
    healthbar = drawhealthbar * health_heart
