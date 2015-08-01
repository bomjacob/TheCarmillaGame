define e = Character('Eileen', color="#c8ffc8")

init:
    image snow = Snow("images/Snowflake.gif", maxparticles=200, wind=200)

# The game starts here.
label start:
    scene mm_bg

    "Hello2"

    call riddle_battle from _call_riddle_battle

    return
