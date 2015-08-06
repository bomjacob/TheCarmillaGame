init python:
    people = {
        "laura": ("Laura Hollis", "Laura2theLetter"),
        "carmilla": ("Carmilla Karnstein", "HeyCarmilla"),
        "laf": ("S. LaFontaine", "LaFilphormes")
    }

    for person in people:
        char = Character(people[person][0] + '\n{size=-5}{color=#B8A5A6}@' + people[person][1], color="#55ACEE",
            window_left_padding=160, show_side_image=Image("img/tweet/" + people[person][1] + ".png", xalign=0.0, yalign=1.0))
        def f(what, k=char, **kwargs):
            k(what, **kwargs)
        setattr(sys.modules[__name__], "tw_" + person, f)