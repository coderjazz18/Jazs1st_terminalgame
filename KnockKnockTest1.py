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
final_punchline = chosen_joke[1]
print(punchline)
# made the final punchline work
who_response = input()
lc_whoRsp = who_response.lower()
if (lc_whoRsp ==  f"{punchline.lower()} who?") or (lc_whoRsp == f"{punchline.lower()} who"):
    print(f"{final_punchline}\nBa Dum Ta Tss!")
else:
    print("Pretend you're an owl and say, who! Try Again!")