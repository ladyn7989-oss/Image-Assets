## Date With Destiny - Main Script
## Core game engine: title screen, map navigation, VN dialogue, belly mode

## ====== GLOBAL STATE ======
default energy = 5
default max_energy = 5
default day = 1
default month = 1
default coins = 50
default time_of_day = "morning"
default current_location = "home"
default current_character = None
default affection = {}
default belly_pets = []
default closeness = {}
default drain = {}
default achievements = set()
default cheat_mode = False
default endless_score = 0
default endless_rounds = 0
default gifted = {}
default visited_dates = []
default riko_collection = []
default new_game_plus = False
default daily_challenge_active = False
default text_speed = 0.03
default animations_enabled = True
default bgm_enabled = True

## ====== MAP LOCATIONS =======
define locations = {
    "home": {"name": "Your Apartment", "desc": "A cozy studio apartment. Your home base.", "chars": []},
    "bar": {"name": "The Howling Pint", "desc": "A dimly lit bar downtown. Smells like whiskey.", "chars": ["husk", "fomo"]},
    "vtower": {"name": "V Tower", "desc": "A sleek penthouse in the entertainment district.", "chars": ["vox"]},
    "forest": {"name": "Moonlit Forest", "desc": "Ancient trees, dappled moonlight. Peaceful.", "chars": ["wolf", "glacia"]},
    "shrine": {"name": "Ancient Shrine", "desc": "A weathered shrine on the hilltop.", "chars": ["anubis"]},
    "temple": {"name": "Desert Temple", "desc": "Golden sands surround an ancient temple.", "chars": ["beerus", "champa"]},
    "alley": {"name": "Back Alley", "desc": "A narrow alley behind the city market.", "chars": ["vincent"]},
    "crossroads": {"name": "The Crossroads", "desc": "A mysterious intersection where paths cross.", "chars": ["riko"]},
    "cafe": {"name": "Starlight Cafe", "desc": "A cozy cafe with warm lighting.", "chars": ["aether", "luna"]},
    "foxhollow": {"name": "Foxhollow", "desc": "A quiet grove where fox spirits gather.", "chars": ["nyx", "zero", "luce"]},
    "archive": {"name": "The Archive", "desc": "A vast library of forgotten memories.", "chars": ["solene"]},
    "cherryton": {"name": "Cherryton Academy", "desc": "A prestigious school for anthro students.", "chars": ["louis", "legoshi", "riz", "bill", "gohin"]},
}

## ====== GAME FLOW ======

label start:
    call screen title_screen
    $ result = _return
    
    if result == "new_game":
        jump new_game
    elif result == "load_game":
        $ renpy.load(_slot_name)
    elif result == "gallery":
        jump gallery
    elif result == "settings":
        jump settings
    elif result == "achievements":
        jump achievements_screen
    elif result == "credits":
        jump credits

label new_game:
    scene black
    "You wake up in a new city. A fresh start — new faces, new possibilities."
    "Your phone buzzes. A dating app notification: 'Welcome to Destiny City! Meet your soulmate today.'"
    "You look out the window at the sprawling city below. Time to explore."
    jump city_map

label city_map:
    $ time_label = {"morning": "☀️ Morning", "afternoon": "🌤️ Afternoon", "evening": "🌆 Evening", "night": "🌙 Night"}[time_of_day]
    scene black
    show text "Day [day] — [time_label]\nEnergy: [energy]/[max_energy]  |  Coins: [coins]\nLocation: [locations[current_location]['name']]" at truecenter
    pause 1.0
    hide text
    call screen map_screen(current_location)
    $ action = _return
    
    if action == "rest":
        "You rest and recover your energy."
        $ energy = max_energy
        $ advance_time()
        jump city_map
    
    elif action == "shop":
        jump shop
    
    elif action == "stats":
        jump stats_screen
    
    elif action == "cheat":
        jump cheat_menu
    
    elif isinstance(action, tuple):
        $ loc_id, char_id = action
        if loc_id != current_location:
            $ current_location = loc_id
            $ energy -= 1
            $ advance_time()
            "You travel to [locations[loc_id]['name']]."
        if char_id:
            $ current_character = char_id
            jump character_menu
        else:
            jump city_map
    else:
        jump city_map

