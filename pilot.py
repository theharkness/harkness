print "You're alone."
print "The last thing you remember is..."
print "Well nothing. The last thing you remember is nothing."
print "You're standing in the middle of the street."
print "Headlights approach."
print "Prove you're a sentient being. Press 1 to jump out of the way before you're killed."

sentient = raw_input("> ")

if sentient == "1":
    print "You're sentient! You survive!"
    print "You jump deftly out of the way of the truck."
    print "Well, as deftly as anyone can jump when they're about to get run over."
    print "You do some sort of barrel roll out of the way, bumping your head on a bucket of nails."
    print "Speaking of which, why the hell is there a bucket of nails on the side of the road?"
    print "Type \"nails\" to explore the bucket. Type \"nah\" to keep trudging along."

    nails = raw_input(" >")

    if nails == "nails":
        print "You pick up the bucket of nails."
        print "It oozes with some mixture of blood, mucus, and rusty nails."
        print "Being the disturbed traveler you are, you plunge your hand in deeper."
        print "And discover a rusty scalpel!"
        print "This will be great for performing spur-of-the-moment surgeries."
        print "You mutter something about always wanting a DIY facelift."


    elif nails == "nah":
        print "Who gives a shit about nails anyway?"
        print "Probably just AIDS infected syringes and cockroach droppings in there anyway."
        print "You wander down the road whistling makeshift sonatas and kicking a rock."
        print "A drifter on the side of the road asks if you've got any change."
        print "You can either type \"give\" to hook the guy up, or \"nope\" if you"
        print "think he should just go out and get a job in this dystopian wasteland."


        drifter = raw_input(" >")

        if drifter == "give":
            print "He thanks you and gives you an absolutely filthy coat to wear."
            print "You probably don't fully grasp how filthy this coat actually is."
            print "While most coats are sewn from threads, you know, shit like alpaca fur,"
            print "this coat is fastened from syringes."
            print "Really dirty syringes."

        if drifter == "nope":
            print "He figures, what the hell, let's fight then."
            print "He shouts something that sounds vaguely Yiddish while rushing you."
            print "As he tackles you to the ground you feel the sharp throbbing pain of a thousand needles."
            print "Turns out he was wearing a coat made out of syringes."
            print "Really dirty syringes."
            print "You slowly stand up and brush off the syringes currently stabbing you"
            print "in the neck and the groin and the eyes and the groin and also the groin."
            print "You pick up one of those dirty syringes and hold it like a knife."
            print "The drifter's eyes widen, as he realizes what this is escalating into."
            print "A dirty syringe fight."
            print "He reaches into the cardboard box behind him and lo and behold,"
            print "he retrieves a giant, filthy, possibly sentient pair of defibrillators."
            print "Where the hell did this drifter get all this filthy medical equipment?"
            print "\"Looks like you brought a syringe to a defibrillator fight, sonny\" he says."
            print "Kinda pisses you off too, 'cause this ain't your daddy."
            print "Type \"run\" to resort to your basest instict, you pitiful coward."
            print "Type \"attack\" to gut this fool like a fish with your crusty AIDS syringe."
            print "Type \"disarm\" to try some real Indiana Jones shit."

            defibrillator = raw_input(" >")

            if defibrillator == "run":
                print "Probably the right move, you snivelling coward."

            elif defibrillator == "attack":
                print "Now that's what I'm talking about!"
                print "As it turns out, the only thing dumber than fighting with a dirty syringe"
                print "is trying to use uncharged defribilators to molest a stranger."
                print "The drifter collapses on the ground from a well placed stab to the groin."
                print "You can steal his defibrillator by typing \"steal\" or type \"walk\""
                print "to keep on walkin' along."

                steal = raw_input(" >")

                if steal == "steal":
                    print "You reach for his defibrillators and then BZZZPPPERRRGHGHGHGH"
                    print "you experience the most awesome nonsense electrical shock from uncharged defibrillators"
                    print "that anyone has likely ever experienced."
                    print "You spend an eight of a second pondering the irony of the situation"
                    print "before exploding into a million pieces."

                elif steal == "walk":
                    print "You keep walking along until you run into a chupacabra."
                    print "He gives you the whole \"halt who goes there?\" spiel"
                    print "but you're pretty unfazed. I mean you just crushed a drifter in syringe combat."
                    print "Nothing gets past you."
                    print "The chupacabra rolls on its back and challenges you to a game of cat chess."
                    print "Wait a minute. Didn't he just say he was a chupacabra?"
                    print "You ask, for clarity's sake. \"Are you a cat or a chupacabra\""
                    print "He ponders this for a moment before saying, \"guess\"."
                    print "Type \"cat\" if you think he's a cat; type \"chupacabra\" if you"
                    print "think he's a chupacabra."

                    cat = raw_input(" >")

                    if cat == "cat":
                        print "He kills you."

                    elif cat == "chupacabra.":
                        print "He kills you."
                        #added an else so shitposters can choose anything they want and get a reasonable response
                    else:
                        print "He strangles you with your own shitty life choices."


            elif defibrillator == "disarm":
                print "You rush up to the drifter, dropping your syringe to try and grab the defribilators."
                print "Turns out he doesn't need the stupid things."
                print "He hits you with a sweet right cross. Followed by a left."
                print "And then something straight out of WWE."
                print "He picks you up and breaks your back over his knee."
                print "You collapse onto the hard rock ground."
                print "You don't die, but you do become a handicapped apprentice drifter."
                print "You study the arts of drifterism from your friend, the drifter who broke your back."
                print "He makes you call him Yoda and holds you sometimes, while you cry yourself to sleep."

            else:
                print "Doing %s might have seemed like a good idea, but here's what happened:" % defibrillator
                print "You trip over a rock and the syringes already sticking out of your body"
                print "stab deeper into a bunch of organs you needed to survive."
                print "Which means you didn't. Survive, that is. "
#added an "else" for the drifter track
        else:
            print "You literally die from indecision."
            print "You're so bad at making decisions you contract AIDS...from yourself."



else:
    print "Come on you retard. It ain't gonna get any easier than that."
    print "The headlights turn out to be connected to a van. Going 60 mph."
    print "You die."
