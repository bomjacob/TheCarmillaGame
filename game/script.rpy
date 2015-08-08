init:
    # Custom effects / transitions
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

    #Main characters
    define c = Character(name="Carmilla", who_color="#F20505")
    define l = Character(name="Laura", who_color="#FFCE00", what_slow_cps_multiplier=1.2)
    define p = Character(name="Perry", who_color="#0D198A")
    define laf = Character(name="LaFontaine", who_color="#268A15")

    #Minor characters
    define leif = Character(name="Leif", who_color="#8A8335")
    define mayor = Character(name="The Mayor")
    

# The game starts here.
label start:  
    menu:
        "Run tests, or tiny demo?"
    
        "Tiny Demo":
            call dorm from _call_dorm
        "Tests":
            call tests from _call_tests

    call credits from _call_credits

    return