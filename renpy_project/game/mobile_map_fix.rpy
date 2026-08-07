# Mobile City Map compatibility layer
# Keeps the existing map data/logic intact while providing a touch-friendly
# presentation for the project's 480x854 portrait Android target.

screen mobile_map_screen(loc_id):
    modal True
    zorder 100

    frame:
        xfill True
        yfill True
        background Solid("#10131b")

        vbox:
            xfill True
            yfill True
            spacing 8
            padding (12, 12)

            hbox:
                xfill True
                ysize 52
                spacing 8

                text "CITY MAP":
                    size 28
                    bold True
                    yalign 0.5

                null width 1

                textbutton "CLOSE":
                    xminimum 100
                    yminimum 48
                    action Return("back")

            # A touch-first scrolling area.  The existing map data is reused,
            # but buttons are deliberately large enough for Android taps.
            viewport:
                id "mobile_city_map_viewport"
                mousewheel True
                draggable True
                scrollbars "vertical"
                yfill True

                vbox:
                    xfill True
                    spacing 10

                    for map_loc_key, map_loc_data in locations.items():
                        frame:
                            xfill True
                            padding (10, 10)
                            background Solid("#1c2230")

                            vbox:
                                xfill True
                                spacing 8

                                text map_loc_data.get("name", map_loc_key):
                                    size 24
                                    bold True

                                text map_loc_data.get("desc", ""):
                                    size 17

                                for map_char_id in map_loc_data.get("characters", []):
                                    if map_char_id in characters:
                                        textbutton characters[map_char_id].get("name", map_char_id):
                                            xfill True
                                            yminimum 56
                                            action Return(map_char_id)

            textbutton "RETURN":
                xfill True
                yminimum 56
                action Return("back")

# Override the city-map entry point with a mobile-safe screen.
label mobile_city_map:
    call screen mobile_map_screen(current_location)
    return
