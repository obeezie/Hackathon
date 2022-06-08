from classes.ninja import Ninja
from classes.pirate import Pirate
import random

turn = random.randint(1,2)

# super().compare_speed(Ninja.speed, Pirate.speed)

michaelangelo = Ninja("Michaelangelo")
jack_sparrow = Pirate("Jack Sparrow")

def play_again():
    choice = input("Would you like to play again? y/n")
    if choice == "y":
        play = True
        michaelangelo.__init__("Michaelangelo")
        jack_sparrow.__init__("Jack Sparrow")
    else: 
        play = False 
    return play

print("Thanks for playing")


# michaelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# michaelangelo.use_item(jack_sparrow)

play = True

while play == True:
    if turn == 1:
        michaelangelo.show_stats()
        michaelangelo.choose_action(jack_sparrow)
        if jack_sparrow.health <= 0:
            print(f"{jack_sparrow.name} is Dead!")
            play = False
            play = play_again()
        turn = 2    
    if turn == 2:
        jack_sparrow.show_stats()
        jack_sparrow.choose_action(michaelangelo)
        if michaelangelo.health <= 0:
            print(f"{michaelangelo.name} is Dead!")
            play = False
            play = play_again()


        turn = 1



# michaelangelo.use_item()

# print(turn)