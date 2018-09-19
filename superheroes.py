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

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        hero_attack = 0
        for ablty in self.abilities:
            hero_attack += ablty.attack()
        return hero_attack

    def defend(self):
        hero_defend = 0
        if self.health is not 0:
            for armr in self.armors:
                hero_defend += armr.defend()
            return hero_defend
        else: return 0

    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1
        else: return self.health

    def add_kill(self, num_kills):
        self.kills += num_kills

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
        self.name = name
        self.defense_strength = defense

    def defend(self):
        return random.randint(0, self.defense_strength)


class Weapon(Ability):
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

    def attack(self, other_team):
        total_attack = 0
        kills = 0
        for hero in self.heroes:
            total_attack += hero.attack()
            kills = other_team.defend(total_attack)
            hero.add_kill(kills)
        return

    def defend(self, damage_amt):
        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()

        damage_taken = total_defense - damage_amt
        if damage_taken > 0:
            return None
        else:
            damage_taken = -damage_taken

        return self.deal_damage(damage_taken)

    def deal_damage(self, damage):
        div_damage = damage // len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(div_damage)
        return self.update_kills()

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            kdr = hero.kills / hero.deaths
            print("{} has a kill to death ratio of {}".format(hero.name, kdr))

    def update_kills(self):
        dead_heroes = 0
        for hero in self.heroes:
            if hero.health <= 0:
                dead_heroes += 1
        return dead_heroes
