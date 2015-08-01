define e = Character('Eileen', color="#c8ffc8")

init:
    image snow = Snow("images/Snowflake.gif", maxparticles=200, wind=200)

# The game starts here.
label start:
    scene mm_bg

    e "You've created a new Ren'Py game."
    
    show snow

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
