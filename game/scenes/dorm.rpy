image lauranormal = "img/characters/laura/lauranormal.png"
image dorm = "img/rooms/dorm.jpg"
label dorm:
    show dorm

    show lauranormal
    "I hold onto the desk in front of me as the ground shook and close my laptop as it stops." with shake
    show lauranormal at right with move
    show carmilla at left with dissolve
    c "Do you really think now is the time to worry about your stupid computer?"
    "Carmilla is standing in the doorway when I turn around."
    l "I'm not leaving it. What if I need to make an update?"
    "I put the laptop in its bag and throw it over my shoulder. Carmilla looks into the hallway."
    c "And here comes the Ginger Twins."

    hide carmilla with dissolve
    show perry at left
    show laf at truecenter
    with easeinleft
    p "lauranormal, do you really need that?"
    l "As much as you need that bag."
    "LaFontaine adjusts the bag they are holding."
    hide lauranormal with dissolve
    show carmilla at right with dissolve
    c "She might need to make an update"
    laf "We're going into the mountains."
    laf "Perr packed food."
    p "It's not a lot - just some trail mix and granola bars - but it's enough to make sure we don't starve."
    "I see Carmilla shake her head."
    c "No blood?"
    laf "There's no way to keep it cold."
    p "Can't you kill an animal?"
    c "But animal blood tastes so bad."

    "The ground shakes again." with shake
    hide perry with dissolve
    show lauranormal at left with dissolve
    l "Maybe we should flee now and argue later?"
    laf "Yeah, let's head for the hills."
    hide laf with dissolve
    l "Come on, Carm."
    show carmilla at truecenter with move
    "Suddenly she's beside me, mumbling something about who she'd eat first."

    return
