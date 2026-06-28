# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alex <alex@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 18:51:57 by alex              #+#    #+#              #
#    Updated: 2026/06/25 23:36:22 by alex             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self):
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, {self._show_count} show")

    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age):
        return age > 365
    
    @classmethod
    def anonymous(cls):
        return cls("Unknown Plant", 0.0, 0)
    
    def grow(self):
        self._height += 30
        self._stats._grow_count += 1
    
    def aging(self):
        self._age += 20
        self._stats._age_count += 1
    
    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        self._stats._show_count += 1

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed == True:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

        def display(self):
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self._diameter = diameter
        self._stats = Tree.Stats()

    def shades(self):
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._diameter}cm wide.")
        self._stats._shade_count += 1

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self._diameter}cm")

class Seed(Flower):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age, color)
        self._seeds = 0
    
    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")

def display_stats(plant):
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    Tree.shades(oak)
    print("[statistics for Oak]")
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow age and bloom]")
    sunflower.aging()
    sunflower.grow()
    sunflower.bloom()
    sunflower._seeds = 42
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("")

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)