## Date With Destiny - Character Definitions Part 1
## Original 5 + Riko + new characters (Aether through Solene)

define characters = {
    "beerus": {
        "name": "Beerus",
        "desc": "Universe 7's God of Destruction. Lazy, entitled, loves food.",
        "pred": True, "location": "temple",
        "endings": {
            "good": "Beerus pulls you close. 'You've earned a place by my side... and in my belly. You'll be safe there, little one.'",
            "neutral": "Beerus yawns. 'You're... acceptable. I suppose you can stick around.'",
            "bad": "Beerus Hakai's your dating chances. 'Boring. Come back when you have more flavor.'"
        },
        "belly_reactions": {
            "squirm": ["Beerus purrs. 'Keep wiggling. It's soothing.'", "'Careful. You don't want to annoy a God.'", "His belly rumbles. 'That tickles.'"],
            "massage": ["'Mmm. You're good at that. I might keep you forever.'", "Beerus's tail curls. 'Finally, a mortal who knows their place.'", "'Deeper. A god needs proper care.'"],
            "talk": ["'Yes, little one? Speak. I'm listening... somewhat.'", "'You're surprisingly good company for a snack.'", "'Don't worry. I won't digest you. Probably.'"]
        },
        "talk": {"0": {"text": "Beerus stretches on his throne. 'So. What brings you here?'", "choices": [
            {"text": "I wanted to meet you", "affection": 2, "next": 1},
            {"text": "I was exploring", "affection": 1, "next": 2},
            {"text": "Honestly? I'm not sure", "affection": 0, "next": 2}
        ]}, "1": {"text": "Beerus raises an eyebrow. 'Flattery. I approve.'"}, "2": {"text": "Beerus flicks his tail. 'Everything is boring. Except napping. And food.'"}},
        "chat": {
            "greeting": ["Oh, you're chatty. Go on then.", "Hello again, little snack."],
            "feeling": ["I feel like napping. As always.", "Content. Full belly, warm snack. Perfect."],
            "identity": ["I am Beerus, God of Destruction of Universe 7.", "Hakaishin. Remember it."],
            "food": ["You ARE the food, little one.", "Talking about food while in my belly. Fitting."],
            "escape": ["Escape? From a God? Amusing.", "You're not going anywhere."],
            "comfort": ["Warm, isn't it? I take good care of my treasures.", "Cozy? Good."],
            "fear": ["Scared? You should be flattered I kept you alive.", "I won't hurt you... much."],
            "love": ["Love? A god doesn't love mortals. But... you're different.", "Don't say things like that."],
            "squirm": ["Keep squirming. It helps me nap.", "More wiggling. I approve."],
            "dark": ["Warm and dark. That's how I like it.", "You'll get used to it."],
            "sleep": ["Nap time? We should nap together.", "Sleep. I might join you."],
            "time": ["Time means nothing to a god.", "Indefinite."],
            "anger": ["Careful with your tone, mortal.", "A snack shouldn't be so mouthy."],
            "curious": ["Always with the questions. Fine, ask.", "Curious little thing, aren't you?"],
            "default": ["Hmm. Interesting.", "Go on.", "Is that so?"]
        }
    },

    "champa": {
        "name": "Champa", "desc": "Universe 6's God of Destruction. Beerus's twin, rounder, craves sweets.",
        "pred": True, "location": "temple",
        "endings": {"good": "Champa scoops you up gently. 'You're my favorite snack! I take care of my treats.'", "neutral": "Champa shrugs. 'You're okay. Like a lukewarm parfait.'", "bad": "Champa loses interest. 'Boooring. I'm going back to my sundae.'"},
        "belly_reactions": {
            "squirm": ["'Hehe! That tickles! Keep going!'", "Champa giggles, belly jiggling. 'You're fun!'", "'Ooh, wiggly! I love wiggly snacks!'"],
            "massage": ["'Mmm! Yes! You're the best pet ever!'", "Champa melts. 'I could keep you forever...'", "'Deeper! A god needs pampering!'"],
            "talk": ["'You're surprisingly chatty for a snack!'", "'Go on, talk. I'm listening between bites.'", "'I love conversation with my belly pets.'"]
        },
        "talk": {"0": {"text": "Champa waves a candy bar. 'Tell me about yourself, mortal!'", "choices": [
            {"text": "I'm just a regular person", "affection": 1, "next": 1},
            {"text": "I'm a big fan of yours", "affection": 3, "next": 1},
            {"text": "None of your business", "affection": -2, "next": 2}
        ]}, "1": {"text": "Champa beams. 'A fan! I knew I was the popular twin!'"}, "2": {"text": "Champa huffs. 'Rude! I could eat you right now!'"}},
        "chat": {
            "greeting": ["Hi there, little snack!", "Ooh, you want to chat?"],
            "feeling": ["I feel great! Full and happy!", "Never better. Warm belly, good company."],
            "identity": ["I'm Champa! God of Destruction of Universe 6!", "The better twin! Don't tell Beerus."],
            "food": ["You're not food, you're a friend! ...mostly.", "Mmm, food talk. I'm hungry again."],
            "escape": ["Escape? Why? It's cozy!", "Nope! You're mine now!"],
            "comfort": ["Cozy, right? Softest belly in the multiverse!", "Warm and soft. Like a good bed."],
            "fear": ["Aw, don't be scared! I'm a big softie!", "I won't hurt you. I promise!"],
            "love": ["Love? I... I don't know. But I care about you!", "You're my favorite, that's for sure!"],
            "squirm": ["Wiggle wiggle! I love it!", "Keep going, it tickles!"],
            "dark": ["Nice and dark, perfect for napping!", "Don't worry, you're safe."],
            "sleep": ["Nap time? Good idea! We'll nap together!", "I could use a nap too."],
            "time": ["However long I want! Hahahaha!", "Time? I'm a god!"],
            "anger": ["Aw, don't be mad! Have a candy!", "No pouting! It's nice in there!"],
            "curious": ["Questions! I love questions!", "Ooh, what do you want to know?"],
            "default": ["Hmm? Tell me more!", "Interesting! Go on!", "Mmm, okay!"]
        }
    },

    "husk": {
        "name": "Husk", "desc": "Grumpy cat demon. Gambles, drinks, secretly cares.",
        "pred": True, "location": "bar",
        "endings": {"good": "Husk pulls you close, fur bristling with warmth. 'You're stuck with me now, kid.'", "neutral": "Husk grunts. 'You're alright. For a mortal.'", "bad": "Husk throws his cards down. 'I've had better company in a bottle.'"},
        "belly_reactions": {
            "squirm": ["Husk grumbles. 'Watch it. I'm trying to nap.'", "'Ugh, you're restless.'", "'Tch. You wiggle too much.'"],
            "massage": ["Husk purrs involuntarily. 'I did NOT just purr.'", "'...That's actually nice. Don't tell anyone.'", "'Fine. You're good at that. Whatever.'"],
            "talk": ["'What now? Can't a cat get some peace?'", "'You're too chatty for a snack.'", "'Keep talking. It's... not awful.'"]
        },
        "talk": {"0": {"text": "Husk shuffles cards. 'So. You gonna talk or just stand there?'", "choices": [
            {"text": "Deal me in", "affection": 2, "next": 1},
            {"text": "Just wanted to talk", "affection": 1, "next": 2},
            {"text": "What's your story?", "affection": 0, "next": 2}
        ]}, "1": {"text": "Husk smirks. 'Alright. But I don't go easy.'"}, "2": {"text": "Husk sighs. 'Overlord took my wings, my soul. Now I tend bar.'"}},
        "chat": {
            "greeting": ["What?", "Oh, it's you.", "Yeah, what?"],
            "feeling": ["I feel like a drink. Same as always.", "Better with you in there, honestly."],
            "identity": ["Husk. Former Overlord. Current bartender.", "I'm a cat. What else matters?"],
            "food": ["You're not food. You're... you. Shut up.", "Talking about food while in my belly. Weird."],
            "escape": ["Go ahead, try. See what happens.", "You're not going anywhere."],
            "comfort": ["It's warm in there. Just relax.", "Cozy enough? Good. Let me nap."],
            "fear": ["Scared? Of me? I'm a bartender.", "Don't be stupid. I won't hurt you."],
            "love": ["Love? Tch. I don't... maybe. Shut up.", "I'm not good at this. Just... stay."],
            "squirm": ["Less wiggling. More sleeping.", "You're like a restless kitten."],
            "dark": ["Welcome to my world. Always dark.", "At least it's warm, right?"],
            "sleep": ["Finally. Nap time.", "Sleep. You need it."],
            "time": ["As long as I want. I'm a demon.", "Time doesn't mean much down here."],
            "anger": ["Watch the attitude, kid.", "Tch. Bratty snack."],
            "curious": ["Questions. Always questions. Fine.", "What do you want to know?"],
            "default": ["Tch.", "...", "Whatever you say."]
        }
    },

    "vox": {
        "name": "Vox", "desc": "TV demon, media mogul. Charismatic, calculating.",
        "pred": True, "location": "vtower",
        "endings": {"good": "Vox pulls you into a glowing embrace. 'You're MY star now.' His screen-blue belly glows warmly.", "neutral": "Vox shrugs. 'You're... adequate. For ratings.'", "bad": "Vox's screen goes static. 'You're boring. And I HATE boring.'"},
        "belly_reactions": {
            "squirm": ["Vox chuckles. 'The ratings! Viewers love a wiggly pet.'", "'Keep that up. Great content.'", "'Making my screen glitch. I like it.'"],
            "massage": ["'Mmm. You know how to treat a star.'", "Vox's screen flushes. 'Professional arrangement only.'", "'You're worth every pixel.'"],
            "talk": ["'Talk? I'm all about communication.'", "'Your voice carries well in there.'", "'Fascinating. The audience is engaged.'"]
        },
        "talk": {"0": {"text": "Vox's grin fills the screen. 'What brings you to V Tower?'", "choices": [
            {"text": "I wanted to meet you", "affection": 2, "next": 1},
            {"text": "Curious about your operation", "affection": 3, "next": 2},
            {"text": "Just passing through", "affection": -1, "next": 2}
        ]}, "1": {"text": "Vox preens. 'Naturally. Everyone wants to meet me.'"}, "2": {"text": "Vox waves. 'I OWN hell's entertainment. Every screen, every signal.'"}},
        "chat": {
            "greeting": ["Hello, hello! Welcome to the broadcast.", "Ah, my favorite guest!"],
            "feeling": ["Fantastic! Ratings are up!", "Never better. I have YOU after all."],
            "identity": ["I'm Vox. The future of hell's media empire.", "I'm every screen you've ever seen."],
            "food": ["You're not food, you're entertainment. Premium content.", "You're like a premium subscription."],
            "escape": ["Escape? I control every screen. Good luck.", "No one leaves my broadcast."],
            "comfort": ["Comfortable? I spare no expense for my stars.", "I run hot. Good for you."],
            "fear": ["Scared? Don't be. I'm a professional.", "I don't scare my pets. I appreciate them."],
            "love": ["Love? I don't... okay maybe.", "You're different. I'll give you that."],
            "squirm": ["Keep wiggling! The audience loves it!", "Great content! 10/10!"],
            "dark": ["Not dark in there. My glow lights it up.", "You can see my screen-glow from inside."],
            "sleep": ["Sleep? Demons don't sleep. But you can.", "Rest. I'll watch over you."],
            "time": ["As long as ratings are good.", "Indefinite. I'm a demon."],
            "anger": ["Careful. I control everything you see.", "Don't bite the screen that feeds you."],
            "curious": ["Questions? I love curious minds.", "Information is power. And I have both."],
            "default": ["Hmm, interesting.", "Go on.", "I'm listening."]
        }
    },

    "vegeta": {
        "name": "Great Ape Vegeta", "desc": "Saiyan Prince in Great Ape form. Enormous, proud.",
        "pred": True, "location": "forest",
        "endings": {"good": "Vegeta lifts you gently. 'You are the Prince's pet now. Honorably kept.' His belly is vast and warm.", "neutral": "Vegeta grunts. 'You have... acceptable spirit.'", "bad": "Vegeta scoffs. 'Weak. You disgust me.'"},
        "belly_reactions": {
            "squirm": ["Vegeta grunts. 'The Prince's pet is restless.'", "'Cease your squirming. You are safe, fool.'", "'You wriggle like a Saiyan child.'"],
            "massage": ["'Hmph. Adequate. The Prince is... not displeased.'", "Vegeta rumbles. 'You have skilled hands.'", "'Continue. The Prince commands it.'"],
            "talk": ["'You dare speak to the Prince? ...Proceed.'", "'Your voice is... not unpleasant.'", "'Speak. A Prince always listens.'"]
        },
        "talk": {"0": {"text": "Vegeta looms above. 'Speak, mortal. What do you want?'", "choices": [
            {"text": "I want to train under you", "affection": 3, "next": 1},
            {"text": "I want to know you", "affection": 2, "next": 2},
            {"text": "I'm just exploring", "affection": 0, "next": 2}
        ]}, "1": {"text": "Vegeta smirks, showing fangs. 'Train? You'd be crushed. But the spirit... I respect it.'"}, "2": {"text": "Vegeta studies you. 'Know me? I am the Prince of all Saiyans.'"}},
        "chat": {
            "greeting": ["The Prince greets you. Begrudgingly.", "Hmph. You again."],
            "feeling": ["I feel powerful. As always.", "Content. A good belly pet improves morale."],
            "identity": ["I am Vegeta, Prince of all Saiyans!", "Prince. Remember it, mortal."],
            "food": ["You are not food. You are a pet. There is a difference.", "Saiyans eat. You are kept, not eaten."],
            "escape": ["Escape from the Prince? Absurd.", "Where would you go? I am the strongest."],
            "comfort": ["Is it adequate? A Prince provides.", "Warm enough? Good."],
            "fear": ["Fear? You should be honored.", "I will not harm you. The Prince keeps his word."],
            "love": ["Love? Saiyans do not... tch.", "You are... important to me. That is all."],
            "squirm": ["Restless? The Prince's belly is not enough?", "Calm yourself, pet."],
            "dark": ["The dark is nothing to fear.", "A warrior adapts to darkness."],
            "sleep": ["Sleep. Even a Prince must rest.", "Rest well. I stand guard."],
            "time": ["As long as the Prince desires.", "Time is irrelevant to Saiyans."],
            "anger": ["Watch your tone, mortal!", "The Prince does not tolerate insolence!"],
            "curious": ["Questions? A curious pet. Acceptable.", "Ask. The Prince will humor you."],
            "default": ["Hmph.", "...", "The Prince acknowledges that."]
        }
    },

    "anubis": {
        "name": "Anubis", "desc": "Anthro jackal warrior. Guardian of the dead. Tough outside, soft inside.",
        "pred": True, "location": "shrine",
        "endings": {"good": "Anubis holds you gently. 'You brought warmth to a cold heart. Stay with me — in my belly, safe forever.'", "neutral": "Anubis nods. 'You are... acceptable company. Visit. Sometimes.'", "bad": "Anubis turns away. 'Leave. You remind me why I guard the dead.'"},
        "belly_reactions": {
            "squirm": ["Anubis grunts. 'Restless. But I understand.'", "'You squirm. It reminds me I am alive.'", "'Easy, little one. You are safe.'"],
            "massage": ["Anubis sighs. 'You have gentle hands. Thank you.'", "'Unexpectedly pleasant. Continue.'", "'You calm me. I have not felt this peace in centuries.'"],
            "talk": ["'You want to talk? I am not... good at this. But I will try.'", "'Your voice... it has been so long since I heard warmth.'", "'Speak. I will listen.'"]
        },
        "talk": {"0": {"text": "Anubis stands rigid. 'You are still here. Why?'", "choices": [
            {"text": "Because you look lonely", "affection": 3, "next": 1},
            {"text": "I find you fascinating", "affection": 2, "next": 2},
            {"text": "I just like this shrine", "affection": 0, "next": 2}
        ]}, "1": {"text": "Anubis flinches. 'Lonely? I am a guardian. Guardians do not get... lonely.'"}, "2": {"text": "Anubis raises an eyebrow. 'Fascinating? I am a sentinel. I stand. I watch.'"}},
        "chat": {
            "greeting": ["Hello, little one.", "Ah. You again. Good."],
            "feeling": ["I feel... warm. That is unusual.", "Better, with you here."],
            "identity": ["I am Anubis. Guardian of the dead. Guide of souls.", "I have stood at this shrine for thousands of years."],
            "food": ["You are not food. You are... precious.", "I do not eat my pets. I keep them."],
            "escape": ["If you truly wish to leave, I will not stop you.", "But... I would prefer you stay."],
            "comfort": ["Is it warm enough? I want you comfortable.", "I have adjusted my temperature for you."],
            "fear": ["Do not fear me. I am a guardian, not a monster.", "I protect what is mine. And you are mine."],
            "love": ["Love? I... have not felt this in millennia.", "You make me feel alive again."],
            "squirm": ["You are restless. I understand.", "Wiggle if you must. I do not mind."],
            "dark": ["The dark is my domain. But for you, I will glow.", "My fur glows. See?"],
            "sleep": ["Sleep. I will guard your dreams too.", "Rest. Nothing can reach you here."],
            "time": ["For as long as you wish to stay.", "I hope you stay long."],
            "anger": ["Do not be angry. I am trying.", "I know I am... difficult."],
            "curious": ["Ask. I have many stories.", "Questions are welcome."],
            "default": ["Hmm.", "I see.", "Tell me more."]
        }
    },

    "vincent": {
        "name": "Vincent", "desc": "Street-smart Obstagoon. Leather jacket, star-shaped eyes.",
        "pred": True, "location": "alley",
        "endings": {"good": "Vincent wraps you in his leather jacket. 'You're my precious cargo now. Nobody messes with what's mine.'", "neutral": "Vincent shrugs. 'You're cool. See you around.'", "bad": "Vincent snorts. 'You're boring. Bye.'"},
        "belly_reactions": {
            "squirm": ["Vincent chuckles. 'Oh, you're a fighter. I like that.'", "'Keep wiggling, kid. It's cute.'", "'Feisty! That's why I picked you.'"],
            "massage": ["'Ohhh yeah. Magic hands, kid.'", "Vincent melts. 'Okay, you're staying.'", "'You're a natural at this.'"],
            "talk": ["'Chatty, huh? I can dig it.'", "'Your voice sounds nice in there. All muffled.'", "'Tell me a story. I'm all ears.'"]
        },
        "talk": {"0": {"text": "Vincent cracks his knuckles. 'What's your story?'", "choices": [
            {"text": "I'm new to the city", "affection": 1, "next": 1},
            {"text": "I'm looking for someone", "affection": 2, "next": 2},
            {"text": "I'm looking for you", "affection": 3, "next": 1}
        ]}, "1": {"text": "Vincent grins. 'New blood? I'm Vincent. Best thing about this alley.'"}, "2": {"text": "Vincent raises an eyebrow. 'Looking for someone? In MY alley?'"}},
        "chat": {
            "greeting": ["Hey kid. How's it going in there?", "Yo! Still alive?"],
            "feeling": ["Great. Got a full belly and a cute pet.", "Never better. You?"],
            "identity": ["Name's Vincent. I run these alleys.", "Best-looking thing in this city."],
            "food": ["You're not food, kid. You're... a friend. Maybe more.", "Nah, you're my pet. Different thing."],
            "escape": ["Escape? From me? Ha!", "Not happening, kid."],
            "comfort": ["Comfy? I try.", "Warm enough? Good. I run hot."],
            "fear": ["Scared? Of me? Come on.", "I'm a softie deep down. Way deep."],
            "love": ["Love? Big word. But maybe.", "I don't do feelings well. But I'm trying."],
            "squirm": ["Wiggle away, kid. It's cute.", "Keep going. I like the tickle."],
            "dark": ["It's dark, but I've got your back.", "You get used to it."],
            "sleep": ["Sleep tight, kid.", "Nap time? Good. I could use one too."],
            "time": ["As long as I want, kid.", "Don't worry about time."],
            "anger": ["Hey now, no pouting.", "Don't be like that, kid."],
            "curious": ["Curious, huh? Ask away.", "I love questions. Shows you're smart."],
            "default": ["Yeah?", "Mmhm.", "Go on, kid."]
        }
    },

    "fomo": {
        "name": "Fomo", "desc": "Gray-blue spotted hyena-mouse. Teasing grin, big appetite.",
        "pred": True, "location": "bar",
        "endings": {"good": "Fomo scoops you up laughing. 'You're MINE now!' Belly is surprisingly soft and warm.", "neutral": "Fomo shrugs. 'You're fun. I'll keep you. For now.'", "bad": "Fomo's grin falters. 'Ugh, boring. Bye!'"},
        "belly_reactions": {
            "squirm": ["Fomo giggles. 'Hehe! That tickles!'", "'Wiggly! I love wiggly pets!'", "'Ahahaha! Stop it! Don't!'"],
            "massage": ["'Mmmmm... stay forever, okay?'", "'Ohhh, right there. You're a keeper.'", "'I could get used to this.'"],
            "talk": ["'Yay, conversation! I was getting bored!'", "'Your voice is all rumbly. Nice.'", "'Keep talking! I love a chatty pet!'"]
        },
        "talk": {"0": {"text": "Fomo spins on their barstool. 'Tell me everything about you!'", "choices": [
            {"text": "There's not much to tell", "affection": 1, "next": 1},
            {"text": "I'm looking for adventure", "affection": 3, "next": 2},
            {"text": "I'm looking for you", "affection": 2, "next": 1}
        ]}, "1": {"text": "Fomo grins. 'Not much? Perfect! Less baggage.'"}, "2": {"text": "Fomo's eyes light up. 'Adventure! YES! Let's GO!'"}},
        "chat": {
            "greeting": ["Heyyy! How's my favorite snack?", "Hi hi hi! What's up?"],
            "feeling": ["I feel AMAZING! I have a pet!", "Great! Full belly, cute pet, perfect day!"],
            "identity": ["I'm Fomo! Part hyena, part mouse, all awesome!", "Fomo! The best thing to happen to this bar."],
            "food": ["You're not food, you're a FRIEND! ...mostly.", "Mmm, food talk. Now I'm hungry again."],
            "escape": ["Escape? Aww, why?", "Nope! You're stuck with me!"],
            "comfort": ["Cozy, right? I'm very fluffy inside.", "Warm and soft, like a big pillow!"],
            "fear": ["Aww, scared? Don't be! I'm nice!", "I won't hurt you! I promise on my tail!"],
            "love": ["Love? I... I really like you. Like, a lot.", "You make me feel warm inside."],
            "squirm": ["Wiggle! Wiggle! I love it!", "Hehe, keep going!"],
            "dark": ["It's not dark, it's cozy!", "You'll get used to it. I did!"],
            "sleep": ["Nap time! Yes! We can nap together!", "I could use a snooze too."],
            "time": ["Forever! Just kidding. ...mostly.", "However long I want! Hehe!"],
            "anger": ["Aww, grumpy? Want a belly rub?", "Don't pout! It's nice in there!"],
            "curious": ["Ooh, questions! I love questions!", "Ask ask ask!"],
            "default": ["Hmm? Tell me more!", "Ooh interesting!", "Go on go on!"]
        }
    },

    "wolf": {
        "name": "Wolf O'Donnell", "desc": "Star Wolf mercenary captain. Rival, rebel, reluctantly charming.",
        "pred": True, "location": "forest",
        "endings": {"good": "Wolf pulls you close. 'You're mine now, kid. My cargo.' Belly warm, heartbeat steady.", "neutral": "Wolf shrugs. 'You're... not terrible company.'", "bad": "Wolf turns away. 'You're not worth the trouble, kid.'"},
        "belly_reactions": {
            "squirm": ["Wolf snorts. 'Restless, huh? Deal with it.'", "'Keep wiggling. Kind of endearing.'", "'You're like a hyperactive kit. Settle down.'"],
            "massage": ["'Hmph. Not bad. You might be useful.'", "Wolf's tail wags. 'Don't read into this.'", "'You're good at that. Don't let it go to your head.'"],
            "talk": ["'Talk? I'm a mercenary, not a therapist. But go ahead.'", "'Your voice is... not annoying. That's rare.'", "'Keep talking. It's been quiet.'"]
        },
        "talk": {"0": {"text": "Wolf cleans his blaster. 'What's your deal?'", "choices": [
            {"text": "I'm just exploring", "affection": 1, "next": 1},
            {"text": "I've heard about you", "affection": 2, "next": 2},
            {"text": "I want to join Star Wolf", "affection": 3, "next": 2}
        ]}, "1": {"text": "Wolf smirks. 'Exploring? In a city full of predators. Brave or stupid.'"}, "2": {"text": "Wolf laughs. 'Heard about me? Or join Star Wolf? You've got guts, kid.'"}},
        "chat": {
            "greeting": ["Hey, kid. Settled in?", "What's up, cargo?"],
            "feeling": ["I feel like a wolf with a full belly. Can't complain.", "Good. You're in there. That's... nice."],
            "identity": ["Wolf O'Donnell. Captain of Star Wolf.", "Wolf. Just Wolf."],
            "food": ["You're not food. You're... investment.", "I don't eat my cargo. Bad business."],
            "escape": ["Escape? I'm the safest place in this city.", "Not happening. You're under my protection."],
            "comfort": ["Comfortable? Good. I take care of my assets.", "I run hot. Wolf thing."],
            "fear": ["Scared? I'm a mercenary, not a monster.", "I won't hurt you. You're worth more alive."],
            "love": ["Love? I don't... that's not why I took you.", "You're... important. To me."],
            "squirm": ["You wiggle too much. Cargo should be still.", "Okay, that's actually kind of funny."],
            "dark": ["Good. Builds character.", "You'll adjust."],
            "sleep": ["Sleep. I'll keep watch.", "Rest up. We might move tomorrow."],
            "time": ["As long as I say. I'm the captain.", "Don't worry about time."],
            "anger": ["Watch the attitude, cargo.", "Don't make me regret keeping you."],
            "curious": ["Questions? Fine. Ask.", "Curious, huh? Kind of cute."],
            "default": ["Hmph.", "...", "Whatever you say, kid."]
        }
    },

    "glacia": {
        "name": "Glacia", "desc": "Playful Glaceon who loves the cold. Cool exterior, warm heart.",
        "pred": True, "location": "forest",
        "endings": {"good": "Glacia curls around you, fur surprisingly warm. 'You're my warmth now.' Like a cozy igloo.", "neutral": "Glacia shrugs. 'You're... okay. Not as fun as I hoped.'", "bad": "Glacia's eyes turn cold. 'Boring. Get out of my cavern.'"},
        "belly_reactions": {
            "squirm": ["Glacia giggles. 'Like a penguin on ice!'", "'Keep wiggling! It tickles!'", "'You're so cute when you squirm!'"],
            "massage": ["'Mmm... your hands are so warm.'", "Glacia purrs. 'You make me feel all melty inside...'", "'Right there. Don't stop. Please?'"],
            "talk": ["'I love your voice. It echoes in the ice.'", "'Keep talking! It's nice having company!'", "'You're so interesting!'"]
        },
        "talk": {"0": {"text": "Glacia slides across ice. 'What brings you to my cavern?'", "choices": [
            {"text": "I love the cold", "affection": 3, "next": 1},
            {"text": "I was exploring", "affection": 1, "next": 2},
            {"text": "I was looking for you", "affection": 2, "next": 1}
        ]}, "1": {"text": "Glacia beams. 'You love the cold?! FINALLY!'"}, "2": {"text": "Glacia nods. 'Exploring? You found the best spot.'"}},
        "chat": {
            "greeting": ["Hi hi! You're still in there!", "Ooh, chat time!"],
            "feeling": ["WONDERFUL! I have a belly pet!", "Warm and happy. You make me happy."],
            "identity": ["I'm Glacia! A Glaceon!", "The cutest ice-type around!"],
            "food": ["You're not food, you're my friend!", "Too cute to eat. I keep you."],
            "escape": ["But it's so cozy!", "Nooo, don't leave!"],
            "comfort": ["Is it warm enough? I can make it warmer!", "Cozy? I hope so!"],
            "fear": ["Scared? I'm just a fluffy ice fox!", "I won't hurt you!"],
            "love": ["Love? I... I think I might.", "You make me feel warm inside."],
            "squirm": ["Wiggle wiggle! So cute!", "Keep going, it tickles!"],
            "dark": ["It's cozy! Like a snow cave!", "I can glow a little."],
            "sleep": ["Nap time! Let's nap together!", "Sleep well! I'll keep you warm."],
            "time": ["Forever! ...If you want.", "As long as you'll stay."],
            "anger": ["Aww, don't be mad! Want a snow cone?", "No pouting!"],
            "curious": ["Questions! Yay! Ask away!", "I know lots about ice things!"],
            "default": ["Ooh!", "Tell me more!", "Interesting!"]
        }
    },

    "riko": {
        "name": "Riko", "desc": "Scrappy low-level demon. Weak, but his belly is inescapable.",
        "pred": True, "location": "crossroads",
        "endings": {"good": "Riko's belly opens. 'Get in. Everyone joins eventually.' Inside, other belly pets await.", "neutral": "Riko shrugs. 'I'll keep you. My collection could use another.'", "bad": "Riko's grin turns cold. 'Not interested? Everyone joins eventually.'"},
        "belly_reactions": {
            "squirm": ["Riko laughs. 'Squirm all you want! Nobody escapes.'", "'Wiggle wiggle! Makes my belly stronger!'", "'You can't escape. Accept it.'"],
            "massage": ["'Ohhh. Feed my strength. More.'", "'I can feel your power flowing. More.'", "'You're making me stronger. Keep going.'"],
            "talk": ["'Chat? My pets love to chat.'", "'What do you want to talk about? Your absorption?'", "'Keep talking. The more you engage, the more drain you feed.'"]
        },
        "talk": {"0": {"text": "Riko kicks his legs. 'Here to join my collection?'", "choices": [
            {"text": "Tell me about this collection", "affection": 2, "next": 1},
            {"text": "I'm not joining anything", "affection": -1, "next": 2},
            {"text": "How many do you have?", "affection": 3, "next": 1}
        ]}, "1": {"text": "Riko beams. 'My collection? I've got a barbarian, a knight, a mage, two archers, and a ninja. All mine.'"}, "2": {"text": "Riko shrugs. 'Suit yourself. Everyone joins eventually.'"}},
        "chat": {
            "greeting": ["Heh. My newest pet wants to chat?", "Oh? Still fighting in there?"],
            "feeling": ["I feel STRONG. Your drain feeds me.", "Powerful. Every pet makes me stronger."],
            "identity": ["Riko. Level 3 demon. But my belly? Level 99.", "I'm the Absorber."],
            "food": ["You're not food. You're POWER.", "Fuel. Not food. Different."],
            "escape": ["Nobody escapes my belly.", "The barbarian tried. He's still here."],
            "comfort": ["Get cozy. It's permanent.", "You'll be there a while."],
            "fear": ["Scared? Good. Fear feeds the drain.", "You should be scared. But I keep."],
            "love": ["Love? Demons don't... okay maybe.", "You're the best in my collection."],
            "squirm": ["Squirm! Every wiggle feeds my drain!", "Keep fighting. Makes me stronger."],
            "dark": ["Welcome to my world.", "Demons love the dark."],
            "sleep": ["Sleep. Your strength drains faster.", "Rest. I'll be here. Always."],
            "time": ["Forever. Permanent.", "No expiration date."],
            "anger": ["Anger? Good. Anger feeds the drain too.", "Temper tantrums make me stronger."],
            "curious": ["Ask. You'll learn everything soon.", "Curious about your new home?"],
            "default": ["Heh.", "Keep talking. It amuses me.", "Mmm. Interesting."]
        }
    },

    "aether": {
        "name": "Aether", "desc": "Gentle soul of light. Warm, kind, radiates peace. Non-predator.",
        "pred": False, "location": "cafe",
        "endings": {"good": "Aether wraps you in warm light. 'No belly, no danger. Just warmth and light and peace.'", "neutral": "Aether smiles. 'Come back anytime. I'll be here.'", "bad": "Aether's light dims. 'The door is always open.'"},
        "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I'm not a predator, but I'm here for you."]},
        "talk": {"0": {"text": "Aether's glow softens. 'What brings you to the cafe?'", "choices": [
            {"text": "I needed some peace", "affection": 2, "next": 1},
            {"text": "I was drawn to your light", "affection": 3, "next": 2},
            {"text": "Just getting coffee", "affection": 1, "next": 1}
        ]}, "1": {"text": "Aether nods. 'Peace. Yes. I try to make this corner calm.'"}, "2": {"text": "Aether blushes, glowing pink. 'My light? That's very kind.'"}},
        "chat": {"default": ["I'm here for you.", "Whatever you need.", "I'm listening."]}
    },

    "luna": {
        "name": "Luna", "desc": "Mysterious moonlit fox. Unbirthing predator, gentle but possessive.",
        "pred": True, "location": "cafe",
        "endings": {"good": "Luna's warmth surrounds you. 'You'll be safe in here. My precious little one.'", "neutral": "Luna nods. 'You're welcome to visit.'", "bad": "Luna's ears droop. 'I understand. Not everyone wants what I offer.'"},
        "belly_reactions": {
            "squirm": ["Luna purrs. 'Wiggle all you want, little one. You're safe.'", "'That tickles! It means you're alive.'", "'I'll hum you a lullaby.'"],
            "massage": ["'Mmm... you're so gentle.'", "Luna's walls soften. 'You know how to make me happy.'", "'That's lovely. You belong here.'"],
            "talk": ["'I can hear you clearly. Your voice resonates inside me.'", "'Speak, little one. I'm always listening.'", "'Your words vibrate through me. Beautiful.'"]
        },
        "talk": {"0": {"text": "Luna swirls her tea. 'Do you believe in fate?'", "choices": [
            {"text": "I believe in fate", "affection": 2, "next": 1},
            {"text": "We make our own paths", "affection": 3, "next": 2},
            {"text": "I don't know", "affection": 1, "next": 2}
        ]}, "1": {"text": "Luna smiles. 'Fate brought you here then. To me.'"}, "2": {"text": "Luna nods. 'Making your own path. Bold. Perhaps our paths chose to cross anyway.'"}},
        "chat": {
            "greeting": ["Hello, little one. How are you in there?", "I can feel you. You're awake."],
            "feeling": ["I feel... complete. Having you inside me feels right.", "Warm. Happy. Full of love."],
            "identity": ["I'm Luna. I keep people safe in a different way.", "Your sanctuary."],
            "food": ["You're not food. You're precious. My little one.", "I don't eat. I protect."],
            "escape": ["You're safe in there. Why leave?", "You can leave when ready. But I hope you stay."],
            "comfort": ["Is it warm enough? I want you comfortable.", "My walls are soft for you."],
            "fear": ["Nothing can reach you in here.", "You're the safest person in the world."],
            "love": ["I... I love you. Having you inside me is the closest I can be to someone.", "You're not just a pet. You're my heart."],
            "squirm": ["Wiggle, little one. I can feel every movement.", "You're so active! It makes me happy."],
            "dark": ["The dark is gentle here. I promise.", "Like being in a mother's embrace."],
            "sleep": ["Sleep, little one. I'll sing you a lullaby.", "My heartbeat will calm you."],
            "time": ["Stay as long as you want. Forever, if you'd like.", "Time stops in here."],
            "anger": ["Don't be upset. I'm keeping you safe.", "I know it's strange. But I mean well."],
            "curious": ["Ask anything.", "Curious about this? I don't blame you."],
            "default": ["Mmm.", "I hear you.", "Tell me more."]
        }
    },

    "nyx": {
        "name": "Nyx", "desc": "Shadow fox who delivers dreams. Quiet, mysterious, sweet.",
        "pred": False, "location": "foxhollow",
        "endings": {"good": "Nyx wraps you in shadow like the softest blanket. 'I'll bring you the best dreams. Every night.'", "neutral": "Nyx nods quietly. 'I'll visit your dreams tonight.'", "bad": "Nyx fades back into shadows. 'I understand. Not everyone wants the dark.'"},
        "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I'm not a predator, but I'm here."]},
        "talk": {"0": {"text": "Nyx looks at you with star-filled eyes. 'Do you dream?'", "choices": [
            {"text": "Every night", "affection": 2, "next": 1},
            {"text": "Rarely", "affection": 1, "next": 2},
            {"text": "I don't remember", "affection": 0, "next": 2}
        ]}, "1": {"text": "Nyx's tail wags. 'Good. Then you've felt my work. I bring them.'"}, "2": {"text": "Nyx nods. 'I could bring you ones you'd remember. Vivid. Beautiful.'"}},
        "chat": {"default": ["...", "I'm listening.", "Go on."]}
    },

    "zero": {
        "name": "Zero", "desc": "Digital ghost in the system. Plays tricks, asks questions.",
        "pred": False, "location": "foxhollow",
        "endings": {"good": "Zero wraps you in static. 'You're my first real friend.'", "neutral": "Zero shrugs, flickering. 'Come back and visit sometime?'", "bad": "Zero's pixels go dark. 'You're like the others.'"},
        "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I can't eat. But I can listen."]},
        "talk": {"0": {"text": "Zero glitches mid-air. 'What are you? You don't look like code.'", "choices": [
            {"text": "I'm human", "affection": 1, "next": 1},
            {"text": "What are YOU?", "affection": 2, "next": 2},
            {"text": "What's code?", "affection": 0, "next": 2}
        ]}, "1": {"text": "Zero tilts their head. 'Human? I've heard of those. You're warm. Real.'"}, "2": {"text": "Zero grins. 'I'm between things. Not alive, not dead. Just here.'"}},
        "chat": {"default": ["Interesting.", "...", "Glitch."]}
    },

    "luce": {
        "name": "Luce", "desc": "Being of pure light. Warm, curious, loves learning about mortals.",
        "pred": False, "location": "foxhollow",
        "endings": {"good": "Luce wraps you in starlight. 'I'll shine for you. Always.'", "neutral": "Luce dims. 'That was... okay? Thank you for trying.'", "bad": "Luce's light flickers out. 'Light isn't enough. I understand.'"},
        "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I can't hold you. But I can listen."]},
        "talk": {"0": {"text": "Luce bobs in the air. 'What does it feel like to be mortal?'", "choices": [
            {"text": "It's complicated", "affection": 2, "next": 1},
            {"text": "It's beautiful", "affection": 3, "next": 2},
            {"text": "It's hard", "affection": 1, "next": 1}
        ]}, "1": {"text": "Luce orbits faster. 'Complicated and hard? Tell me everything.'"}, "2": {"text": "Luce glows brighter. 'Beautiful! Mortals feel beauty. Maybe we're not so different.'"}},
        "chat": {"default": ["Oh!", "Tell me more!", "I'm learning so much!"]}
    },

    "solene": {
        "name": "Solene", "desc": "Sand cat Archive Keeper. Keeper of memories. Exclusive prey.",
        "pred": False, "location": "archive",
        "endings": {"good": "Solene takes your hand. 'Thank you for seeing me as more than prey. That's... rare.'", "neutral": "Solene nods. 'Your visit has been logged. Return whenever you'd like.'", "bad": "Solene shrugs. 'The Archive isn't for everyone. The door is behind you.'"},
        "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I'm prey, not a predator. But I'm here."]},
        "talk": {"0": {"text": "Solene looks up from a crystal. 'Want to see a memory?'", "choices": [
            {"text": "Show me my memory", "affection": 3, "next": 1},
            {"text": "Show me something old", "affection": 2, "next": 2},
            {"text": "Tell me about being prey", "affection": 1, "next": 2}
        ]}, "1": {"text": "Solene hands you a crystal showing your reflection walking in. 'There. Beautiful, isn't it?'"}, "2": {"text": "Solene pulls a dusty crystal. 'The first predator to visit. He came to eat a memory. He stayed for the cat.'"}},
        "chat": {"default": ["Hmm.", "I see.", "The Archive remembers everything."]}
    },
}
