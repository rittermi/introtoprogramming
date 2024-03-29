﻿
image silk = "makesilk.jpg"
image spice = "cassia.jpg"
image market = "ricemerchant.jpg"
image route = "route.jpg"
image teamerchant = "teaman.jpg"
image tea = "teafield.jpg"
image greatwall = "greatwallcaravan.jpg"
image caravan = "caravan.jpg"
image desert = "gobidesert.jpg"
image mongolians = "mongolians.jpg"
image fight = "fight.jpg"
image barter = "barter.jpg"
image oasis = "oasis.jpg"


define tm = Character("Tea Merchant")
define slkm = Character("Silk Merchant")
define spcm = Character("Spice Merchant")
define cd = Character("Caravan Leader")

define number = (renpy.random.randint(20, 100))
define homecasualty = (renpy.random.randint(1, 10))
define awaycasualty = (renpy.random.randint(1, 10))
init:
    pass

label start:
    scene market
    "You are about to make your way along one of the routes of the Silk Road to sell your wares. What are you selling?"

    $ yuan = 0


    menu:
        "Silk":
            jump silk
        "Tea":
            jump tea
        "Spices":
            jump spices

    label silk:
        scene silk

        slkm "Excellent choice! China began using silk as a currency during the Han Dynasty and China kept the process of making it a secret for hundreds of years."
        jump travel

    label tea:
        scene tea
        show teamerchant at right
        tm "Awesome! Tea is China's oldest export. People had to boil water to kill any pathogens that might be living in the water and adding tea leaves greatly improves the flavor."
        jump travel

    label spices:
        scene spice
        spcm "The world was driven by the spice trade for centuries. One popular spice from China is called 'cassia'. It's similar to cinnamon."
        jump travel

    label travel:
        scene route
        cd "While most people do not travel the whole silk road, you're ambitious. Here are cities we'll be stopping in including our current location, Xian."
        scene greatwall
        cd "As you can see, we'll be traveling along the Great Wall for protection for as long as we can."
        scene caravan
        cd "Unfortunately, the Wall ends before we reach our first city around the Gobi Dessert. We'll have to keep a closer eye our for dangers."
        scene desert
        "Your caravan successfully makes it to the Gobi Desert"
        cd "We should reach an oasis soon. Keep your eyes open."
        scene mongolians
        "You see a group of riders approaching"
        menu:
            "Fight them off":
                jump fight
            "Attempt to talk with them":
                jump talk

    label fight:
        scene fight
        "You manage to fight them off with some bloodshed on both sides"
        "Your merchandise it all accounted for"
        "[homecasualty] people in your caravan died"
        "You found [awaycasualty] raiders among the dead"
        jump oasis
    label talk:
        scene barter
        "You manage to convince them to spare you by giving up some of your merchandise"
        "No one is harmed"
        "You lost [number] yuan worth of merchandise"
        jump oasis
    label oasis:
        scene oasis
        cd "We made it! Time to rest for a bit."



    $ randevent = renpy.random.choice(["Encounter Bandits", "Encounter Snow Leopard", "Lose Merchandise"])
