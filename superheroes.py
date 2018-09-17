import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.abilities = list()

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        hero_attack = 0
        for ablty in self.abilities:
            hero_attack += ablty.attack()
        return hero_attack

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


class Weapon(Ability): # Weapon inherits Ability Template
    # Overide the .attack() from Ability to new .attack() in Weapon
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        # Instantiate resources.
        self.name = team_name
        self.heroes = []

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        if name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if name in self.heroes:
            hero_index = self.heroes.find(name)
            print(self.heroes[hero_index])
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero)

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
