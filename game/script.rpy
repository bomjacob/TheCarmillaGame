init:
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

# The game starts here.
label start:  

    "Testing twitter handles"

    tw_laura "On the bright side, we have a {b}lot{/b} of bear spray."

    tw_laf "Maybe Perry's right with the whole \"don't use flames in every experiment, weirdo!\" Thing. #goodbyehair #wehadsomefuntimes{w=3.0}\nBut then again, fire. #forscience"

    tw_carmilla "Day 21. I was reduced to eating a badger three days ago. Euugh."

    "Testing mob sounds"

    play sound "sound/effect/angry_mob.mp3"

    "Testing test riddle battle with placeholder dialouge."

    call riddle_battle from _call_riddle_battle

    call credits from _call_credits

    return