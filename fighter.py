import random


class Fighter:
    def __init__(self, name, description, current_hit_points,
                 max_hit_points, min_damage, max_damage, image):
        self.name = name
        self.description = description
        self.current_hit_points = current_hit_points
        self.max_hit_points = max_hit_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.image = image
        self.stole_soul = False
        self.num_of_potions = 1

    def attack(self):
        attack_strength = random.randint(self.min_damage, self.max_damage)
        return attack_strength

    def heal(self):
            self.current_hit_points = self.max_hit_points
            return True

    def is_alive(self):
        if self.current_hit_points > 0:
            return True
        else:
            return False
