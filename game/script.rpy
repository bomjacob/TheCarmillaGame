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

    #Custom transforms
    # define 4 positions so that we can have more than 3 characters at the front of the screen at once
    # looks like this:  |   left 2  left1   right1  right2  |
    # anchors image a bit below the bottom of the screen

    transform basetrans:
        xanchor 0.5 ypos 1.0 yanchor 0.8 zoom 1.2

    transform left2:
        on show:
            xpos 0.125 basetrans
        on replace:
            linear 1 xpos 0.125 basetrans

    transform left1:
        on show:
            xpos 0.375 basetrans
        on replace:
            linear 1.0 xpos 0.375 basetrans

    transform right1:
        on show:
            xpos 0.625 basetrans
        on replace:
            linear 1.0 xpos 0.625 basetrans

    transform right2:
        on show:
            xpos 0.875 basetrans
        on replace:
            linear 1.0 xpos 0.875 basetrans
    

# The game starts here.
label start:  
    #Stop main menu music
    stop music

    menu:
        "Run tests, or tiny demo?"
    
        "Dorm Scene":
            call dorm from _call_dorm
        "Travelling Scene":
            call travelling from _call_travelling
        "Tests":
            call tests from _call_tests

    call credits from _call_credits

    return