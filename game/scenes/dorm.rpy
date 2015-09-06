init:
    $ doorway = Position(xpos = 0.1, xanchor = 0, ypos = 0.1, yanchor = 0)

label dorm:
    show dorm

    show laura normal at doorway
    "I hold onto the desk in front of me as the ground shakes." with shake
    "I close the lid of my laptop as it stops, and turn towards the door."
    show laura normal at right with move
    show carm normal at doorway with dissolve
    carm "Do you really think now is the time to worry about your stupid computer?" 
    "Carmilla is standing in the doorway, looking harried."
    laura "I'm not leaving it. What if I need to make an update?"
    "I put the laptop in its bag and throw it over my shoulder. Carmilla looks into the hallway."
    carm "Ginger Twins incoming, and it looks like they’ve packed enough for the whole student body."

    hide carm with dissolve
    show perry normal at left
    show laf normal at truecenter
    with easeinleft
    perry "Laura, do you really need your laptop?"
    laura "As much as you need all that stuff you guys are carrying!"
    "LaFontaine adjusts the bag on their shoulders."
    hide laura with dissolve
    show carm normal at right with dissolve
    carm "She might need to make an update."
    laf "We're going into the mountains, there’s not exactly going to be a great wifi connection! Perr packed {i}food{/i}, which is kind of necessary for survival."
    perry "It's not as much as I’d like to bring -- mostly some trail mix and granola bars-- but it should be enough to make sure we don't starve, I think."
    carm "No blood?"
    laf "There's no way to refrigerate it."
    perry "Well, it’s a bit unsanitary, but we thought - can't you, um, kill an animal?"
    carm "But animal blood tastes awful..."

    "The ground shakes again." with shake
    hide perry with dissolve
    show laura normal at left with dissolve
    laura "Maybe we should run now and argue later!"
    laf "Yeah, let's head for the hills."
    hide laf with dissolve
    laura "Come on, Carm."
    show carm normal at truecenter with move
    "She saunters out of our dorm room, mumbling something about who she's going to eat first."

    return
