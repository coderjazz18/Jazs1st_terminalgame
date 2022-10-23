# File finally acting as it should
import random
# this module will allow a random joke to be selected



# Knock Knock Class
class KnockKnockJokes:
    def __init__(self, player1, category):
        self.player1 = player1
        self.category = category
    
    def __repr__(self):
        # message initiated for the player
        message = f"So you've chosen to do the most bamboozlin of {self.category} Knock Knock Jokes! Very well, we shall begin!"
        return message
    
    def InitalKnock(self):
        # First set of Knock kNock
        print("\nKnock Knock...")
        # the player responds
        self.response = input()

    # NEED TO FIGURE OUT HOW TO GET THIS PART TO WORK NEEP TO LOOP THROUGH DICTIONARIES AND GET THE JOKE
    def whosThere(self, jokes):
        lc_response = self.response.lower()

        # chooses a random joke
        chosen_joke = random.choice(jokes)
        # gets the first punchline to choosen joke
        punchline = chosen_joke[0]

        if self.response == "whos there?" or self.response == "whos there":
            print(punchline)
        else:
            print("Pssssttttt!!! You're supposed to say, 'Who's there?' >.<")
    
    def punchline(self, who_response, punchline_pt1, final_punchline):
        if who_response == f"{punchline_pt1} who?":
            return final_punchline + "Ba Dum Ta Tss!"
        else:
            return "Pretend you're an owl and say, who?"

# the ANimal Jokes
animal_jokes = [
    ['Moose', 'Moose you bein\' so nosy!'],
    ['Poodle', 'Poodle a lil mustard on my hot dog please!'],
    ['Iguana', 'Iguana hold your hand.'],
    ['Goat', 'Goat to the door and find out!'],
    ['Alpaca', 'Alpaca the trunk, you pack-a the suitcase!']
    ]

# The Food jokes
food_jokes = [
    ['Peas', 'Peas to meet you!'],
    ['Potatoes', 'Potatoes don\'t have a last name silly!'],
    ['Ice-cream Soda', 'ICE SCREAM SODA WHOLE WORLD CAN HEAR ME!'],
    ['Muffin', 'Theres muffin the matter with me. I\'m doing fine!'],
    ['Butter', 'Butter bring an umbrella - it looks like it\'s rainin\'!']
]

# The spooky jokes
spooky_jokes = [
    ['Harry', 'Harry spider crawling up your back!'],
    ['Ivana', 'Ivana suck your blood!'],
    ['Ooze', 'Ooze that monster under yer bed!'],
    ['Howie', 'Howie gonna hide this dead body?'],
    ['Doughnut', 'Doughnut worry, I shall give yer a swift death!']
]

# the random jokes
out_of_this_world_jokes = [
    ['Ash', 'Sounds like you have a cold!'],
    ['Sadie', 'Sadie magic word and watch me disappear!'],
    ['Cash', 'No thanks, I\'ll have some peanuts.'],
    ['Luke', 'Luke through the peephole and find out!'],
    ['Roach', 'Roach you an email last week and i\'m still waiting for a response.']
]

# PLayer & Welcome
player = input("\nWelcome to the World of Knock Knock Jokes! Now please tell us, who is there?\n")
joke_categories = ['Animal', 'Food', 'Spooky', 'Out of this WORLD!']
print(f"\nNow, {player}, from the categories shown, please choose your category:")
for joke in joke_categories:
    print(joke)

player_category = input("\nChoose wisely.... ")

print("\nExcellent Choice!\n")



# makes sure ot lowercase whatever was typed by player
category_lowercase = player_category.lower()
if category_lowercase == "animal":
    animal_player = KnockKnockJokes(player, player_category)
    print(animal_player)
    # The game begins
    animal_player.InitalKnock()
    # respond to the player's 'whos there'
    animal_player.whosThere(animal_jokes)


