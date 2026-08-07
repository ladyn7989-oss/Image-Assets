## Date With Destiny - Beastars Characters (Part 2)
## Louis, Legoshi, Riz, Bill, Gohin

init python:
    characters.update({
        "louis": {
            "name": "Louis",
            "desc": "Red deer, Cherryton Academy star actor. Proud, driven, hiding vulnerability.",
            "pred": False, "location": "cherryton",
            "endings": {
                "good": "Louis removes his mask. 'You see me. The real me. No one else does.' He takes your hand. 'Stay. Not as a pet. As... a partner.'",
                "neutral": "Louis nods curtly. 'You're... observant. I can appreciate that.'",
                "bad": "Louis turns cold. 'You see nothing. Like everyone else. Leave.'"
            },
            "belly_reactions": {"squirm": ["..."], "massage": ["..."], "talk": ["I'm not a predator. I'm a deer. But I'll listen."]},
            "talk": {"0": {"text": "Louis stands on stage. 'What do you want to know?'", "choices": [
                {"text": "Why acting?", "affection": 2, "next": 1},
                {"text": "What's the Horn Conglomerate?", "affection": 1, "next": 2},
                {"text": "Are you happy?", "affection": 3, "next": 1}
            ]}, "1": {"text": "Louis looks at empty seats. 'Acting? Because on stage, I can be someone else. Someone not expected to be perfect.'"}, "2": {"text": "Louis straightens. 'The Conglomerate is my family's business. I'm expected to take over. Whether I want to or not.'"}},
            "chat": {"default": ["Hmm.", "I see.", "Interesting."]}
        },

        "legoshi": {
            "name": "Legoshi",
            "desc": "Gray wolf, Cherryton Academy stage crew. Shy, kind, struggles with instincts.",
            "pred": True, "location": "cherryton",
            "endings": {
                "good": "Legoshi's tail wags despite himself. 'You're not afraid. Of me. Of this.' He gently pulls you close. 'I'll be careful. The gentlest wolf you'll ever meet.'",
                "neutral": "Legoshi nods, ears flat. 'Thanks for... not running. I'll see you around?'",
                "bad": "Legoshi retreats into shadows. 'I understand. Wolves are scary. Go.'"
            },
            "belly_reactions": {
                "squirm": ["Legoshi's ears flatten. 'S-sorry! Am I squishing you?'", "'You're moving... is that okay?'", "'P-please don't squirm too much. It triggers things. But I'll be okay!'"],
                "massage": ["Legoshi whimpers softly. 'That's... really nice. Thank you.'", "'You're so gentle. You're... really brave.'", "'I'll try to stay calm. Your hands are warm.'"],
                "talk": ["'You want to talk? Sure! I mean... yes.'", "'Your voice sounds nice in there. Muffled but warm.'", "'Nobody's ever wanted to talk inside my belly. You're different.'"]
            },
            "talk": {"0": {"text": "Legoshi fidgets with his tail. 'What do you want to talk about?'", "choices": [
                {"text": "Tell me about yourself", "affection": 2, "next": 1},
                {"text": "Do you like being a wolf?", "affection": 3, "next": 2},
                {"text": "Just company is fine", "affection": 1, "next": 1}
            ]}, "1": {"text": "Legoshi scratches behind his ear. 'Myself? I'm nothing special. Just a wolf in stage crew.'"}, "2": {"text": "Legoshi goes quiet. 'Being a wolf is... complicated. The instincts are loud. The world expects you to be a monster.'"}},
            "chat": {
                "greeting": ["O-oh, hi. Are you okay in there?", "H-hey. You're... talking?"],
                "feeling": ["I feel... nervous. But good nervous.", "Honestly? Happy. Nobody's ever wanted to stay."],
                "identity": ["I'm Legoshi. Just a wolf. Nothing special.", "Legoshi. Stage crew. Gray wolf."],
                "food": ["You're not food! I mean... you are, technically, but I don't... you're not.", "I don't think of you as food. I promise."],
                "escape": ["If you want to leave, I'll let you out. I'd never force this.", "You can go. I just... I hope you don't want to."],
                "comfort": ["Is it okay in there? I'm not too tight?", "Warm enough? I can try to be softer."],
                "fear": ["Are you scared? I'm sorry. I'll be gentler.", "Please don't be afraid. I'm not dangerous. Really."],
                "love": ["Love? I... I might. For you. Is that weird?", "You make me feel things I've never felt. Gentle things."],
                "squirm": ["You're wiggling. Do you want out? No? Okay. I'm fine.", "It tickles. But in a nice way."],
                "dark": ["It's dark in there, isn't it? I'm sorry.", "I know the dark well. I live in the shadows."],
                "sleep": ["You can sleep. I'll keep you safe. That's a promise.", "Rest. I'll be here when you wake up."],
                "time": ["Stay as long as you want. I'd like that.", "I don't mind. I have nowhere to be either."],
                "anger": ["Are you mad? I'm sorry. I'm not good at this.", "I understand if you're upset."],
                "curious": ["Questions? Sure. I'm not interesting, but... ask away.", "You want to know about me? Really?"],
                "default": ["Mm.", "...sorry, I'm not good at talking.", "Is that okay?"]
            }
        },

        "riz": {
            "name": "Riz",
            "desc": "Brown bear, Cherryton Academy. Massive, gentle, hiding a dark secret.",
            "pred": True, "location": "cherryton",
            "endings": {
                "good": "Riz cups you gently in massive paws. 'I'll be careful. I'll be so careful.' His belly is vast and warm. 'You're safe here.'",
                "neutral": "Riz nods slowly. 'You're... kind. Not many people give me a chance.'",
                "bad": "Riz looks away, eyes dark. 'You should go. Before I... before something happens. Please.'"
            },
            "belly_reactions": {
                "squirm": ["Riz rumbles softly. 'It's okay. You can wiggle. I'll be gentle.'", "'You're so small in there. But I can feel you.'", "'Careful. I don't want to... I'm trying to be careful.'"],
                "massage": ["Riz's breathing slows. 'That's... really nice. Nobody touches a bear gently.'", "'You're so gentle. It makes me want to protect you.'", "'Mmm. I could fall asleep like this.'"],
                "talk": ["'You want to talk? I'm not great at conversation. But I'll try.'", "'Your voice is so small in there. But I can hear every word.'", "'Nobody's ever wanted to talk to the big scary bear. You're different.'"]
            },
            "talk": {"0": {"text": "Riz looks down at his paws. 'You're not afraid of me. Why?'", "choices": [
                {"text": "You don't seem scary", "affection": 2, "next": 1},
                {"text": "I see the real you", "affection": 3, "next": 2},
                {"text": "I don't judge", "affection": 2, "next": 1}
            ]}, "1": {"text": "Riz's eyes soften. 'Not scary? I'm a bear. Everything about me is built to frighten. But thank you.'"}, "2": {"text": "Riz looks away. 'The real me? The real me is a bear who hurt his best friend. You still want to see that?'"}},
            "chat": {
                "greeting": ["Oh. Hi. Are you... okay in there?", "I can hear you. I'm listening."],
                "feeling": ["I feel... peaceful. You're warm and safe.", "Calm. For the first time in a long time."],
                "identity": ["I'm Riz. A brown bear. I'm trying to be better.", "Riz. Just Riz. Not a monster."],
                "food": ["You're not food. You're... precious. I won't hurt you.", "I've done enough harm. You're safe."],
                "escape": ["If you want to leave, I understand. I'll let you out gently.", "I won't keep you against your will."],
                "comfort": ["Is it warm enough? I'm a big bear. I run hot.", "Comfortable? Good. I'd never crush you."],
                "fear": ["Scared? I understand. A bear this big... it's natural.", "I won't hurt you. Not again."],
                "love": ["Love? I... I don't deserve that. But if you mean it...", "You make me want to be gentle. Just for you."],
                "squirm": ["It's okay. Wiggle if you need to. I'm gentle.", "I can feel you. You're so small."],
                "dark": ["It's dark in there. I'm sorry. But you're safe.", "I know the dark well. It's not always scary."],
                "sleep": ["Rest. I'll guard you. A bear's promise.", "Sleep. Nothing will reach you."],
                "time": ["Stay as long as you need. I'll be here.", "I have nowhere to be. I'm patient."],
                "anger": ["I understand. Being inside a bear... it's a lot.", "I'm sorry. I'll do better."],
                "curious": ["Ask anything. I have nothing to hide. Not from you.", "Questions are okay. I'll answer honestly."],
                "default": ["Mmm.", "I see.", "I'm listening."]
            }
        },

        "bill": {
            "name": "Bill",
            "desc": "Tiger, Cherryton Academy. Cocky, athletic, secretly insecure.",
            "pred": True, "location": "cherryton",
            "endings": {
                "good": "Bill pulls you close, grin softening. 'You actually see ME. Not just the tiger. Me.' His belly is warm. 'You're stuck with me now. Deal with it.'",
                "neutral": "Bill shrugs, grin back. 'You're alright. For a non-tiger. Don't make it weird.'",
                "bad": "Bill's grin turns cold. 'Boring. I thought you were different. See ya.'"
            },
            "belly_reactions": {
                "squirm": ["Bill chuckles. 'Feisty! I like that.'", "'You're like a little mouse in there. Adorable.'", "'Hey, that tickles! Watch the stripes!'"],
                "massage": ["'Ohhh yeah. Right there. You're good at this, kid.'", "Bill purrs, then catches himself. 'That was... a growl. A content growl.'", "'Okay, you're definitely staying.'"],
                "talk": ["'Chatty, huh? Fine, talk to me.'", "'Your voice sounds all rumbly in there. Kind of cool.'", "'Keep talking. I'm actually listening. Don't tell anyone.'"]
            },
            "talk": {"0": {"text": "Bill flexes in the hallway. 'So? Impressed yet?'", "choices": [
                {"text": "Very impressed", "affection": 3, "next": 1},
                {"text": "Try harder", "affection": 1, "next": 2},
                {"text": "I see through the act", "affection": 2, "next": 2}
            ]}, "1": {"text": "Bill grins wider. 'Damn right. I'm the total package.'"}, "2": {"text": "Bill's grin falters. 'The act? What act? This IS me. Mostly.'"}},
            "chat": {
                "greeting": ["Hey kid. What's up in there?", "Yo! Still kicking?"],
                "feeling": ["I feel GREAT. Got a belly pet. Life's good.", "Pretty awesome. You make it better."],
                "identity": ["Bill. The tiger. The star. Remember it.", "I'm Bill. Cherryton's best actor."],
                "food": ["You're not food. You're... a friend snack.", "Nah, you're my pet. Pets aren't food."],
                "escape": ["Escape? From a tiger? Good luck.", "Nah, you're not going anywhere."],
                "comfort": ["Comfy? I've got the warmest belly at Cherryton.", "Tiger metabolism. You're welcome."],
                "fear": ["Scared? I'm harmless! Mostly harmless!", "I won't eat you. I already did. Ha!"],
                "love": ["Love? I... pff. Maybe. If you're lucky.", "You're different from the others."],
                "squirm": ["Wiggle wiggle! Ha, it tickles!", "Keep going, it's fun."],
                "dark": ["Dark in there? Tigers see in the dark though.", "You'll get used to it."],
                "sleep": ["Nap time? Good idea.", "Rest up. Tomorrow's another day."],
                "time": ["As long as I want! I'm a tiger.", "Stay a while. Ha!"],
                "anger": ["Hey, no pouting. You're MY pet now.", "Come on, it's not that bad!"],
                "curious": ["Questions? Sure, ask away. I know everything.", "Curious about me? Naturally."],
                "default": ["Mmhm.", "Sure sure.", "Yeah yeah."]
            }
        },

        "gohin": {
            "name": "Gohin",
            "desc": "Giant panda, back-alley doctor. Gruff, protective, saves lives.",
            "pred": True, "location": "cherryton",
            "endings": {
                "good": "Gohin pulls you in with surprising gentleness. 'You're my patient now. My responsibility. I don't lose patients.' His belly is like a warm hospital bed.",
                "neutral": "Gohin nods. 'You're... not terrible company. Come back if you get hurt. Or bored. Whatever.'",
                "bad": "Gohin waves dismissively. 'If you're not bleeding, you're wasting my time. Out.'"
            },
            "belly_reactions": {
                "squirm": ["Gohin grunts. 'Stop squirming. Your vitals are good. Squirm if you need to.'", "'Restless? Normal.'", "'You're surprisingly healthy for someone inside a panda.'"],
                "massage": ["'Mmph. That's... medically beneficial. Continue.'", "Gohin actually relaxes. 'I never get massages. This is... nice.'", "'Your technique could use work. But the effort is noted.'"],
                "talk": ["'You want to talk? Fine. I'm not going anywhere. Neither are you.'", "'I've heard a lot of confessions in this clinic. Go ahead.'", "'Talk. I'm listening. Doctor-patient confidentiality applies.'"]
            },
            "talk": {"0": {"text": "Gohin examines a chart. 'What brings you to my clinic? You're not bleeding.'", "choices": [
                {"text": "I wanted to meet you", "affection": 1, "next": 1},
                {"text": "I heard you help people", "affection": 3, "next": 2},
                {"text": "I was just exploring", "affection": 0, "next": 1}
            ]}, "1": {"text": "Gohin grunts. 'Meet me? I'm a doctor, not a celebrity. But... fine.'"}, "2": {"text": "Gohin looks up, surprised. 'Help people? I do what needs doing. Someone has to.'"}},
            "chat": {
                "greeting": ["What? You need something?", "Oh, it's you. Still in there."],
                "feeling": ["I feel fine. I always feel fine. Work to do.", "Better with you safe in there. Don't tell anyone."],
                "identity": ["Gohin. Doctor. Panda. That's it.", "I'm a back-alley doctor. I save lives."],
                "food": ["You're not food. You're a patient. Different.", "I don't eat my patients. That's malpractice."],
                "escape": ["Leave if you want. I'm not a jailer.", "But I'd prefer you stay. For medical reasons."],
                "comfort": ["Comfortable? Your vitals are stable. Good.", "Panda fur is excellent insulation."],
                "fear": ["Scared? Of a doctor? I'm the safest person you know.", "I won't hurt you. I save people."],
                "love": ["Love? I don't... that's not why I brought you in.", "You're... important. For medical reasons. Shut up."],
                "squirm": ["Your heart rate is elevated. Calm down.", "Normal movement. Nothing to worry about."],
                "dark": ["Dark in there? That's normal. You'll adapt.", "I can't turn on a light in my belly. Sorry."],
                "sleep": ["Sleep? Fine. I'll monitor your breathing.", "Rest. Doctor's orders."],
                "time": ["I'll let you out when your vitals stabilize.", "Stay until you're healed. Or forever."],
                "anger": ["Don't be difficult. I'm trying to help.", "Frustration noted. And ignored."],
                "curious": ["Questions? I'm a doctor. I have answers.", "Curious about medicine? I can teach you."],
                "default": ["Mmph.", "...", "Noted."]
            }
        }
    })
