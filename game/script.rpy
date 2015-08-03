define e = Character('Eileen', color="#c8ffc8")

init:
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

# The game starts here.
label start:  

    "Hello1"

    play sound "sound/effect/angry_mob.mp3"

    "Hello2"

    #call riddle_battle from _call_riddle_battle

    call credits from _call_credits

    return