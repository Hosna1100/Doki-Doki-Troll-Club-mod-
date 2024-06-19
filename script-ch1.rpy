label ch1_main:
    stop music fadeout 2.0
    scene bg club_day_e
    with dissolve_scene_full
    play music t2
    
    if choice =="shadow?":
        jump truth_reveal

label truth_reveal:
    mc "after some days of joke and laughter, club members started suspect Trollface that who he is and what his aim is." 
    show sayori c3 zorder 2 at t41
    s "you think who Trollface really is? I mean, he's always there and we never know anything about him." 
    show yuri h2 zorder 2 at t42
    y "I thought about it too. he always brings mystery for us but never says anything about himself." 
    show natsuki 5y zorder 2 at t43
    n "well, I think it's time to face it. we should make a plan and face the truth!" 
    show monika 3b zorder 2 at t44
    m "good idea, Natsuki. we can use Trollface's jokes to challenge him and face who he really is." 
    mc "alright, so what's our plan?"
    show sayori c3 zorder 2 at t41
    s 4r"we can create a difficult mystery for him! if he can't slove it, he should tell us who he really is!"
    show yuri h2 zorder 2 at t41 
    y 2b"and we can use our literature knowledge to make a mystery that a real literature club member can solve."
    show natsuki 4l zorder 2 at t43
    n 4l"great! let's start!"
    hide monika
    show natsuki 4s zorder 2 at t43
    show trollface 3b zorder 1 at t11
    trollface "haha, your waiting for my jokes again?"
    mc "today, is our turn to have a challenge for you, Trollface"
    trollface "really? well, let's see what you can do."
    s "خوب، این معمای ماست: 'چیزی که در کتاب‌ها زندگی می‌کند اما هرگز نفس نمی‌کشد، چیست؟'"
    trollface 1j"this question is so easy! the answer is..."
    trollface 2o"I...I don't know..."
    mc "so, now is time to tell the truth. Who you really are?"
    show trollface 3a at f11
    trollface "you really caught me. I am..."
    trollface 2b"یک تجسم از خواسته‌های شما برای سرگرمی و خنده هستم. من اینجا بودم تا به شما نشان دهم که گاهی اوقات، شما باید فقط بخندید و از زندگی لذت ببرید."
    mc "پس، همه این مدت، تو فقط می‌خواستی به ما کمک کنی تا شاد باشیم؟"
    trollface 1j"دقیقاً! و به نظر می‌رسد که کار من تمام شده است. شما همه یاد گرفته‌اید که چگونه خودتان را سرگرم کنید."
    mc "Trollface..."
    hide trollface
    show t_cg1
    mc "You're so kind..."
    mc "sorry for suspecting you..."
    hide t_cg1
    show t_cg1_exp1
    trollface "no problem..."
    trollface "حداقل خوشحالم که تونستم شادت کنم..."
    mc "واقعا دلم برای شما تنگ می شود...اگه توانستی بیا بازم بهمان سر بزن!"
    trollface "منم دلم برای همه ی شما تنگ می شود...اگه تونستم بازم میام!"
    hide t_cg1_exp1
    "all" "goodbye!!!!!"
    hide trollface
    "و اینطوری، ترول فیس ناپدید شد، اما خنده و شادی که او به باشگاه آورده بود، همیشه با ما می‌ماند."
    return

    if choice =="آرامش؟":
        jump dark_truth

