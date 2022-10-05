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
            return final_punchline + "Ba Dum Ta Tuss!"



player = input("\nWelcome to the World of Knock Knock Jokes! Now please tell us, who is there?\n")
joke_categories = ['Animal', 'Food', 'Scary', 'Out of this WORLD!']
print(f"\nNow, {player}, from the categories shown, please choose your category:")
for joke in joke_categories:
    print(joke)

player_category = input("\nChoose wisely.... ")

print("\nExcellent Choice!\n")

practice = KnockKnockJokes(player, player_category)
print(practice)