label ch1_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t4
    mc "امروز یک روز عادی در باشگاه ادبیات به نظر می‌رسد..."
    show trollface 1b zorder 1 at t11
    trollface "سلام دوستان! آماده برای کمی سرگرمی هستید؟"
    show natsuki 5w zorder 2 at t41
    n "اوه نه، نه دوباره!"
    show yuri 1f zorder 3 at t42
    y "چه شوخی‌ای در ذهن داری این بار، ترول فیس؟"
    trollface 1a"فقط یک معمای کوچک! اگر می‌توانید حلش کنید، یک جایزه ویژه در انتظارتان است!"
    show sayori 1r zorder 4 at h43
    s "من همیشه برای چالش‌های جدید آماده‌ام!"
    show monika 3r zorder 5 at t44
    m "بیایید ببینیم این بار چه در سر داری."
    hide monika
    hide sayori
    hide natsuki
    hide yuri

    trollface "خوب، اینجا معمای من: 'من چیزی دارم که شما همیشه دنبالش هستید و هرگز پیدایش نمی‌کنید. من چیستم؟'" 
    mc "این که خیلی ساده است! پاسخ..."
    menu:
        "پایان بازی؟":
            mc "پایان بازی؟"
            trollface "نه، اما نزدیک بود! امتحان دیگری بدهید!"
        "سایه؟":
            mc "سایه؟"
            trollface "دقیقاً! شما آن را حدس زدید! جایزه شما یک دور کامل خنده با من است!"
        "آرامش؟":
            mc "آرامش؟"
            trollface "اوه، این خیلی عمیق بود! شاید دفعه بعد!"

    trollface 3j"خوب، این برای امروز کافی است! منتظر شوخی بعدی من باشید!"
    hide trollface
    "هر روز با ترول فیس یک ماجراجویی جدید است..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