label dark_truth:
    "بعد از هفته‌هایی پر از خنده و شوخی، اعضای باشگاه شروع به تردید کردند. شاید ترول فیس اهداف دیگری داشته باشد..."
    show sayori 1g zorder 2 at f41
    s "دوستان، من نگرانم. شاید ترول فیس دلایل دیگری برای حضورش داشته باشد."
    show yuri 2f zorder 2 at t42
    y "بله، من هم احساس می‌کنم که چیزهایی پنهان است. مثل اینکه هر شوخی یک پیام مخفی دارد."
    show natsuki 1e zorder 2 at h43
    n "ما باید کاری کنیم. نمی‌توانیم اجازه دهیم که او با ما بازی کند!"
    show monika 4i zorder 2 at t44
    m "درسته. باید حقیقت را کشف کنیم. باید بفهمیم ترول فیس واقعاً چه نقشه‌ای دارد."
    mc "خوب، چطور می‌خواهیم این کار را انجام دهیم؟"
    s "ما باید او را به چالش بکشیم. باید از او بخواهیم که حقیقت را بگوید."
    y "و اگر نگفت، ما باید او را مجبور کنیم."
    hide yuri
    hide monika
    hide sayori
    show trollface 1b zorder 2 at t11
    trollface "هاها، آماده برای شوخی جدید من هستید؟"
    mc "نه، امروز ما برای تو یک سوال داریم، ترول فیس. تو واقعاً کیستی و چه می‌خواهی؟"
    trollface "چه سوال جالبی! فکر می‌کنید آماده شنیدن جواب هستید؟"
    show trollface 2i zorder 2 at f11
    trollface "من نه تنها برای خنده آمده‌ام. من آمده‌ام تا شما را آزمایش کنم، تا ببینم آیا واقعاً می‌توانید با واقعیت‌های تاریک دنیایتان روبرو شوید."
    mc "واقعیت‌های تاریک؟ تو دقیقاً چه منظوری داری؟"
    trollface "هر شوخی من یک درس بود، یک آزمایش. و شما همه آن را نادیده گرفتید، فقط خندیدید و ادامه دادید."

    trollface "اما حالا که می‌دانید، دیگر نمی‌توانید به سادگی بخندید. دیگر نمی‌توانید از حقیقت فرار کنید."
    mc "پس تو می‌خواستی به ما درسی بدهی؟"
    trollface 3h"بله، و درس من تمام نشده است. من همیشه اینجا خواهم بود، یادآوری کننده حقیقتی که شما سعی در فراموشی آن دارید."
    hide trollface
    mc "و با این حال، ترول فیس ناپدید شد. اما سایه‌ای که او بر جای گذاشت، همیشه با ما خواهد بود."
    return

    if choice =="پایان بازی؟":
        jump twisted_intentions

label twisted_intentions:
    "روزها می‌گذرند و شوخی‌های ترول فیس دیگر مثل قبل سرگرم‌کننده نیستند. اعضای باشگاه شروع به نشان دادن رفتارهای عجیبی می‌کنند."
    show sayori 3h zorder 2 at t41
    s "من... من نمی‌دانم چرا، اما احساس بدی دارم. انگار که دیگر نمی‌توانم بخندم."
    show yuri 2r zorder 2 at t42
    y "و من همیشه عصبانی هستم! این شوخی‌ها... آنها دیگر خنده‌دار نیستند."
    show natsuki 5f zorder 2 at t43
    n "من هم همینطور! این ترول فیس فقط می‌خواهد ما را عصبانی کند!"
    show monika 2i zorder 2 at t44
    m "من فکر می‌کنم ترول فیس نقشه‌ای دارد. او نمی‌خواهد فقط ما را بخنداند، او می‌خواهد ما را تغییر دهد."
    mc "پس باید با او روبرو شویم. باید بفهمیم او واقعاً چه می‌خواهد."
    s "بله، ما باید حقیقت را بدانیم."
    y "ما نمی‌توانیم اجازه دهیم که او با احساسات ما بازی کند."
    show trollface 2a zorder 2 at t11
    trollface "هاها، آماده برای شوخی جدید من هستید؟"
    mc "نه، ما می‌خواهیم بدانیم تو واقعاً چه می‌خواهی، ترول فیس."
    trollface "چه جالب! شما واقعاً فکر می‌کنید که می‌توانید حقیقت را کشف کنید؟"
    show trollface 1x zorder 2 at t11
    trollface "من اینجا نیستم فقط برای خنده. من اینجا هستم تا شما را تغییر دهم، تا شما را به چیزی که هرگز فکر نمی‌کردید می‌توانید باشید، تبدیل کنم."
    mc "تغییر ما؟ به چه صورت؟"
    trollface "با هر شوخی، من روح شما را تیره‌تر می‌کنم. با هر خنده، من شما را از درون تغییر می‌دهم."
    trollface "و حالا که شما متوجه شده‌اید، دیگر نمی‌توانید به سادگی برگردید. شما دیگر همان افراد قبلی نیستید."
    mc "پس تو می‌خواستی ما را بدخلق کنی؟"
    trollface "دقیقاً! و کار من هنوز تمام نشده است. من همیشه اینجا خواهم بود، یادآوری کننده تغییری که شما تجربه کرده‌اید."
    hide trollface
    mc "و با این حال، ترول فیس ناپدید شد. اما تأثیر او بر روی ما همیشه باقی خواهد ماند."
    return


# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
