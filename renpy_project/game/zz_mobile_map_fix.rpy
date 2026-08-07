# Final mobile City Map override / Android diagnostic.
# This intentionally avoids dynamic viewport iteration and image assets so we can
# isolate whether Android is rendering the map controls themselves.

screen map_screen(loc_id):
    style_prefix "map"
    modal True
    add Solid("#1a0e2e")

    frame:
        xfill True
        yfill True
        padding (14, 14)
        background Solid("#1a0e2e")

        vbox:
            xfill True
            spacing 8

            text "Destiny City Map" size 25 color "#a78bfa" xalign 0.5
            text "Location: [locations[loc_id]['name']]" size 14 color "#e9d5ff" xalign 0.5
            text "Energy: [energy]/[max_energy] | Coins: [coins] | Day: [day]" size 13 color "#f472b6" xalign 0.5
            text "Android Map Diagnostic" size 12 color "#9a8aaf" xalign 0.5

            viewport:
                id "mobile_city_map_viewport"
                xfill True
                ysize 570
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    xfill True
                    spacing 8

                    textbutton "🏠  Your Apartment":
                        xfill True
                        yminimum 58
                        action Return(("home", None))
                    textbutton "🍺  The Howling Pint":
                        xfill True
                        yminimum 58
                        action Return(("bar", None))
                    textbutton "🏢  V Tower":
                        xfill True
                        yminimum 58
                        action Return(("vtower", None))
                    textbutton "🌲  Moonlit Forest":
                        xfill True
                        yminimum 58
                        action Return(("forest", None))
                    textbutton "⛩️  Ancient Shrine":
                        xfill True
                        yminimum 58
                        action Return(("shrine", None))
                    textbutton "🏺  Desert Temple":
                        xfill True
                        yminimum 58
                        action Return(("temple", None))
                    textbutton "🌃  Back Alley":
                        xfill True
                        yminimum 58
                        action Return(("alley", None))
                    textbutton "✦  The Crossroads":
                        xfill True
                        yminimum 58
                        action Return(("crossroads", None))
                    textbutton "☕  Starlight Cafe":
                        xfill True
                        yminimum 58
                        action Return(("cafe", None))
                    textbutton "🦊  Foxhollow":
                        xfill True
                        yminimum 58
                        action Return(("foxhollow", None))
                    textbutton "📚  The Archive":
                        xfill True
                        yminimum 58
                        action Return(("archive", None))
                    textbutton "🏫  Cherryton Academy":
                        xfill True
                        yminimum 58
                        action Return(("cherryton", None))

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
