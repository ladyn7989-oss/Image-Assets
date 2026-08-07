# Mobile City Map compatibility layer
# Touch-friendly City Map for the project's 480x854 portrait Android target.
# Keeps the existing map_screen name so the existing game flow can call it.

screen map_screen(loc_id):
    style_prefix "map"
    modal True
    add Solid("#1a0e2e")

    frame:
        xfill True
        yfill True
        padding (10, 10)
        background Solid("#1a0e2e")

        vbox:
            xfill True
            yfill True
            spacing 6

            text "Destiny City Map" size 25 color "#a78bfa" xalign 0.5
            text "Location: [locations[loc_id]['name']]" size 14 color "#e9d5ff" xalign 0.5
            text "Energy: [energy]/[max_energy] | Coins: [coins] | Day: [day]" size 13 color "#f472b6" xalign 0.5

            # Give the Android viewport an explicit height and the content an
            # explicit width. This avoids the zero/ambiguous child-size layout
            # that can make a Ren'Py viewport appear empty on mobile.
            viewport:
                id "mobile_city_map_viewport"
                xfill True
                ysize 560
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    xsize 430
                    spacing 8

                    for map_loc_key, map_loc_data in locations.items():
                        frame:
                            xsize 430
                            background Solid("#2a1a3e")
                            padding (10, 8)

                            vbox:
                                xfill True
                                spacing 5

                                text map_loc_data["name"] size 18 color "#a78bfa"
                                text map_loc_data["desc"] size 12 color "#9a8aaf"

                                $ map_loc_chars = map_loc_data.get("chars", [])
                                if map_loc_chars:
                                    $ map_char_names = ", ".join([characters[c]["name"] for c in map_loc_chars if c in characters])
                                    text "Characters here: [map_char_names]" size 11 color "#f472b6"

                                # Stack controls on narrow Android screens so every
                                # action remains comfortably tappable.
                                textbutton "Travel Here":
                                    xfill True
                                    yminimum 50
                                    action Return((map_loc_key, None))

                                for map_char_id in map_loc_chars:
                                    if map_char_id in characters:
                                        textbutton "Visit [characters[map_char_id]['name']]":
                                            xfill True
                                            yminimum 50
                                            action Return((map_loc_key, map_char_id))

            hbox:
                xfill True
                spacing 6

                textbutton "Rest":
                    xfill True
                    yminimum 52
                    action Return("rest")
                textbutton "Shop":
                    xfill True
                    yminimum 52
                    action Return("shop")
                textbutton "Stats":
                    xfill True
                    yminimum 52
                    action Return("stats")
                if cheat_mode:
                    textbutton "Cheats":
                        xfill True
                        yminimum 52
                        action Return("cheat")
