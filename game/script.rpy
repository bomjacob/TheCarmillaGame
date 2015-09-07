init:
    # Custom effects / transitions
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

    #Main characters
    define carm = Character(name="Carmilla", who_color="#F20505", image="carm")
    define laura = Character(name="Laura", who_color="#FFCE00", what_slow_cps_multiplier=1.2, image="laura")
    define perry = Character(name="Perry", who_color="#0D198A", image="perry")
    define laf = Character(name="LaFontaine", who_color="#268A15", image="laf")

    #Minor characters
    define leif = Character(name="Leif", who_color="#8A8335", image="leif")
    define mayor = Character(name="The Mayor", image="mayor")
    

# The game starts here.
label start:  
    #Stop main menu music
    stop music

    menu:
        "Run tests, or tiny demo?"
    
        "Dorm Scene":
            call dorm from _call_dorm
        "Tests":
            call tests from _call_tests

    call credits from _call_credits

    return