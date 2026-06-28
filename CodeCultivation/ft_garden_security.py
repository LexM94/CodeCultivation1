# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alex <alex@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 01:39:23 by alex              #+#    #+#              #
#    Updated: 2026/06/24 02:02:11 by alex             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
    
    def get_height(self):
        return self._height
    def get_age(self):
        return self._age
    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")
    def set_age(self, age):
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")
    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
    
if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: ", end= "")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-3)
    print()
    rose.show()