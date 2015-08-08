init:
    # Custom effects / transitions
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

    #Main characters
    define c = Character(name="Carmilla")
    define l = Character(name="Laura")
    define p = Character(name="Perry")
    define laf = Character(name="LaFontaine")

    #Minor characters
    define leif = Character(name="Leif")
    define mayor = Character(name="The Mayor")
    

# The game starts here.
label start:  
    menu:
        "Run tests, or tiny demo?"
    
        "Tiny Demo":
            call dorm from _call_dorm
        "Tests":
            call test from _call_tests

    call credits from _call_credits

    return