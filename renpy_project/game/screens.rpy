## Date With Destiny - Custom Screens

## ====== TITLE SCREEN ======
screen title_screen():
    style_prefix "title"
    add Solid("#1a0e2e")
    
    vbox:
        xalign 0.5
        yalign 0.25
        spacing 8
        text "Date With Destiny" size 36 color "#a78bfa" xalign 0.5
        text "Ren'Py Edition" size 16 color "#f472b6" xalign 0.5
    
    vbox:
        xalign 0.5
        yalign 0.55
        spacing 12
        xsize 280
        
        textbutton "New Game" action Return("new_game") xalign 0.5
        textbutton "Continue" action Show("load_screen")
        textbutton "Gallery" action Return("gallery") xalign 0.5
        textbutton "Achievements" action Return("achievements") xalign 0.5
        textbutton "Settings" action Return("settings") xalign 0.5
        textbutton "Credits" action Return("credits") xalign 0.5
    
    text "v1.0 — by MariaTheGlaceon" size 12 color "#4a3a5a" xalign 0.5 yalign 0.96

## ====== LOAD SCREEN ======
screen load_screen():
    modal True
    add Solid("#1a0e2e")
    
    vbox:
        xalign 0.5
        yalign 0.15
        text "Load Game" size 28 color "#a78bfa" xalign 0.5
    
    vbox:
        xalign 0.5
        yalign 0.35
        spacing 10
        xsize 280
        for i in range(1, 6):
            $ slot = str(i)
            textbutton "Save Slot [i]" action [SetVariable("_slot_name", slot), Return("load_game")] xalign 0.5
        textbutton "Back" action Hide("load_screen") xalign 0.5

## ====== MAP SCREEN ======
screen map_screen(loc_id):
    style_prefix "map"
    add Solid("#1a0e2e")
    
    vbox:
        xalign 0.5
        yalign 0.05
        spacing 4
        text "Destiny City Map" size 24 color "#a78bfa" xalign 0.5
        text "Location: [locations[loc_id]['name']]" size 14 color "#e9d5ff" xalign 0.5
        text "Energy: [energy]/[max_energy] | Coins: [coins] | Day: [day]" size 14 color "#f472b6" xalign 0.5
    
    # Location grid
    viewport:
        xalign 0.5
        yalign 0.22
        xsize 440
        ysize 420
        scrollbars "vertical"
        mousewheel True
        
        vbox:
            spacing 8
            for loc_key, loc_data in locations.items():
                frame:
                    background Solid("#2a1a3e")
                    xsize 420
                    padding (12, 8)
                    
                    vbox:
                        spacing 4
                        text "[loc_data['name']]" size 16 color "#a78bfa"
                        text "[loc_data['desc']]" size 12 color "#9a8aaf"
                        
                        if loc_data['chars']:
                            text "Characters here: [', '.join([characters[c]['name'] for c in loc_data['chars'] if c in characters])]" size 11 color "#f472b6"
                        
                        hbox:
                            spacing 8
                            textbutton "Travel Here" action Return((loc_key, None)) xminimum 100 yminimum 30
                            for char_id in loc_data['chars']:
                                if char_id in characters:
                                    textbutton "Visit [characters[char_id]['name']]" action Return((loc_key, char_id)) xminimum 120 yminimum 30
    
    # Bottom action bar
    hbox:
        xalign 0.5
        yalign 0.95
        spacing 12
        textbutton "Rest" action Return("rest")
        textbutton "Shop" action Return("shop")
        textbutton "Stats" action Return("stats")
        if cheat_mode:
            textbutton "Cheats" action Return("cheat")

## ====== CHARACTER INTERACTION SCREEN ======
screen char_interaction(char_id):
    style_prefix "char"
    add Solid("#1a0e2e")
    
    $ ch = characters.get(char_id, {})
    
    vbox:
        xalign 0.5
        yalign 0.1
        spacing 6
        text "[ch.get('name', 'Unknown')]" size 28 color "#a78bfa" xalign 0.5
        text "[ch.get('desc', '')]" size 14 color "#9a8aaf" xalign 0.5
        text "Affection: [affection.get(char_id, 0)]/100" size 16 color "#f472b6" xalign 0.5
    
    # Character sprite placeholder
    frame:
        xalign 0.5
        yalign 0.35
        background Solid("#2a1a3e")
        xsize 200
        ysize 200
        text "[ch.get('name', '?')[0]]" size 80 color "#7c3aed" xalign 0.5 yalign 0.5
    
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 10
        xsize 280
        
        textbutton "Talk" action Return("talk")
        textbutton "Date" action Return("date")
        if ch.get('pred', False):
            textbutton "Belly Pet Mode" action Return("belly")
        textbutton "Gift" action Return("gift")
        textbutton "Back" action Return("back")

## ====== BELLY MODE DISPLAY ======
screen belly_display(char_id, drain_level, closeness_level):
    add Solid("#1a0e2e")
    
    vbox:
        xalign 0.5
        yalign 0.08
        spacing 4
        text "Inside [characters[char_id]['name']]'s Belly" size 24 color "#a78bfa" xalign 0.5
        text "Closeness: [closeness_level]  |  Drain: [drain_level]%" size 16 color "#f472b6" xalign 0.5
        text "Occupants: [len(belly_pets)]" size 14 color "#e9d5ff" xalign 0.5
    
    # Belly sprite placeholder
    frame:
        xalign 0.5
        yalign 0.4
        background Solid("#2a1a3e")
        xsize 240
        ysize 240
        text "🫃" size 100 xalign 0.5 yalign 0.5

## ====== ACHIEVEMENT NOTIFICATION ======
screen achievement_popup(name, desc):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.1
        background Solid("#7c3aedDD")
        padding (16, 12)
        
        vbox:
            spacing 4
            text "🏆 Achievement Unlocked!" size 18 color "#f472b6" xalign 0.5
            text "[name]" size 20 color "#e9d5ff" xalign 0.5
            text "[desc]" size 14 color "#c9b5df" xalign 0.5
    
    timer 3.0 action Hide("achievement_popup")

## ====== STYLES ======
style title_text:
    color "#e9d5ff"


style title_button:
    background Solid("#2a1a3e")
    hover_background Solid("#7c3aed")
    padding (20, 12)
    xsize 240

style title_button_text:
    color "#e9d5ff"
    hover_color "#ffffff"
    size 20

style map_text:
    color "#e9d5ff"

style map_button:
    background Solid("#2a1a3e")
    hover_background Solid("#7c3aed44")
    padding (10, 6)

style map_button_text:
    color "#e9d5ff"
    hover_color "#f472b6"
    size 13

style char_text:
    color "#e9d5ff"

style char_button:
    background Solid("#2a1a3e")
    hover_background Solid("#7c3aed")
    padding (20, 14)
    xsize 260

style char_button_text:
    color "#e9d5ff"
    hover_color "#f472b6"
    size 20
