# Based on http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=22481
label credits(frommenu=False):
    if not frommenu:
        if persistent.credits_seen is None:
            $ persistent.credits_seen = False
        $ hard = not persistent.credits_seen
    else:
        $ hard = False
    scene black
    with dissolve

    if not frommenu:
        show theend:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=hard)
        hide theend

    show cred
    $ renpy.pause(credits_speed, hard=hard)
    hide cred

    if not frommenu:
        show thanks:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(4, hard=hard)
        hide thanks

        $ persistent.credits_seen = True

    return

label credits_frommenu:
    call credits(True) from _call_credits_1

init python:
    credits = (
        ('Lead Developer', 'Jacob', 'the-ballad-of-buffy.tumblr.com'),
        ('Writers', 'M', 'mhbills92.tumblr.com'),
        ('Backgrounds', 'Paperclipfreak', 'omgpaperclipfreak.tumblr.com'),
        ('Characters', 'Caroline Astruz', 'tokiwooki.tumblr.com'),
        ('Additional programming', 'Josie', 'howlwithme.co.vu'),
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
    $ credits_speed = 20
    image cred:
        Text(credits_s, text_align=0.5)
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        linear credits_speed ypos 0.0 yanchor 1.0
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)