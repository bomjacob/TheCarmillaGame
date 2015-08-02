# Auto load images from img folder
init python hide:
    for file in renpy.list_files():
        if file.startswith('img/'):
            if file.endswith('.png'):
                name = file.replace('img/','').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file, yanchor=400))
                continue
            continue