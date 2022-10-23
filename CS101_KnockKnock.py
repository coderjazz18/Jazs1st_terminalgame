# File finally acting as it should
import random
# this module will allow a random joke to be selected



# Knock Knock Class
class KnockKnockJokes:
    def __init__(self, player1, category):
        self.player1 = player1
        self.category = category
    
    def __repr__(self):
        message = f"So you've chosen to do the most bamboozlin of {self.category} Knock Knock Jokes! Very well, we shall begin!"
        return message
    
    def InitalKnock(self):
        print("\nKnock Knock...")

    # NEED TO FIGURE OUT HOW TO GET THIS PART TO WORK NEEP TO LOOP THROUGH DICTIONARIES AND GET THE JOKE
    def whosThere(self, response, jokes):
        lc_response = response.lower()

        # chooses a random joke
        chosen_joke = random.choice(jokes)
        punchline = chosen_joke['punchline']

        if lc_response == str and (response == "whos there?" or "whos there"):
            return punchline
        else:
            return "Pssssttttt!!! You're supposed to say, 'Who's there?' >.<"
    
    def punchline(self, who_response, punchline_pt1, final_punchline):
        if who_response == f"{punchline_pt1} who?":
            return final_punchline + "Ba Dum Ta Tss!"
        else:
            return "Pretend you're an owl and say, who?"

# the ANimal Jokes
animal_jokes = [
    {'punchline':'Moose', "final_punchline":'Moose you bein\' so nosy!'},
    {'punchline':'Poodle', "final_punchline":'Poodle a lil mustard on my hot dog please!'},
    {'punchline':'Iguana', "final_punchline":'Iguana hold your hand.'},
    {'punchline':'Goat', "final_punchline":'Goat to the door and find out!'},
    {'punchline':'Alpaca', "final_punchline":'Alpaca the trunk, you pack-a the suitcase!'}
    ]

# The Food jokes
food_jokes = [
    {'punchline':'Peas', "final_punchline":'Peas to meet you!'},
    {'punchline':'Potatoes', "final_punchline":'Potatoes don\'t have a last name silly!'},
    {'punchline':'Ice-cream Soda', "final_punchline":'ICE SCREAM SODA WHOLE WORLD CAN HEAR ME!'},
    {'punchline':'Muffin', "final_punchline":'Theres muffin the matter with me. I\'m doing fine!'},
    {'punchline':'Butter', "final_punchline":'Butter bring an umbrella - it looks like it\'s rainin\'!'}
]

# The spooky jokes
spooky_jokes = [
    {'punchline':'Harry', "final_punchline":'Harry spider crawling up your back!'},
    {'punchline':'Ivana', "final_punchline":'Ivana suck your blood!'},
    {'punchline':'Ooze', "final_punchline":'Ooze that monster under yer bed!'},
    {'punchline':'Howie', "final_punchline":'Howie gonna hide this dead body?'},
    {'punchline':'Doughnut', "final_punchline":'Doughnut worry, I shall give yer a swift death!'}
]

# the random jokes
out_of_this_world_jokes = [
    {'punchline':'Ash', "final_punchline":'Sounds like you have a cold!'},
    {'punchline':'Sadie', "final_punchline":'Sadie magic word and watch me disappear!'},
    {'punchline':'Cash', "final_punchline":'No thanks, I\'ll have some peanuts.'},
    {'punchline':'Luke', "final_punchline":'Luke through the peephole and find out!'},
    {'punchline':'Roach', "final_punchline":'Roach you an email last week and i\'m still waiting for a response.'}
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
    # the player responds
    player_response = input()
    # respond to the player's 'whos there'
    animal_player.whosThere(player_response, animal_jokes)

