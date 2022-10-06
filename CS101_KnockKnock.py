# File finally acting as it should


# Knock Knock Class
class KnockKnockJokes:
    def __init__(self, player1, category):
        self.player1 = player1
        self.category = category
    
    def __repr__(self):
        message = f"So you've chosen to do the most bamboozlin of {self.category} Knock Knock Jokes! Very well, we shall begin!"
        return message
    
    def InitalKnock(self):
        print("Knock Knock...")

    def whosThere(self, response, punchline_pt1):
        if response == str and (response == "Whos there?" or "whos there" or 'whos there?' or 'WHOS THERE?'):
            return punchline_pt1
    
    def punchline(self, who_response, punchline_pt1, final_punchline):
        if who_response == f"{punchline_pt1} who?":
            return final_punchline + "Ba Dum Ta Tss!"

# the ANimal Jokes
animal_jokes = {
    {'punchline1':'Moose', "final_punchline":'Moose you bein\' so nosy!'},
    {'punchline1':'Poodle', "final_punchline":'Poodle a lil mustard on my hot dog please!'},
    {'punchline1':'Iguana', "final_punchline":'Iguana hold your hand.'},
    {'punchline1':'Goat', "final_punchline":'Goat to the door and find out!'},
    {'punchline1':'Alpaca', "final_punchline":'Alpaca the trunk, you pack-a the suitcase!'}
}

# The Food jokes
food_jokes = {
    {'punchline1':'Peas', "final_punchline":'Peas to meet you!'},
    {'punchline1':'Potatoes', "final_punchline":'Potatoes don\'t have a last name silly!'},
    {'punchline1':'Ice-cream Soda', "final_punchline":'ICE SCREAM SODA WHOLE WORLD CAN HEAR ME!'},
    {'punchline1':'Muffin', "final_punchline":'Theres muffin the matter with me. I\'m doing fine!'},
    {'punchline1':'Butter', "final_punchline":'Butter bring an umbrella - it looks like it\'s rainin\'!'}
}

# The spooky jokes
spooky_jokes = {
    {'punchline1':'Harry', "final_punchline":'Harry spider crawling up your back!'},
    {'punchline1':'Ivana', "final_punchline":'Ivana suck your blood!'},
    {'punchline1':'Ooze', "final_punchline":'Ooze that monster under yer bed!'},
    {'punchline1':'Howie', "final_punchline":'Howie gonna hide this dead body?'},
    {'punchline1':'Doughnut', "final_punchline":'Doughnut worry, I shall give yer a swift death!'}
}

# the random jokes
out_of_this_world_jokes = {
    {'punchline1':'Ash', "final_punchline":'Sounds like you have a cold!'},
    {'punchline1':'Sadie', "final_punchline":'Sadie magic word and watch me disappear!'},
    {'punchline1':'Cash', "final_punchline":'No thanks, I\'ll have some peanuts.'},
    {'punchline1':'Luke', "final_punchline":'Luke through the peephole and find out!'},
    {'punchline1':'Roach', "final_punchline":'Roach you an email last week and i\'m still waiting for a response.'}
}


# PLayer & Welcome
player = input("\nWelcome to the World of Knock Knock Jokes! Now please tell us, who is there?\n")
joke_categories = ['Animal', 'Food', 'Spooky', 'Out of this WORLD!']
print(f"\nNow, {player}, from the categories shown, please choose your category:")
for joke in joke_categories:
    print(joke)

player_category = input("\nChoose wisely.... ")

print("\nExcellent Choice!\n")

practice = KnockKnockJokes(player, player_category)
print(practice)