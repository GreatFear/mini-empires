import random

class Nation:

    # Initalizing a Nation Object
    def __init__(self, wood, stone, food, lumbermill, quarry, farm, house, barrack, fort, lumberjack, miner, farmer, current_pop, current_soldiers):
        # Resources
        self.wood = wood
        self.stone = stone
        self.food = food
        
        # Buildings
        self.lumbermill = lumbermill
        self.quarry = quarry
        self.farm = farm
        self.house = house
        self.barrack = barrack
        self.fort = fort
        
        # Population
        self.lumberjack = lumberjack
        self.miner = miner
        self.farmer = farmer
        self.current_pop = current_pop
        self.current_soldiers = current_soldiers
        self.max_population = max_population()

    # Building Buildings
    def build_lumbermill(self):
        if self.wood > 5 and self.stone > 10:
            self.wood -= 5 * amt
            self.stone -= 10 * amt
            self.lumbermill += amt

    def build_quarry(self, amt):
        if self.wood > (10 * amt) and self.stone > (5 * amt):
            self.wood -= 10 * amt
            self.stone -= 10 * amt
            self.quarry += amt

    def build_house(self, amt):
        if self.wood > (5 * amt) and self.stone > (5 * amt):
            self.wood -= 5 * amt
            self.stone -= 5 * amt
            self.house += amt

    def build_barrack(self, amt):
        if self.wood > (15 * amt) and self.stone > (15 * amt):
            self.wood -= 15 * amt
            self.stone -= 15 * amt
            self.house += amt

    def build_fort(self, amt):
        if self.wood > (25 * amt) and self.stone > (25 * amt):
            self.wood -= 25 * amt
            self.stone -= 25 * amt
            self.fort += amt

    def get_lumbermill(self):
        return self.lumbermill

    def get_quarry(self):
        return self.quarry

    def get_house(self):
        return self.house

    def get_barrack(self):
        return self.barrack

    def get_fort(self):
        return self.fort
            
    # Army related stuff
    def army_attack(self):
        return self.current_soldiers * 5

    def army_defense(self):
        return self.current_soldiers * 7
        
    # Population
    def max_population(self):
        return self.house * 5

    def max_army_size(self):
        return self.barrack * 10

    # Updating Stuff owo
    def update_resource(self):
        self.wood += lumberjack * 3
        self.stone += miner * 3
        self.food += (farmer * 5) - (current_pop * 2)

    def update_population(self):
        ava_pop = self.max_population - self.current_pop
        self.current_pop += pow(current_pop, (ava_pop/(self.max_population * 10) + 1))

        if(self.current_pop > self.max_population):
            self.current_pop = self.max_population
        
    def update_state(self):
        update_resource()
        update_population()
