label ch0_main:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t4
    mc "looks like today is a normal day in literature club..."
    show trollface 1b zorder 1 at t11
    trollface "hello my friends! ready for some entertainment?"
    show natsuki 5w zorder 2 at t41
    n "oh no! not again!"
    show yuri 1f zorder 2 at t42
    y "what kind of joke you have in mind, Trollface?"
    trollface 1a"just a little mystery! if you can, solve it! an award is expecting you!"
    show sayori 1r zorder 2 at h43
    s "I'm always ready for new challenges!"
    show monika 3r zorder 2 at t44
    m "let's see what you have in head, this time."
    hide monika
    hide sayori
    hide natsuki
    hide yuri

    trollface "well, here's my mystery :'I have something that you always looking for it but you never find it. what am I?" 
    mc "it's so easy! the answer is..."
    menu:
        "game ending?":
            mc "game ending?"
            trollface "no, but it was close. try again next time!"
        "shadow?":
            mc "shadow?"
            trollface "exactly! you guessed that! your price is a full period laughing with me!"
        "secerity?":
            mc "secerity?"
            trollface "oh, it was so deep! maybe next time."

    trollface 3j"okay, enough for today! wait for my next joke!"
    hide trollface
    "everyday with Trollface is a new adventure..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