label character_menu:
    $ ch = characters[current_character]
    scene black
    show text "[ch['name']] is here.\nAffection: [affection.get(current_character, 0)]/100" at truecenter
    pause 0.5
    hide text
    
    call screen char_interaction(current_character)
    $ choice = _return
    
    if choice == "talk":
        jump talk_tree
    elif choice == "date":
        if energy < 1:
            "You don't have enough energy to go on a date."
            jump character_menu
        $ energy -= 1
        jump story_mode
    elif choice == "belly":
        jump belly_join
    elif choice == "gift":
        jump gift_menu
    elif choice == "back":
        jump city_map

## ====== TIME SYSTEM ======
init python:
    def advance_time():
        global time_of_day, day, month, energy, max_energy
        order = ["morning", "afternoon", "evening", "night"]
        idx = order.index(time_of_day)
        idx += 1
        if idx >= 4:
            idx = 0
            day += 1
            if day > 30:
                day = 1
                month += 1
                renpy.notify("A new month begins...")
        time_of_day = order[idx]
        if time_of_day == "morning":
            energy = max_energy
            # World simulation: characters move, encounters happen
            update_world()

## ====== WORLD SIMULATION ======
init python:
    def update_world():
        # 30% chance a character moves to a random location
        import random
        for char_id in characters:
            if random.random() < 0.3:
                if char_id not in ["aether", "luna"]:  # Protected chars don't move
                    new_loc = random.choice(list(locations.keys()))
                    # Remove from old location
                    for loc in locations.values():
                        if char_id in loc["chars"]:
                            loc["chars"].remove(char_id)
                    locations[new_loc]["chars"].append(char_id)
        
        # 30% chance of belly pet encounter
        if random.random() < 0.3:
            preds = [c for c in characters if characters[c].get("pred", False)]
            prey = [c for c in characters if not characters[c].get("pred", False) and c not in ["aether", "luna"]]
            if preds and prey:
                pred = random.choice(preds)
                victim = random.choice(prey)
                if victim not in belly_pets:
                    belly_pets.append({"pred": pred, "prey": victim, "drain": 0})

## ====== STORY MODE ======
label story_mode:
    $ ch = characters[current_character]
    $ scene_idx = 0
    $ branch_flags = {}
    
label story_scene:
    if scene_idx >= 7:
        jump story_ending
    $ sc = ch['story'][scene_idx]
    scene black with dissolve
    "[sc['text']]"
    if 'choices' in sc and sc['choices']:
        menu:
            for choice in sc['choices']:
                $ label_text = choice['text']
                "[label_text]":
                    $ branch_flags[choice.get('flag', '')] = choice.get('value', True)
                    if 'affection' in choice:
                        $ affection[current_character] = affection.get(current_character, 0) + choice['affection']
                    if 'goto' in choice:
                        $ scene_idx = choice['goto']
                    else:
                        $ scene_idx += 1
                    jump story_scene
    else:
        $ scene_idx += 1
        jump story_scene

label story_ending:
    $ aff = affection.get(current_character, 0)
    if aff >= 70:
        $ ending_type = "good"
    elif aff >= 30:
        $ ending_type = "neutral"
    else:
        $ ending_type = "bad"
    $ ending_text = ch.get('endings', {}).get(ending_type, "Your date comes to an end.")
    scene black with dissolve
    "[ending_text]"
    $ achievements.add("First Date")
    if ending_type == "good":
        $ achievements.add("True Romance")
    elif ending_type == "bad":
        $ achievements.add("Cold Rejection")
    jump post_ending

label post_ending:
    "What would you like to do?"
    menu:
        "Enter Belly Pet Mode" if ch.get('pred', False):
            jump belly_mode
        "Continue to Endless Mode":
            jump endless_mode
        "Return to City Map":
            jump city_map

