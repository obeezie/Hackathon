from classes.ninja import Ninja
from classes.pirate import Pirate
import random

turn = random.randint(1,2)



michaelangelo = Ninja("Michaelangelo")
jack_sparrow = Pirate("Jack Sparrow")

# michaelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# michaelangelo.use_item(jack_sparrow)

play = True

while play == True:
    if turn == 1:
        michaelangelo.choose_action(jack_sparrow)
        if jack_sparrow.health <= 0:
            play = False
        turn = 2    
    if turn == 2:
        jack_sparrow.choose_action(michaelangelo)
        if michaelangelo.health <= 0:
            play = False
        turn = 1



# michaelangelo.use_item()

# print(turn)