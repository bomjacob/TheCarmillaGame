init:
    # Custom effects / transitions
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)

    #Click to continue indicator
    image ctc_blink:
       "ui/ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 

    #Main characters
    define carm = Character(name="Carmilla", who_color="#F20505", ctc="ctc_blink", ctc_position="nestled")
    define laura = Character(name="Laura", who_color="#FFCE00", ctc="ctc_blink", ctc_position="nestled", what_slow_cps_multiplier=1.2, image="laura")
    define perry = Character(name="Perry", who_color="#0D198A", ctc="ctc_blink", ctc_position="nestled")
    define laf = Character(name="LaFontaine", who_color="#268A15", ctc="ctc_blink", ctc_position="nestled")

    #Minor characters
    define leif = Character(name="Leif", who_color="#8A8335", ctc="ctc_blink", ctc_position="nestled")
    define mayor = Character(name="The Mayor", ctc="ctc_blink", ctc_position="nestled")

    #Narrator
    define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
    

# The game starts here.
label start:  
    #Stop main menu music
    stop music

    menu:
        "Run tests, or tiny demo?"
    
        "Tiny Demo":
            call dorm from _call_dorm
        "Tests":
            call tests from _call_tests

    call credits from _call_credits

    return