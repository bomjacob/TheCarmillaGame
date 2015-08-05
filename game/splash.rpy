init python:
    if persistent.disclaimer_seen is None:
        persistent.disclaimer_seen = False

label splashscreen:
    scene black
    $ renpy.pause(0.5, hard=True)

    image disclaimer:
        Text("""\n{size=80}Disclaimer{/size}\n\n{size=25}TheCarmillaGame Team does not own Carmilla \
(The Web Series). Carmilla (The Web Series) is the intellectual property of U by Kotex. There is no \
financial gain made from this game nor will any be sought. This is for entertainment purposes only.\n\n \
While this game is based, in part, on tweets that are part of the Carmilla (The Web Series) transmedia \
experience, but is in no way canon, or in any way indorsed by the Carmilla Writers.\n\nThis game fills \
the story gap between Season 1 and Season 2 of Carmilla, it is highly recommeded to have watched the \
entirety of Season 1 before playing this game.{/size}""", text_align=0.5, xmaximum=740)
    image ctc:
        Text("""{size=10}Press any key to continue{/size}\n""", text_align=0.5, xmaximum=740)

    show disclaimer at top with dissolve
    if not persistent.disclaimer_seen:
        show ctc at center with dissolve
        $ renpy.pause()
    else:
        $ renpy.pause(3)
    hide disclaimer with dissolve
    hide ctc
    $ persistent.disclaimer_seen = True

    show text "{size=+10}TheCarmillaGame Team presents...{/size}" at truecenter with dissolve
    $ renpy.pause(2, hard=False)

    hide text with dissolve
    $ renpy.pause(0.5, hard=False)

    return