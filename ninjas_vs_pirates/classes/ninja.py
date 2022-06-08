class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.throwing_stars = 0
        self.health_potions = 1
        self.poison = 1
    
    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def choose_action( self, pirate):
        print(f"----------Start of {self.name}'s turn-------------")
        print(f"Choose an action:")
        print(f"1: Attack")
        print(f"2: Use item")
        choice = input("Choose a number: ")
        if choice == "1":
            self.attack(pirate)
        elif choice == "2":
            self.use_item(pirate)

    def attack( self , pirate ):
        pirate.health -= self.strength

        print(f"\n{self.name} attacks {pirate.name} for 15dmg")
        print(f"{pirate.name} health is now {pirate.health}hp")
        return self

    def use_item(self, pirate):
        choice = " "
        print("-------------------Items-------------------")
        print(f"1 -> Throwing Stars = {self.throwing_stars} : Deals 15dmg")
        print(f"2 -> Health Potion = {self.health_potions} : Heals 25hp")
        print(f"3 -> Poison = {self.poison} : Enemy loses 2 strength points")
        choice = input("Enter the corresponding number to use item: ")

        if choice == "1":
            if self.throwing_stars > 0:
                self.throwing_stars -= 1
                pirate.health -= 10
                print(f"\n{self.name} uses a throwing star")
                print(f"{pirate.name}'s health: {pirate.health}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough throwing stars!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(pirate)

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
                self.use_item(pirate)
        elif choice == "3":
            if self.poison > 0:
                self.poison -= 1
                pirate.strength -= 2
                print(f"\n{self.name} uses poison")
                print(f"{pirate.name}'s strength: {pirate.strength}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                print("Not enough throwing stars!")
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                self.use_item(pirate)
                
    @staticmethod
    def compare_speed(num1, num2):
        if(num1 == num2):
            print("These fighters have the same speed!")
        elif(num1 > num2):
            print("Fighter 1 is dancing between the raindrops!")
        elif(num1 < num2):
            print("Fighter 2 has challenged Barry Allen to a race.")