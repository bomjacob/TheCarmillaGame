label splashscreen:
    scene black
    $ renpy.pause(0.5, hard=True)

    show text "{size=+10}TheCarmillaGame Team presents...{/size}" at truecenter with dissolve
    $ renpy.pause(2, hard=True)

    hide text with dissolve
    $ renpy.pause(0.5, hard=True)

    return