label splashscreen:
    scene black
    $ renpy.pause(0.5, hard=True)

    image disclaimer:
        Text("""{size=80}Disclaimer!{/size}\n\n{size=30}TheCarmillaGame Team does not own Carmilla (The Web Series). Carmilla \
(The Web Series) is the intellectual property of U by Kotex. There is no financial gain made from this game nor will \
any be sought. This is for entertainment purposes only.\n
While this game is based, in part, on tweets that are part of the Carmilla (The Web Series) transmedia experience,\
but is in no way canon! Keep that in mind while playing!{/size}""", text_align=0.5, xmaximum=720)

    show disclaimer at top with dissolve
    $ renpy.pause(6, hard=False)
    hide disclaimer

    show text "{size=+10}TheCarmillaGame Team presents...{/size}" at truecenter with dissolve
    $ renpy.pause(2, hard=True)

    hide text with dissolve
    $ renpy.pause(0.5, hard=True)

    return