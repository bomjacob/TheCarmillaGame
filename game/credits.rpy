# Based on http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=22481
label credits:
    if persistent.credits_seen is None:
        $ persistent.credits_seen = False
    $ credits_speed = 20
    scene black
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=not persistent.credits_seen)
    hide theend
    with dissolve
    $ renpy.pause(credits_speed - 5, hard=not persistent.credits_seen)
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=not persistent.credits_seen)
    hide thanks
    with dissolve
    $ persistent.credits_seen = True
    return

init python:
    credits = (
        ('Lead Developer', 'Jacob', 'the-ballad-of-buffy.tumblr.com'),
        ('Writers', 'M', 'mhbills92.tumblr.com'),
        ('Backgrounds', 'Paperclipfreak', 'omgpaperclipfreak.tumblr.com'),
        ('Characters', 'Caroline Astruz', 'tokiwooki.tumblr.com'),
        ('Programming', 'Josie', 'howlwithme.co.vu'),
        ('PR', 'Nicole', 'nicoleseatingcake.tumblr.com')
    )
    credits_s = "{size=80}Credits\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += '{size=60}' + c[1] + "\n"
        credits_s += '{size=10}' + c[2] + "{size=60}\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" 
    credits_s += "\n".join(str.split(renpy.version()))
    
init:
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)