## ====== BELLY PET MODE ======
label belly_mode:
    $ ch = characters[current_character]
    $ closeness[current_character] = closeness.get(current_character, 0)
    $ drain_level = drain.get(current_character, 0)
    
label belly_loop:
    scene black with dissolve
    show text "[ch['name']]'s Belly Pet Mode\nCloseness: [closeness[current_character]]  |  Drain: [drain_level]%\nOccupants: [len(belly_pets)]" at truecenter
    pause 0.5
    hide text
    
    menu:
        "{b}Squirm{/b}":
            $ reaction = get_belly_reaction(current_character, "squirm")
            "[reaction]"
            $ closeness[current_character] -= 2
            if current_character == "riko":
                $ drain_level = max(0, drain_level - 3)
            jump belly_loop
        "{b}Massage{/b}":
            $ reaction = get_belly_reaction(current_character, "massage")
            "[reaction]"
            $ closeness[current_character] += 3
            if current_character == "riko":
                $ drain_level = min(100, drain_level + 12)
            jump belly_loop
        "{b}Talk{/b}":
            $ reaction = get_belly_reaction(current_character, "talk")
            "[reaction]"
            $ closeness[current_character] += 1
            if current_character == "riko":
                $ drain_level = min(100, drain_level + 5)
            jump belly_loop
        "{b}Chat (AI){/b}":
            jump ai_chat
        "{b}Struggle Free{/b}" if drain_level < 50 or current_character != "riko":
            "You manage to struggle free!"
            $ drain[current_character] = 0
            jump city_map
        "{b}Leave{/b}":
            $ drain[current_character] = drain_level
            jump city_map

    if drain_level >= 100 and current_character == "riko":
        jump drained_ending

label drained_ending:
    scene black with dissolve
    "Riko's drain has reached 100%! Your strength flows into him..."
    "You feel yourself becoming part of him — permanently."
    "Riko: 'Finally... your power is mine. You're mine forever now.'"
    $ achievements.add("Drained")
    $ affection["riko"] = 100
    "You have been permanently absorbed by Riko."
    jump city_map

## ====== AI CHAT SYSTEM ======
label ai_chat:
    $ ch = characters[current_character]
    "Chat with [ch['name']] inside the belly. Type a message:"
    
label chat_loop:
    $ user_input = renpy.input("You:", length=200)
    $ user_input = user_input.strip()
    if user_input == "":
        jump chat_loop
    if user_input.lower() in ["exit", "quit", "leave", "back"]:
        jump belly_loop
    $ response = get_ai_chat_response(current_character, user_input)
    "[ch['name']]: [response]"
    jump chat_loop

## ====== ENDLESS MODE ======
label endless_mode:
    $ ch = characters[current_character]
    $ endless_score = 0
    $ endless_rounds = 0
    
label endless_round:
    $ endless_rounds += 1
    $ scenario = get_endless_scenario()
    scene black with dissolve
    "[scenario['text']]"
    menu:
        for choice in scenario['choices']:
            $ label_text = choice['text']
            "[label_text]":
                $ aff_change = choice.get('affection', 0)
                $ affection[current_character] = max(0, min(100, affection.get(current_character, 0) + aff_change))
                $ endless_score += abs(aff_change)
                if aff_change > 0:
                    "[ch['name']]: [choice.get('reaction', '...')]"
                else:
                    "[ch['name']]: [choice.get('reaction', '...')]"
    if endless_rounds >= 10:
        $ achievements.add("Marathon Date")
    elif endless_rounds >= 5:
        $ achievements.add("Survivor")
    "Round [endless_rounds] complete! Score: [endless_score]"
    menu:
        "Continue":
            jump endless_round
        "End":
            "Final Score: [endless_score] in [endless_rounds] rounds!"
            jump city_map

