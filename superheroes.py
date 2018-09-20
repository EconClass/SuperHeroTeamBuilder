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
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
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

    def isAlive(self):
        status = list()
        for hero in self.heroes:
            if hero.health > 0:
                status.append(True)
            else: status.append(False)
        if all(status) == True:
            return True
        else: return False

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_hero(self):
        hero_name = input("Name thy hero: ")
        weapon_name = input("Name thy weapon: ")
        ability_name = input("Name of ability: ")
        ability_power = input("Number between 500 and 10000: ")
        ability = Ability(ability_name, ability_power)
        hero = Hero(hero_name)
        weapon = Weapon(weapon_name)
        ar_name = input("Name thy armor: ")
        ar_def = input("Number between 500 and 10000: ")
        armor = Armor(ar_name, ar_def)

        hero.add_ability(ability)
        hero.add_ability(weapon)
        hero.add_armor(armor)
        return hero



    def build_team_one(self, team_name):
        # This method should allow a user to build team one.
        team_name = input("Name thy team: ")
        self.team_one = Team(team_name)
        count = 0
        while count < 3:
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            count += 1


    def build_team_two(self, team):
        # This method should allow user to build team two.
        team_name = input("Name thy team: ")
        self.team_two = Team(team_name)
        count = 0
        while count < 3:
            hero = self.create_hero()
            self.team_two.add_hero(hero)
            count += 1

    def team_battle(self):
        # This method should continue to battle teams until
        # one or both teams are dead.
        while self.team_one.isAlive() == True and self.team_two.isAlive() == True:
            self.team_two.defend(self.team_one)
            self.team_one.attack(self.team_two)
            self.team_one.defend(self.team_two)
            self.team_two.attack(self.team_one)
            self.team_one.update_kills()
            self.team_two.update_kills()

    def show_stats(self):
        # This method should print out the battle statistics
        # including each heroes kill/death ratio.
        print("Team {}".format(team_one.name))
        team_one.stats()
        print("Team {}".format(team_two.name))
        team_two.stats()
