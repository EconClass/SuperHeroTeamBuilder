import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        hero_attack = 0
        for ablty in self.abilities:
            hero_attack += ablty.attack()
        return hero_attack

    def defend(self):
        # This method should run the defend method on each piece of armor and calculate the total defense.
        #
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.

    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the
        # hero's health.
        #
        # If the hero dies update number of deaths.

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        min_attack = self.attack_strength // 2
        return random.randint(min_attack, self.attack_strength)

    def update_attack(self, attack_strength):
        # Update attack
        self.attack_strength = attack_strength

class Armor:
    def __init__(self, name, defense):
        # Instantiate name and defense strength.
        self.name = name
        self.defense = defense

    def defend(self):
        # Return a random value between 0 and the
        # initialized defend strength.

class Weapon(Ability): # Weapon inherits Ability Template
    # Overide the .attack() from Ability to new .attack() in Weapon
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def find_hero(self, name):
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                return hero      # Returns object
        return 0

    def remove_hero(self, name):
        index = 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.pop(index)
                return
            index += 1
        return 0

    def view_all_heroes(self):
        # Print out all heroes to the console.
        for hero in self.heroes:
            print(hero.name)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack()) ##
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack()) ##
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack()) ##
    weapon = Weapon("Lasso of Truth", 500)
    hero.add_ability(weapon)
    print(hero.attack()) ##
    team = Team("Justice League")
    new_hero = Hero("Batman")
    B_ability = Ability("Master Martial Artist", 700)
    new_hero.add_ability(B_ability)
    print(new_hero.attack()) ##
    weapon = Weapon("Batarangs", 700)
    new_hero.add_ability(weapon)
    print(new_hero.attack()) ##
    team.add_hero(hero)
    team.add_hero(new_hero)
    team.find_hero("Wonder Woman")
    print(team.view_all_heroes()) ##