## ====== GIFT SYSTEM ======
label gift_menu:
    $ ch = characters[current_character]
    "Gift Shop — Your Coins: [coins]"
    menu:
        "Chocolate Box (20 coins)" if coins >= 20:
            $ coins -= 20
            $ affection[current_character] = min(100, affection.get(current_character, 0) + 10)
            $ gifted[current_character] = gifted.get(current_character, []) + ["chocolate"]
            "[ch['name']] loves the chocolate! +10 affection!"
        "Plush Toy (35 coins)" if coins >= 35:
            $ coins -= 35
            $ affection[current_character] = min(100, affection.get(current_character, 0) + 15)
            "[ch['name']] hugs the plushie tight! +15 affection!"
        "Belly Oil (50 coins)" if coins >= 50:
            $ coins -= 50
            $ affection[current_character] = min(100, affection.get(current_character, 0) + 25)
            $ closeness[current_character] = closeness.get(current_character, 0) + 10
            "[ch['name']] purrs at the belly oil... +25 affection, +10 closeness!"
        "Back":
            jump character_menu
    jump gift_menu

label shop:
    "Welcome to the shop! Coins: [coins]"
    menu:
        "Refill Energy (10 coins)" if coins >= 10 and energy < max_energy:
            $ coins -= 10
            $ energy = max_energy
            "Energy restored!"
        "Buy Chocolate (20 coins)" if coins >= 20:
            $ coins -= 20
            "Bought chocolate for gifting."
        "Buy Plush Toy (35 coins)" if coins >= 35:
            $ coins -= 35
            "Bought a plush toy."
        "Buy Belly Oil (50 coins)" if coins >= 50:
            $ coins -= 50
            "Bought belly oil."
        "Back":
            jump city_map
    jump shop

## ====== STATS SCREEN ======
label stats_screen:
    scene black with dissolve
    show text "=== Stats ===\nDay: [day]  Month: [month]\nCoins: [coins]\nEnergy: [energy]/[max_energy]\n\nDates Completed: [len(visited_dates)]\nAchievements: [len(achievements)]/20\n\nAffection Levels:" at truecenter
    pause 2.0
    hide text
    jump city_map

## ====== CHEAT MODE ======
label cheat_menu:
    if not cheat_mode:
        "Cheat Mode is disabled. Enable it?"
        menu:
            "Yes":
                $ cheat_mode = True
            "No":
                jump city_map
    "Cheat Menu:"
    menu:
        "Max Affection (all)":
            python:
                for cid in characters:
                    affection[cid] = 100
            "All affection maxed!"
            jump cheat_menu
        "+100 Coins":
            $ coins += 100
            "Coins: [coins]"
            jump cheat_menu
        "Refill Energy":
            $ energy = max_energy
            "Energy refilled!"
            jump cheat_menu
        "Unlock All Achievements":
            $ achievements = set(["First Date","Belly Pet","Heartbreaker","Sentient Fat","Drained","Survivor","Marathon Date","Curious Cat","Belly Buddy","First Keep","Full House","Completionist","Flower Picker","Ghost Hunter","Big Spender","True Romance","Cold Rejection","Three Faces of Love","Daily Champion","Deja Vu"])
            "All achievements unlocked!"
            jump cheat_menu
        "Back":
            jump city_map

## ====== GALLERY ======
label gallery:
    scene black with dissolve
    "Gallery — View unlocked art"
    menu:
        "Character Portraits":
            jump gallery_portraits
        "Ending CGs":
            jump gallery_endings
        "Back":
            jump start

label gallery_portraits:
    "Portrait gallery coming soon."
    jump gallery

label gallery_endings:
    "Ending gallery coming soon."
    jump gallery

## ====== SETTINGS ======
label settings:
    scene black with dissolve
    "Settings"
    menu:
        "Text Speed: Fast":
            $ text_speed = 0.01
        "Text Speed: Normal":
            $ text_speed = 0.03
        "Text Speed: Slow":
            $ text_speed = 0.06
        "Toggle Animations ([animations_enabled])":
            $ animations_enabled = not animations_enabled
        "Toggle BGM ([bgm_enabled])":
            $ bgm_enabled = not bgm_enabled
            if not bgm_enabled:
                stop music
        "Reset All Save Data":
            "Are you sure? This will erase everything."
            menu:
                "Yes, reset everything":
                    $ reset_save_data()
                    "All data cleared."
                    jump start
                "No":
                    pass
        "Back":
            jump start
    jump settings

