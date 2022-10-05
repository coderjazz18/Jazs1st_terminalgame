# File finally acting as it should


# Knock Knock Class
class KnockKnockJokes:
    def __init__(self) -> None:
        pass


player = input("\nWelcome to the World of Knock Knock Jokes! Now please tell us, who is there?\n")
joke_categories = ['Animal', 'Food', 'Scary', 'Out of this WORLD!']
print(f"\nNow, {player}, from the categories shown, please choose your category:")
for joke in joke_categories:
    print(joke)

player_category = input("\nChoose wisely.... ")

print("\nExcellent Choice!")

