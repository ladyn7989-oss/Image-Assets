# Mobile City Map compatibility layer
# Touch-first presentation for the project's 480x854 portrait Android target.

screen mobile_map_screen(loc_id):
    style_prefix "map"
    modal True

    add Solid("#1a0e2e")

    vbox:
        xfill True
        yfill True
        spacing 6
        padding (10, 10)

        text "Destiny City Map" size 25 color "#a78bfa" xalign 0.5
        text "Location: [locations[loc_id]['name']]" size 14 color "#e9d5ff" xalign 0.5
        text "Energy: [energy]/[max_energy] | Coins: [coins] | Day: [day]" size 13 color "#f472b6" xalign 0.5

        viewport:
            id "mobile_city_map_viewport"
            xfill True
            yfill True
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                xfill True
                spacing 8

                for map_loc_key, map_loc_data in locations.items():
                    frame:
                        xfill True
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

                            hbox:
                                xfill True
                                spacing 6

                                textbutton "Travel Here":
                                    xminimum 110
                                    yminimum 50
                                    action Return((map_loc_key, None))

                                for map_char_id in map_loc_chars:
                                    if map_char_id in characters:
                                        textbutton "Visit [characters[map_char_id]['name']]":
                                            xminimum 135
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