## ====== ACHIEVEMENTS ======
label achievements_screen:
    scene black with dissolve
    "Achievements: [len(achievements)]/20"
    $ ach_list = ["First Date","Belly Pet","Heartbreaker","Sentient Fat","Drained","Survivor","Marathon Date","Curious Cat","Belly Buddy","First Keep","Full House","Completionist","Flower Picker","Ghost Hunter","Big Spender","True Romance","Cold Rejection","Three Faces of Love","Daily Champion","Deja Vu"]
    $ ach_desc = {"First Date":"Complete your first date","Belly Pet":"Enter belly pet mode","Heartbreaker":"Unlock endings for every character","Sentient Fat":"Get absorbed by Fomo","Drained":"Get drained by Riko","Survivor":"Survive 5+ endless rounds","Marathon Date":"Survive 10+ endless rounds","Curious Cat":"Investigate a random encounter","Belly Buddy":"Join someone's belly","First Keep":"Keep a pet at 50% drain","Full House":"Riko holds all 10 pets","Completionist":"Unlock everything","Flower Picker":"Pick a glowing flower","Ghost Hunter":"Follow a ghostly whisper","Big Spender":"Spend 100+ coins","True Romance":"Good ending","Cold Rejection":"Bad ending","Three Faces of Love":"All 3 ending tiers","Daily Champion":"Complete a Daily Challenge","Deja Vu":"Complete New Game+"}
    python:
        for ach in ach_list:
            status = "✅" if ach in achievements else "🔒"
            desc = ach_desc.get(ach, "")
            renpy.say(None, f"{status} {ach}: {desc}", interact=False)
    ""
    jump start

## ====== CREDITS ======
label credits:
    scene black with dissolve
    "Date With Destiny"
    "Ren'Py Edition v1.0"
    ""
    "Original game by MariaTheGlaceon"
    "Ported from HTML PWA to Ren'Py"
    ""
    "Music: 'My Piano Sings' by John Holowach"
    "Music: 'The Garden' by Torley"
    "Both from the Internet Archive (CC license)"
    ""
    "All character art by MariaTheGlaceon & AI generation"
    ""
    "Thanks for playing!"
    jump start

