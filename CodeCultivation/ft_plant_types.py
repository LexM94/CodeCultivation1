class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self._diameter = diameter

    def shades(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {self._diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest: str, nutritional: float) -> None:
        super().__init__(name, height, age)
        self._harvest = harvest
        self._nutritional = nutritional

    def growth(self) -> None:
        self._height = self._height + 2.1
        self._age = self._age + 1
        self._nutritional = self._nutritional + 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest}")
        print(f"Nutritional value: {self._nutritional}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shades]")
    oak.shades()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.growth()
    tomato.show()
