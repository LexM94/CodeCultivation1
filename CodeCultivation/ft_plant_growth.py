# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alex <alex@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/22 01:18:08 by alex              #+#    #+#              #
#    Updated: 2026/06/22 01:32:36 by alex             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth
    
    def grow(self):
        self.height = self.growth + self.height
    
    def aging(self):
        self.age = self.age + 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()

    start_height = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.aging()
        print(f"=== Day {day} ===")
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")