## ====== HELPER FUNCTIONS ======
init python:
    def get_belly_reaction(char_id, action):
        ch = characters.get(char_id, {})
        reactions = ch.get('belly_reactions', {})
        action_reactions = reactions.get(action, ["..."])
        import random
        return random.choice(action_reactions)
    
    def get_ai_chat_response(char_id, user_input):
        ch = characters.get(char_id, {})
        chat_data = ch.get('chat', {})
        user_lower = user_input.lower()
        
        # Keyword-based response system (15 categories)
        categories = [
            ("greeting", ["hello", "hi", "hey", "yo", "sup"], "greeting"),
            ("feeling", ["how are you", "how do you feel", "you ok", "feeling"], "feeling"),
            ("name", ["your name", "who are you", "what are you"], "identity"),
            ("food", ["hungry", "eat", "food", "belly", "stomach"], "food"),
            ("escape", ["let me out", "free", "escape", "leave", "outside"], "escape"),
            ("comfort", ["comfortable", "warm", "cozy", "soft", "nice"], "comfort"),
            ("fear", ["scared", "afraid", "fear", "worried", "nervous"], "fear"),
            ("love", ["love", "care", "feelings", "like you", "adore"], "love"),
            ("squirm", ["squirm", "move", "struggle", "wiggle"], "squirm"),
            ("dark", ["dark", "can't see", "scared of dark", "light"], "dark"),
            ("sleep", ["sleep", "tired", "rest", "nap"], "sleep"),
            ("time", ["how long", "when", "time", "forever"], "time"),
            ("anger", ["hate", "stupid", "let go", "release me", "jerk"], "anger"),
            ("curious", ["what is", "why", "how come", "what happened"], "curious"),
            ("other", [], "default"),
        ]
        
        for cat_name, keywords, response_key in categories:
            if any(kw in user_lower for kw in keywords):
                responses = chat_data.get(response_key, ["..."])
                import random
                return random.choice(responses)
        
        responses = chat_data.get("default", ["Hmm... tell me more."])
        import random
        return random.choice(responses)
    
    def get_endless_scenario():
        import random
        scenarios = [
            {"text": "[ch_name] suggests a walk in the park.", "choices": [
                {"text": "Hold hands during the walk", "affection": 3, "reaction": "Aww, how sweet!"},
                {"text": "Walk independently", "affection": 1, "reaction": "Enjoying the fresh air?"},
                {"text": "Complain about the weather", "affection": -2, "reaction": "Hmph, party pooper."}
            ]},
            {"text": "[ch_name] asks what you want for dinner.", "choices": [
                {"text": "Whatever you're having", "affection": 2, "reaction": "Sharing is caring!"},
                {"text": "Something expensive", "affection": -1, "reaction": "Bold choice..."},
                {"text": "I'm not hungry", "affection": -2, "reaction": "More for me then."}
            ]},
            {"text": "[ch_name] wants to show you something.", "choices": [
                {"text": "Show me everything!", "affection": 3, "reaction": "I knew you'd be excited!"},
                {"text": "Maybe later", "affection": -2, "reaction": "Oh... okay."},
                {"text": "What is it first?", "affection": 1, "reaction": "It's a surprise!"}
            ]},
            {"text": "[ch_name] looks at you with a soft expression.", "choices": [
                {"text": "Lean in closer", "affection": 4, "reaction": "Your warmth feels nice..."},
                {"text": "Look away awkwardly", "affection": -1, "reaction": "Was it something I said?"},
                {"text": "Ask what's wrong", "affection": 2, "reaction": "Nothing's wrong. Everything's right."}
            ]},
        ]
        sc = random.choice(scenarios)
        sc["text"] = sc["text"].replace("[ch_name]", characters.get(current_character, {}).get("name", "They"))
        return sc
    
    def reset_save_data():
        global energy, max_energy, day, month, coins, time_of_day, current_location
        global current_character, affection, belly_pets, closeness, drain
        global achievements, cheat_mode, endless_score, endless_rounds
        global gifted, visited_dates, riko_collection, new_game_plus
        energy = 5; max_energy = 5; day = 1; month = 1; coins = 50
        time_of_day = "morning"; current_location = "home"; current_character = None
        affection = {}; belly_pets = []; closeness = {}; drain = {}
        achievements = set(); cheat_mode = False
        endless_score = 0; endless_rounds = 0
        gifted = {}; visited_dates = []; riko_collection = []; new_game_plus = False

## ====== TALK TREE ======
label talk_tree:
    $ ch = characters[current_character]
    $ talk_node = 0
    
label talk_node:
    if str(talk_node) not in ch.get('talk', {}):
        "You've covered everything for now."
        jump character_menu
    $ node = ch['talk'][str(talk_node)]
    scene black with dissolve
    "[node['text']]"
    if 'choices' in node:
        menu:
            for choice in node['choices']:
                $ label_text = choice['text']
                "[label_text]":
                    $ talk_node = choice.get('next', talk_node + 1)
                    if 'affection' in choice:
                        $ affection[current_character] = max(0, min(100, affection.get(current_character, 0) + choice['affection']))
                    jump talk_node
    else:
        $ talk_node += 1
        jump talk_node

## ====== BELLY JOIN (World Sim) ======
label belly_join:
    $ ch = characters[current_character]
    if current_character in belly_pets:
        "There's already someone in [ch['name']]'s belly!"
        jump character_menu
    "You ask to join [ch['name']]'s belly."
    if ch.get('pred', False):
        $ achievements.add("Belly Buddy")
        jump belly_mode
    else:
        "[ch['name']] isn't a predator. They can't hold you in their belly."
        jump character_menu
