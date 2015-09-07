init:
    #We want them to be able to walk in and out of the room
    transform __doorway:
        on show:
            xpos 0.38 xanchor 0.5 ypos 0.6 yanchor 1.0 zoom 0.5
        on replace:
            linear 1.0 xpos 0.38 xanchor 0.5 ypos 0.6 yanchor 1.0 zoom 0.5

label dorm:
    show dorm

    show laura normal at center
    "I hold onto the desk in front of me as the ground shakes." with shake
    "I close the lid of my laptop as it stops, and turn towards the door."
    show laura normal at right2
    show carm normal at __doorway with dissolve
    carm "Do you really think now is the time to worry about your laptop?" 
    "Carmilla is standing in the doorway, looking harried."
    laura "I'm not leaving it. What if I need to make an update?"
    "I put the laptop in its bag and throw it over my shoulder. Carmilla looks into the hallway."
    carm "Ginger Twins incoming, and it looks like they’ve packed enough for the whole student body."

    show carm normal at right1

    show perry normal at left1
    show laf normal at left2
    with easeinleft
    perry "Laura, do you really need your laptop?"
    laura "As much as you need all that stuff you guys are carrying!"
    "LaFontaine adjusts the bag on their shoulders."
    carm "She might need to make an update."
    laf "We're going into the mountains, there’s not exactly going to be a great wifi connection! Perr packed {i}food{/i}, which is kind of necessary for survival."
    perry "It's not as much as I’d like to bring -- mostly some trail mix and granola bars-- but it should be enough to make sure we don't starve, I think."
    carm "No blood?"
    laf "There's no way to refrigerate it."
    perry "Well, it’s a bit unsanitary, but we thought - can't you, um, kill an animal?"
    carm "But animal blood tastes awful..."

    "The ground shakes again." with shake
    laura "Maybe we should run now and argue later!"
    laf "Yeah, let's head for the hills."
    hide laf with dissolve
    hide perry with dissolve
    laura "Come on, Carm."
    show carm normal at __doorway
    "She saunters out of our dorm room, mumbling something about who she's going to eat first."

    return
