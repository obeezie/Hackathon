# from ninjas_vs_pirates.classes import Ninja


class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.parrot = 3
        self.health_potions = 1
        self.scurvy = 2

    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def choose_action( self, ninja):
        print(f"----------Start of {self.name}'s turn-------------")
        print(f"Choose an action:")
        print(f"1: Attack")
        print(f"2: Use item")
        choice = input("Choose a number: ")
        if choice == "1":
            self.attack(ninja)
        elif choice == "2":
            self.use_item(ninja)

    def attack ( self , ninja ):
        ninja.health -= self.strength

        print(f"\n{self.name} attacks {ninja.name} for 15dmg")
        print(f"{ninja.name} health is now {ninja.health}hp")
        return self

    def use_item(self, ninja):
        choice = " "
        print("-------------------Items-------------------")
        print(f"1 -> Parrot = {self.parrot} : Deals 15dmg")
        print(f"2 -> Health Potion = {self.health_potions} : Heals 25hp")
        print(f"3 -> Scurvy Bite = {self.scurvy} : Enemy loses 2 strength points")
        choice = input("Enter the corresponding number to use item: ")

        if choice == "1":
            if self.parrot > 0:
                self.parrot -= 1
                ninja.health -= 10
                print(f"\n{self.name} uses a macaw!")
                print(f"{ninja.name}'s health: {ninja.health}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough avian friends!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja)

        elif choice == "2":
            if self.health_potions > 0:
                self.health_potions -= 1
                self.health += 25
                print(f"\n{self.name} uses a health potion")
                print(f"{self.name}'s health has increased: {self.health}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough health potions")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja)
        elif choice == "3":
            if self.scurvy > 0:
                self.scurvy -= 1
                ninja.strength -= 2
                print(f"\n{self.name} uses Scurvy Bite")
                print(f"{ninja.name}'s strength: {ninja.strength}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough teeth left!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(ninja) 
