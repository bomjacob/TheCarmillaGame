# Code for riddle battle

#Placeholder characters for now
image laura = Placeholder('girl')
image lief = Placeholder('boy')

define le = Character(name="Lief")
define l = Character(name="Laura")

label riddle_battle:
    $ import random
    define correct_riddles = 0
    define riddles = [
        ("What means something to you, but not to me?",
            ("Your mom.", "You opinion.", "Your life."), 2),
        ("I have a head but never weep, have a bed but never sleep,\nhave a bank but not a cent, although I run I'm never spent.\nWhat am I?",
            ("An emotionless highly caffeinated poor athlete.", "A River"), 1),
        ("What has a single eye but cannot see?",
            ("A needle", "A blind pirate", "A blind cyclops"), 0),
        ("What is he that builds stronger than either the mason, the shipwright or the carpenter?",
            ("The Writer", "The Priest", "The Gallows-maker"), 2)
        ]
    define lief_replies = {True: ("Yes, that is correct!", "It's correct!"),
                           False: ("Haha, that's completely wrong!", "Nope! Wrong!")}
    show lief

    le "Let the riddle battle begin!"
    l "I'm so ready for this!"

    $ renpy.random.shuffle(riddles)

    # Randomly loop though riddles
    $ i = len(riddles)
    while i > 0:
        $ i -= 1
        $ riddle = riddles[i]
        # Lief says riddle text
        le "[riddle[0]]"
        # Shuffle choices
        $ choices = [(x, j) for j, x in enumerate(riddle[1])]
        $ random.shuffle(choices)
        # Menu
        $ answer = renpy.display_menu(choices)
        # If answer is correct
        if answer == riddle[2]:
            $ le(random.choice(lief_replies[True]))
            $ correct_riddles += 1
        else:
            with vpunch
            with hpunch
            $ le(random.choice(lief_replies[False]))
            


    "Test" "You answered [correct_riddles] riddles correctly!"


