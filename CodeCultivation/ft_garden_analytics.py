class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown Plant", 0.0, 0)

    def grow(self) -> None:
        self._height += 30
        self._stats._grow_count += 1

    def aging(self) -> None:
        self._age += 20
        self._stats._age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        self._stats._show_count += 1


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

class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        harvest: str, nutritional: float
    ) -> None:
        super().__init__(name, height, age)
        self._harvest = harvest
        self._nutritional = nutritional

    def grow(self) -> None:
        super().grow()
        self._nutritional += 1

    def aging(self) -> None:
        super().aging()
        self._nutritional += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest}")
        print(f"Nutritional value: {self._nutritional}")

class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self._diameter = diameter
        self._stats = Tree.Stats()

    def shades(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._diameter}cm wide."
        )
        self._stats._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {self._diameter}cm")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str, seeds: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def set_seeds(self, count: int) -> None:
        self._seeds = count

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
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
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
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
    oak.shades()
    print("[statistics for Oak]")
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.aging()
    sunflower.grow()
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0.0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.grow()
        tomato.aging()
    tomato.show()
    print("[statistics for Tomato]")
    display_stats(tomato)
    print("")

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)