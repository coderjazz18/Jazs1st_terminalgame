import random

# switched from dictionaries to lists and i'm using index instead
animal_jokes = [
    ['Moose', 'Moose you bein\' so nosy!'],
    ['Poodle', 'Poodle a lil mustard on my hot dog please!'],
    ['Iguana', 'Iguana hold your hand.'],
    ['Goat', 'Goat to the door and find out!'],
    ['Alpaca', 'Alpaca the trunk, you pack-a the suitcase!']
    ]

chosen_joke = random.choice(animal_jokes)
punchline = chosen_joke[0]
print(chosen_joke)
print(punchline)