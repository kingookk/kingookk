import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AarohiX import app


@app.on_message(filters.command(["اغاني","ميوزك"], ""))
async def music(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],
        
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
   
        [InlineKeyboardButton("السـورس 🤍", url=f"https://t.me/source _av")],
        
    ])
    await m.reply_text("↢ اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^music2 (\\d+)$"))
async def music2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],
 
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

        [InlineKeyboardButton("السـورس 🤍", url=f"https://t.me/source _av")],
        
    ])
    await m.message.edit_text("↢ اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^araby (\\d+)$"))
async def araby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مهرجانات 🔊", callback_data="mhrgan " + str(m.from_user.id))] +
        [InlineKeyboardButton("ادهم نابلسي 🔊", callback_data="adham " + str(m.from_user.id))],
        [InlineKeyboardButton("ويجز 🔊", callback_data="wegz " + str(m.from_user.id))] +
        [InlineKeyboardButton("تامر حسني 🔊", callback_data="tamer " + str(m.from_user.id))],
        [InlineKeyboardButton("مروان موسي 🔊", callback_data="marwan " + str(m.from_user.id))] +
        [InlineKeyboardButton("حماده هلال 🔊", callback_data="helal " + str(m.from_user.id))],
        [InlineKeyboardButton("بابلو 🔊", callback_data="bablo " + str(m.from_user.id))] +
        [InlineKeyboardButton("اصاله 🔊", callback_data="asala " + str(m.from_user.id))],
        [InlineKeyboardButton("اليسا 🔊", callback_data="elesa " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد سعيد 🔊", callback_data="mosaeed " + str(m.from_user.id))],
        [InlineKeyboardButton("اغاني شعبي 🔊", callback_data="sahby " + str(m.from_user.id))] +
        [InlineKeyboardButton("عمار حسني 🔊", callback_data="ammar " + str(m.from_user.id))],
        [InlineKeyboardButton("الجوكر 🔊", callback_data="joker " + str(m.from_user.id))] +
        [InlineKeyboardButton("حماقي 🔊", callback_data="hamaky " + str(m.from_user.id))],
        [InlineKeyboardButton("عمرو دياب 🔊", callback_data="dyab " + str(m.from_user.id))] +
        [InlineKeyboardButton("احمد كامل 🔊", callback_data="kamel " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
        [InlineKeyboardButton("السـورس 🤍", url=f"https://t.me/source_av")],
        
    ])
    await m.message.edit_text("↢ اهلا بك بقائمه الالفنانين اختر احدي المغنيين\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mhrgan (\\d+)$"))
async def mhrgan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مهرجانات 1 🔊", callback_data="mhrgan1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مهرجانات 2 🔊", callback_data="mhrgan2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مهرجانات 3 🔊", callback_data="mhrgan3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مهرجانات 4 🔊", callback_data="mhrgan4 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],
    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mhrgan1 (\\d+)$"))
async def mhrgan1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("ابوكي تاجر سلاح 🎧", callback_data="Xmhrg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عالم تعبانه 🎧", callback_data="Xmhrg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("عصام صاصا 😂 🎧", callback_data="Xmhrg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مابغيبش اونطه 🎧", callback_data="Xmhrg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("سلامات 🎧", callback_data="Xmhrg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوعي تصيع يا باي 🎧", callback_data="Xmhrg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("احنا محدش يقدرنا 🎧", callback_data="Xmhrg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("داهيه 🎧", callback_data="Xmhrg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("انتظرونا 🎧", callback_data="Xmhrg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خربانه انتي 🎧", callback_data="Xmhrg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضربه بضربه 🎧", callback_data="Xmhrg11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنتي قلبي 🎧", callback_data="Xmhrg12 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنت الجيران 🎧", callback_data="Xmhrg13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنتي اه بحبك 🎧", callback_data="Xmhrg14 " + str(m.from_user.id))],
        [InlineKeyboardButton("يابن امك 🎧", callback_data="Xmhrg15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كارثه 🎧", callback_data="Xmhrg16 " + str(m.from_user.id))],
        [InlineKeyboardButton("عود البطل 🎧", callback_data="Xmhrg17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رايحين نسهر 🎧", callback_data="Xmhrg18 " + str(m.from_user.id))],
        [InlineKeyboardButton("شوكلاته سايحه 🎧", callback_data="Xmhrg19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بونبوني ساقط 🎧", callback_data="Xmhrg20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة الهرجانات رقم 1\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mhrgan2 (\\d+)$"))
async def mhrgan2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("بنت البطل 🎧", callback_data="Xmhrg21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لعنه 🎧", callback_data="Xmhrg22 " + str(m.from_user.id))],
        [InlineKeyboardButton("تراك الاسد والرعاع 🎧", callback_data="Xmhrg23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("صاصا وسامر المدني 🎧", callback_data="Xmhrg24 " + str(m.from_user.id))],
        [InlineKeyboardButton("القاهره فوق 🎧", callback_data="Xmhrg25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ياطير 🎧", callback_data="Xmhrg26 " + str(m.from_user.id))],
        [InlineKeyboardButton("مولود كبير 🎧", callback_data="Xmhrg27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هلا والله 🎧", callback_data="Xmhrg28 " + str(m.from_user.id))],
        [InlineKeyboardButton("قلبي عايز صرمه 🎧", callback_data="Xmhrg29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كسر جمجمه 🎧", callback_data="Xmhrg30 " + str(m.from_user.id))],
        [InlineKeyboardButton("عملت سيرش ع الجدع 🎧", callback_data="Xmhrg31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حرمة 🎧", callback_data="Xmhrg32 " + str(m.from_user.id))],
        [InlineKeyboardButton("سور الجدعان 🎧", callback_data="Xmhrg33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اندال 🎧", callback_data="Xmhrg34 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحقودي 🎧", callback_data="Xmhrg35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("داين تدان 🎧", callback_data="Xmhrg36 " + str(m.from_user.id))],
        [InlineKeyboardButton("روح الحب 🎧", callback_data="Xmhrg37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مهموم 🎧", callback_data="Xmhrg38 " + str(m.from_user.id))],
        [InlineKeyboardButton("م عارف 😂 🎧", callback_data="Xmhrg39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اهلا صحابي الواطيين 🎧", callback_data="Xmhrg40 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة المهرجانات رقم 2\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mhrgan3 (\\d+)$"))
async def mhrgan3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("رضا البحراوي 2 🎧", callback_data="Xmhrg112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رضا البحراوي 1 🎧", callback_data="Xmhrg113 " + str(m.from_user.id))],
        [InlineKeyboardButton("كابتن كابتن 🎧", callback_data="Xmhrg114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مضروب بالكيف 🎧", callback_data="Xmhrg115 " + str(m.from_user.id))],
        [InlineKeyboardButton("اده اده اده 🎧", callback_data="Xmhrg116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("في الطفولة 🎧", callback_data="Xmhrg117 " + str(m.from_user.id))],
        [InlineKeyboardButton("البنات والسوشيال ميديا 🎧", callback_data="Xmhrg118 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يلا بينا نتجنن 🎧", callback_data="Xmhrg119 " + str(m.from_user.id))],
        [InlineKeyboardButton("صاحبي توب 🎧", callback_data="Xmhrg120 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ادلعي ياموزه 🎧", callback_data="Xmhrg121 " + str(m.from_user.id))],
        [InlineKeyboardButton("غصب عنك 🎧", callback_data="Xmhrg122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا بيكا الاوبهه 🎧", callback_data="Xmhrg123 " + str(m.from_user.id))],
        [InlineKeyboardButton("معاكي حياتي 🎧", callback_data="Xmhrg124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وقوف فالقلب 🎧", callback_data="Xmhrg125 " + str(m.from_user.id))],
        [InlineKeyboardButton("بعد الفقدان 🎧", callback_data="Xmhrg126 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة المهرجانات رقم 3\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mhrgan4 (\\d+)$"))
async def mhrgan4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("شلة مغروره 🎧", callback_data="Xmhrg127 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قلبي بيرضي 🎧", callback_data="Xmhrg128 " + str(m.from_user.id))],
        [InlineKeyboardButton("ولاد البلد 🎧", callback_data="Xmhrg129 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كينج اللعبه 🎧", callback_data="Xmhrg130 " + str(m.from_user.id))],
        [InlineKeyboardButton("كلبش 🎧", callback_data="Xmhrg131 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكتبا مليان 🎧", callback_data="Xmhrg132 " + str(m.from_user.id))],
        [InlineKeyboardButton("طيارات 🎧", callback_data="Xmhrg133 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مدينة المستقبل 🎧", callback_data="Xmhrg134 " + str(m.from_user.id))],
        [InlineKeyboardButton("صاحبي توب 🎧", callback_data="Xmhrg135 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العين بالعين 🎧", callback_data="Xmhrg136 " + str(m.from_user.id))],
        [InlineKeyboardButton("طب يلا 🎧", callback_data="Xmhrg137 " + str(m.from_user.id))] +
        [InlineKeyboardButton("توينز جاحد 🎧", callback_data="Xmhrg138 " + str(m.from_user.id))],
        [InlineKeyboardButton("ناس ملاعين 🎧", callback_data="Xmhrg139 " + str(m.from_user.id))] +
        [InlineKeyboardButton("استبينا 🎧", callback_data="Xmhrg140 " + str(m.from_user.id))],
        [InlineKeyboardButton("مفيش واحد سالك 🎧", callback_data="Xmhrg141 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة المهرجانات رقم 4\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmhrg1 (\\d+)$"))
async def Xmhrg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg2 (\\d+)$"))
async def Xmhrg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg3 (\\d+)$"))
async def Xmhrg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/215", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg4 (\\d+)$"))
async def Xmhrg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg5 (\\d+)$"))
async def Xmhrg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/217", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg6 (\\d+)$"))
async def Xmhrg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/218", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg7 (\\d+)$"))
async def Xmhrg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg8 (\\d+)$"))
async def Xmhrg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg9 (\\d+)$"))
async def Xmhrg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg10 (\\d+)$"))
async def Xmhrg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/222", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg11 (\\d+)$"))
async def Xmhrg11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg12 (\\d+)$"))
async def Xmhrg12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg13 (\\d+)$"))
async def Xmhrg13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/225", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg14 (\\d+)$"))
async def Xmhrg14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/226", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg15 (\\d+)$"))
async def Xmhrg15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/227", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg16 (\\d+)$"))
async def Xmhrg16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/228", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg17 (\\d+)$"))
async def Xmhrg17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/229", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg18 (\\d+)$"))
async def Xmhrg18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/230", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg19 (\\d+)$"))
async def Xmhrg19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/231", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg20 (\\d+)$"))
async def Xmhrg20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/232", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg21 (\\d+)$"))
async def Xmhrg21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/233", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg22 (\\d+)$"))
async def Xmhrg22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/234", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg23 (\\d+)$"))
async def Xmhrg23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/235", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg24 (\\d+)$"))
async def Xmhrg24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/236", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg25 (\\d+)$"))
async def Xmhrg25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/237", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg26 (\\d+)$"))
async def Xmhrg26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/238", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg27 (\\d+)$"))
async def Xmhrg27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/239", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg28 (\\d+)$"))
async def Xmhrg28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/240", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg29 (\\d+)$"))
async def Xmhrg29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/241", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg30 (\\d+)$"))
async def Xmhrg30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/242", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg31 (\\d+)$"))
async def Xmhrg31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/243", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg32 (\\d+)$"))
async def Xmhrg32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/244", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg33 (\\d+)$"))
async def Xmhrg33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/245", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg34 (\\d+)$"))
async def Xmhrg34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/246", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg35 (\\d+)$"))
async def Xmhrg35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/247", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg36 (\\d+)$"))
async def Xmhrg36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/248", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg37 (\\d+)$"))
async def Xmhrg37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/249", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg38 (\\d+)$"))
async def Xmhrg38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/250", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg39 (\\d+)$"))
async def Xmhrg39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/251", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg40 (\\d+)$"))
async def Xmhrg40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/252", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg112 (\\d+)$"))
async def Xmhrg112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/253", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg113 (\\d+)$"))
async def Xmhrg113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/254", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg114 (\\d+)$"))
async def Xmhrg114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/255", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg115 (\\d+)$"))
async def Xmhrg115(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/256", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg116 (\\d+)$"))
async def Xmhrg116(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/257", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg117 (\\d+)$"))
async def Xmhrg117(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/258", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg118 (\\d+)$"))
async def Xmhrg118(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/259", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg119 (\\d+)$"))
async def Xmhrg119(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/260", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg120 (\\d+)$"))
async def Xmhrg120(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/261", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg121 (\\d+)$"))
async def Xmhrg121(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/262", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg122 (\\d+)$"))
async def Xmhrg122(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/263", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg123 (\\d+)$"))
async def Xmhrg123(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/264", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg124 (\\d+)$"))
async def Xmhrg124(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/265", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg125 (\\d+)$"))
async def Xmhrg125(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/266", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg126 (\\d+)$"))
async def Xmhrg126(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/267", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg127 (\\d+)$"))
async def Xmhrg127(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/268", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg128 (\\d+)$"))
async def Xmhrg128(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/269", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg129 (\\d+)$"))
async def Xmhrg129(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/270", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg130 (\\d+)$"))
async def Xmhrg130(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/271", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg131 (\\d+)$"))
async def Xmhrg131(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/272", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg132 (\\d+)$"))
async def Xmhrg132(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/273", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg133 (\\d+)$"))
async def Xmhrg133(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/274", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg134 (\\d+)$"))
async def Xmhrg134(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/275", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg135 (\\d+)$"))
async def Xmhrg135(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/276", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg136 (\\d+)$"))
async def Xmhrg136(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/277", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg137 (\\d+)$"))
async def Xmhrg137(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/278", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg138 (\\d+)$"))
async def Xmhrg138(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/279", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg139 (\\d+)$"))
async def Xmhrg139(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/280", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg140 (\\d+)$"))
async def Xmhrg140(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/281", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmhrg141 (\\d+)$"))
async def Xmhrg141(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/282", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^adham (\\d+)$"))
async def adham(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حدا ما بينسي 🎧", callback_data="Xadh1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كيف بحبك هبك 🎧", callback_data="Xadh2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مشتاق 🎧", callback_data="Xadh3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حدك الكون 🎧", callback_data="Xadh4 " + str(m.from_user.id))],
        [InlineKeyboardButton("بتعرف شعوري 🎧", callback_data="Xadh5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النهايه السعيده 🎧", callback_data="Xadh6 " + str(m.from_user.id))],
        [InlineKeyboardButton("نسخه منك 🎧", callback_data="Xadh7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هو الحب 🎧", callback_data="Xadh8 " + str(m.from_user.id))],
        [InlineKeyboardButton("ودعني 🎧", callback_data="Xadh9 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني ادهم نابلسي", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xadh1 (\\d+)$"))
async def Xadh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/302", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh2 (\\d+)$"))
async def Xadh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/303", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh3 (\\d+)$"))
async def Xadh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/304", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh4 (\\d+)$"))
async def Xadh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/305", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh5 (\\d+)$"))
async def Xadh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/306", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh6 (\\d+)$"))
async def Xadh6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/307", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh7 (\\d+)$"))
async def Xadh7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/308", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh8 (\\d+)$"))
async def Xadh8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/309", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xadh9 (\\d+)$"))
async def Xadh9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/310", reply_to_message_id=mid)


######################################################################
######################################################################

@app.on_callback_query(filters.regex("^agnaby (\\d+)$"))
async def agnaby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙹𝚄𝚂𝚃𝙸𝙽𝙴 𝙱𝙸𝙱𝙴𝚁 🔊", callback_data="agn1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙼𝙰𝚁𝙾𝙾𝙽 🔊", callback_data="agn2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝙸𝙰 🔊", callback_data="agn3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙴𝙳 𝚂𝙷𝙴𝙴𝚁𝙰𝙽 🔊", callback_data="agn4 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙿𝙾𝚂𝚃 𝙼𝙰𝙻𝙾𝙽𝙴 🔊", callback_data="agn5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚃𝙰𝚈𝙻𝙾𝚁 𝚂𝚆𝙸𝙵𝚃 🔊", callback_data="agn6 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚃𝙷𝙴 𝙲𝙷𝙰𝙸𝙽𝚂𝙼𝙾𝙺𝙴𝚁𝚂 🔊", callback_data="agn7 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙱𝙸𝙻𝙻𝙸𝙴 𝙴𝙸𝙻𝙸𝚂𝙷 🔊", callback_data="agn8 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙴𝙸𝙼𝙰𝙶𝙸𝙽𝙴 𝙳𝚁𝙰𝙶𝙾𝙽 🔊", callback_data="agn9 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙲𝙷𝙰𝚁𝙻𝙸𝙴 𝙿𝚄𝚃𝙷 🔊", callback_data="agn10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙷𝙰𝙻𝚂𝙴𝚈 🔊", callback_data="agn11 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙱𝙴𝙱𝙴 𝚁𝙴𝚇𝙷𝙰 🔊", callback_data="agn12 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Mix 🔊", callback_data="mix " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه الاغاني الاجنبي اختر احدي المغنيين\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn1 (\\d+)$"))
async def agn1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙻𝙾𝙽𝙴𝙻𝚈 🎧", callback_data="Xagn144 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙷𝙾𝙻𝚈 🎧", callback_data="Xagn145 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙿𝙾𝙿 𝚂𝚃𝙰𝚁 🎧", callback_data="Xagn146 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙻𝙾𝚅𝙴 𝚈𝙾𝚄𝚁 𝚂𝙴𝙻𝙵 🎧", callback_data="Xagn147 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚆𝙷𝙰𝚃 𝙳𝙾 𝚈𝙾𝚄 🎧", callback_data="Xagn148 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙵𝙾𝚁 𝙴𝚅𝙴𝚁 🎧", callback_data="Xagn149 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚈𝚄𝙼𝙼𝚈 🎧", callback_data="Xagn150 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙸𝙽𝚃𝙴𝙽𝚃𝙸𝙾𝙽𝚂 🎧", callback_data="Xagn151 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝙾𝚁𝚁𝚈 🎧", callback_data="Xagn152 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙲𝙾𝙻𝙳 𝚆𝙰𝚃𝙴𝚁 🎧", callback_data="Xagn153 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙲𝙾𝙼𝙿𝙰𝙽𝚈 🎧", callback_data="Xagn154 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙹𝚄𝚂𝚃𝙸𝙽𝙴 𝙱𝙸𝙱𝙴𝚁\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn2 (\\d+)$"))
async def agn2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙼𝙴𝙼𝙾𝚁𝙸𝙴𝚂 🎧", callback_data="Xagn161 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙼𝙰𝙿𝚂 🎧", callback_data="Xagn162 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙶𝙸𝚁𝙻𝚂 𝙻𝙸𝙺𝙴 𝚈𝙾𝚄 🎧", callback_data="Xagn163 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚂𝚄𝙶𝙰𝚁 🎧", callback_data="Xagn164 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙿𝙰𝚈𝙿𝙷𝙾𝙽𝙴 🎧", callback_data="Xagn165 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙼𝙰𝚁𝙾𝙾𝙽\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn3 (\\d+)$"))
async def agn3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙲𝙷𝙰𝙽𝙳𝙴𝙻𝙸𝙴𝚁 🎧", callback_data="Xagn167 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚃𝙷𝙴 𝙶𝚁𝙴𝙰𝚃𝙴𝚂𝚃 🎧", callback_data="Xagn168 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚄𝙽𝚂𝚃𝙾𝙿𝙿𝙰𝙱𝙻𝙴 🎧", callback_data="Xagn169 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙲𝙷𝙴𝙰𝙿 𝚃𝙷𝚁𝙸𝙻𝙻𝚂  🎧", callback_data="Xagn170 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙸𝙼 𝚂𝚃𝙸𝙻𝙻 𝙷𝙴𝚁𝙴🎧", callback_data="Xagn171 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝚂𝙸𝙰 \n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn4 (\\d+)$"))
async def agn4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙿𝙴𝚁𝙵𝙴𝙲𝚃 🎧", callback_data="Xagn173 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚂𝙷𝙰𝙿𝙴 𝙾𝙵 𝚈𝙾𝚄 🎧", callback_data="Xagn174 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚃𝙷𝙸𝙽𝙺𝙸𝙽𝙶 𝙾𝚄𝚃 𝙻𝙾𝚄𝙳 🎧", callback_data="Xagn175 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙿𝙷𝙾𝚃𝙾𝙶𝚁𝙰𝙿𝙷 🎧", callback_data="Xagn176 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙳𝙸𝚅𝙴 🎧", callback_data="Xagn177 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙶𝙰𝙻𝚆𝙰𝚈 𝙶𝙸𝚁𝙻 🎧", callback_data="Xagn178 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙸 𝙳𝙾𝙽𝚃 𝙲𝙰𝚁𝙴 🎧", callback_data="Xagn179 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙴𝙳 𝚂𝙷𝙴𝙴𝚁𝙰𝙽\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn5 (\\d+)$"))
async def agn5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙲𝙸𝚁𝙲𝙻𝙴𝚂 🎧", callback_data="Xagn181 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚁𝙾𝙲𝙺𝚂𝚃𝙰𝚁 🎧", callback_data="Xagn182 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙶𝙾𝙾𝙳𝙱𝚈𝙴𝚂 🎧", callback_data="Xagn183 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🎧", callback_data="Xagn184 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝚄𝙽 𝙵𝙻𝙾𝚆𝙴𝚁 🎧", callback_data="Xagn185 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚆𝙾𝚆 🎧", callback_data="Xagn186 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙿𝙾𝚂𝚃 𝙼𝙰𝙻𝙾𝙽�\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn6 (\\d+)$"))
async def agn6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙱𝙻𝙰𝙲𝙺 𝚂𝙿𝙰𝙲𝙴  🎧", callback_data="Xagn188 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙲𝙰𝚁𝙳𝙸𝙶𝙰𝙽 🎧", callback_data="Xagn189 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙳𝙴𝙻𝙸𝙲𝙰𝚃𝙴 🎧", callback_data="Xagn190 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙻𝙾𝙾𝙺 𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝙼𝙰𝙳𝙴 𝙼𝙴 𝙳𝙾 🎧", callback_data="Xagn191 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙴𝚇𝙸𝙻𝙴 🎧", callback_data="Xagn192 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚈𝙾𝚄 𝙱𝙴𝙻𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝙼𝙴 🎧", callback_data="Xagn193 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝚃𝙰𝚈𝙻𝙾𝚁 𝚂𝚆𝙸𝙵𝚃\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn7 (\\d+)$"))
async def agn7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴𝚁 🎧", callback_data="Xagn195 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙳𝙾𝙽𝚃 𝙻𝙴𝚃 𝙼𝙴 𝙳𝙾𝚆𝙽 🎧", callback_data="Xagn196 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝙸𝙲𝙺 𝙱𝙾𝚈 🎧", callback_data="Xagn197 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝙹𝚄𝚂𝚃 𝙻𝙸𝙺𝙴 🎧", callback_data="Xagn198 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙸𝙻𝙻𝙴𝙽𝙸𝚄𝙼 🎧", callback_data="Xagn199 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙷𝙾𝙿𝙴 🎧", callback_data="Xagn200 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝚃𝙷𝙴 𝙲𝙷𝙰𝙸𝙽𝚂𝙼𝙾𝙺𝙴𝚁𝚂\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn8 (\\d+)$"))
async def agn8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙻𝙾𝚅𝙴𝙻𝚈 🎧", callback_data="Xagn202 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚆𝙷𝙴𝙽 𝚃𝙷𝙴 𝙿𝙰𝚁𝚃𝚈 𝙾𝚅𝙴𝚁 🎧", callback_data="Xagn203 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙱𝙴𝙻𝙻𝚈𝙰𝙲𝙷𝙴 🎧", callback_data="Xagn204 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙱𝚄𝚁𝚈 𝙰 𝙵𝚁𝙸𝙴𝙽𝙳 🎧", callback_data="Xagn205 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙰𝙻𝙻 𝚃𝙷𝙴 𝙶𝙾𝙾𝙳 𝙶𝙸𝚁𝙻𝚂 𝙶𝙾 𝚃𝙾 𝙷𝙴𝙻𝙻  🎧", callback_data="Xagn206 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙱𝙰𝙳 𝙶𝚄𝚈  🎧", callback_data="Xagn207 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙱𝙸𝙻𝙻𝙸𝙴 𝙴𝙸𝙻𝙸𝚂𝙷\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn9 (\\d+)$"))
async def agn9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙱𝙴𝙻𝙸𝙴𝚅𝙴𝚁 🎧", callback_data="Xagn209 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙽𝙰𝚃𝚄𝚁𝙰𝙻 🎧", callback_data="Xagn210 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚃𝙷𝚄𝙽𝙳𝙴𝚁 🎧", callback_data="Xagn211 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚁𝙰𝙳𝙸𝙾𝙰𝙲𝚃𝙸𝚅𝙴 🎧", callback_data="Xagn212 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙻𝙸𝙰𝚁 🎧", callback_data="Xagn213 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚆𝙷𝙰𝚃𝙴𝚅𝙴𝚁 𝙸𝚃 𝚃𝙰𝙺𝙴𝚂 🎧", callback_data="Xagn214 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙴𝙸𝙼𝙰𝙶𝙸𝙽𝙴 𝙳𝚁𝙰𝙶𝙾𝙽\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn10 (\\d+)$"))
async def agn10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙰𝚃𝚃𝙴𝙽𝚃𝙸𝙾𝙽 🎧", callback_data="Xagn216 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙷𝙾𝚆 𝙻𝙾𝙽𝙶 🎧", callback_data="Xagn217 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚆𝙴 𝙳𝙾𝙽𝚃 𝚃𝙰𝙻𝙺 𝙰𝙽𝚈𝙼𝙾𝚁𝙴 🎧", callback_data="Xagn218 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙳𝙰𝙽𝙶𝙴𝚁𝙾𝚄𝚂𝙻𝚈 🎧", callback_data="Xagn219 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙾𝙽𝙴 𝙲𝙰𝙻𝙻 𝙰𝚆𝙰𝚈 🎧", callback_data="Xagn220 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚂𝙴𝙴 𝚈𝙾𝚄 𝙰𝙶𝙸𝙽𝙴 🎧", callback_data="Xagn221 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙲𝙷??𝚁𝙻𝙸𝙴 𝙿𝚄𝚃𝙷\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn11 (\\d+)$"))
async def agn11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙱𝙰𝙳 𝙰𝚃 𝙻𝙾𝚅𝙴 🎧", callback_data="Xagn223 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙼𝙴 🎧", callback_data="Xagn224 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙱𝙴 𝙺𝙸𝙽𝙳 🎧", callback_data="Xagn225 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝚂𝙾𝚁𝚁𝚈 🎧", callback_data="Xagn226 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙶𝚁𝙰𝚅𝙴𝚈𝙰𝚁𝙳 🎧", callback_data="Xagn227 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙷𝙸𝙼 𝙰𝙽𝙳 𝙸 🎧", callback_data="Xagn228 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙷𝙰𝙻𝚂𝙴𝚈\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^agn12 (\\d+)$"))
async def agn12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("𝙸 𝙶𝙾𝚃 𝚈𝙾𝚄 🎧", callback_data="Xagn230 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙸𝙼 𝙰 𝙼𝙴𝚂𝚂 🎧", callback_data="Xagn231 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝚂𝙰𝚈 𝙼𝚈 𝙽𝙰𝙼𝙴 🎧", callback_data="Xagn232 " + str(m.from_user.id))] +
        [InlineKeyboardButton("𝙼𝙴𝙰𝙽𝚃 𝚃𝙾 𝙱𝙴 🎧", callback_data="Xagn233 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙸𝙽 𝙽𝙰𝙼𝙴 𝙾𝙵 𝙻𝙾𝚅𝙴 🎧", callback_data="Xagn234 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝙷𝙰𝚁𝙳𝙴𝚁 🎧", callback_data="Xagn235 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])

    await m.message.edit_text("↢ اهلا بك بقائمه اغاني 𝙱𝙴𝙱𝙴 𝚁𝙴𝚇𝙷𝙰\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mix (\\d+)$"))
async def mix(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("Lambada 🎧", callback_data="Xagn1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Boombastic 🎧", callback_data="Xagn2 " + str(m.from_user.id))],
        [InlineKeyboardButton("Despasito 🎧", callback_data="Xagn3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Bum bum 🎧", callback_data="Xagn4 " + str(m.from_user.id))],
        [InlineKeyboardButton("Let it go 🎧", callback_data="Xagn5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Yesterday 🎧", callback_data="Xagn6 " + str(m.from_user.id))],
        [InlineKeyboardButton("He comes the sun 🎧", callback_data="Xagn7 " + str(m.from_user.id))],
        [InlineKeyboardButton("Venom 🎧", callback_data="Xagn8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Rab god 🎧", callback_data="Xagn9 " + str(m.from_user.id))],
        [InlineKeyboardButton("A whole new world 🎧", callback_data="Xagn10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Its you 🎧", callback_data="Xagn11 " + str(m.from_user.id))],
        [InlineKeyboardButton("Drunk 🎧", callback_data="Xagn12 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Moonlight 🎧", callback_data="Xagn13 " + str(m.from_user.id))],
        [InlineKeyboardButton("Get you the moon 🎧", callback_data="Xagn14 " + str(m.from_user.id))],
        [InlineKeyboardButton("Can we kiss forever 🎧", callback_data="Xagn15 " + str(m.from_user.id))],
        [InlineKeyboardButton("Wake up in the sky 🎧", callback_data="Xagn16 " + str(m.from_user.id))],
        [InlineKeyboardButton("Just the way you are 🎧", callback_data="Xagn17 " + str(m.from_user.id))],
        [InlineKeyboardButton("Dark side 🎧", callback_data="Xagn18 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Still cold 🎧", callback_data="Xagn19 " + str(m.from_user.id))],
        [InlineKeyboardButton("What if i told you that i love you 🎧", callback_data="Xagn20 " + str(m.from_user.id))],
        [InlineKeyboardButton("Your not alone 🎧", callback_data="Xagn21 " + str(m.from_user.id))],
        [InlineKeyboardButton("Cant lie 🎧", callback_data="Xagn22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("Lie to me 🎧", callback_data="Xagn23 " + str(m.from_user.id))],
        [InlineKeyboardButton("River 🎧", callback_data="Xagn24 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="agnaby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ Select What you want from the Song", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^xagn1 (\\d+)$"))
async def xagn1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/177", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn2 (\\d+)$"))
async def xagn2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/178", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn3 (\\d+)$"))
async def xagn3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/179", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn4 (\\d+)$"))
async def xagn4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/180", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn5 (\\d+)$"))
async def xagn5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/181", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn6 (\\d+)$"))
async def xagn6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/182", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn7 (\\d+)$"))
async def xagn7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/183", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn8 (\\d+)$"))
async def xagn8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/184", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn9 (\\d+)$"))
async def xagn9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/185", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn10 (\\d+)$"))
async def xagn10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/186", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn11 (\\d+)$"))
async def xagn11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn12 (\\d+)$"))
async def xagn12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn13 (\\d+)$"))
async def xagn13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn14 (\\d+)$"))
async def xagn14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn15 (\\d+)$"))
async def xagn15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/215", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn16 (\\d+)$"))
async def xagn16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn17 (\\d+)$"))
async def xagn17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/217", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn18 (\\d+)$"))
async def xagn18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/218", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn19 (\\d+)$"))
async def xagn19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn20 (\\d+)$"))
async def xagn20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn21 (\\d+)$"))
async def xagn21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn22 (\\d+)$"))
async def xagn22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/222", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn23 (\\d+)$"))
async def xagn23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^xagn24 (\\d+)$"))
async def xagn24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U_VBU/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn144 (\\d+)$"))
async def Xagn144(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/144", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn145 (\\d+)$"))
async def Xagn145(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/145", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn161 (\\d+)$"))
async def Xagn161(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/161", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn162 (\\d+)$"))
async def Xagn162(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/162", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn163 (\\d+)$"))
async def Xagn163(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/163", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn164 (\\d+)$"))
async def Xagn164(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/164", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn165 (\\d+)$"))
async def Xagn165(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/165", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn167 (\\d+)$"))
async def Xagn167(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/167", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn168 (\\d+)$"))
async def Xagn168(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/168", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn169 (\\d+)$"))
async def Xagn169(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/169", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn170 (\\d+)$"))
async def Xagn170(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/170", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn171 (\\d+)$"))
async def Xagn171(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/171", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn173 (\\d+)$"))
async def Xagn173(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/173", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn174 (\\d+)$"))
async def Xagn174(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/174", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn175 (\\d+)$"))
async def Xagn175(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/175", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn176 (\\d+)$"))
async def Xagn176(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/176", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn177 (\\d+)$"))
async def Xagn177(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/177", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn178 (\\d+)$"))
async def Xagn178(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/178", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn179 (\\d+)$"))
async def Xagn179(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/179", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn181 (\\d+)$"))
async def Xagn181(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/181", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn182 (\\d+)$"))
async def Xagn182(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/182", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn183 (\\d+)$"))
async def Xagn183(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/183", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn184 (\\d+)$"))
async def Xagn184(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/184", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn185 (\\d+)$"))
async def Xagn185(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/185", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn186 (\\d+)$"))
async def Xagn186(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/186", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn188 (\\d+)$"))
async def Xagn188(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/188", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn189 (\\d+)$"))
async def Xagn189(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/189", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn190 (\\d+)$"))
async def Xagn190(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/190", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn191 (\\d+)$"))
async def Xagn191(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/191", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn192 (\\d+)$"))
async def Xagn192(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/192", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn193 (\\d+)$"))
async def Xagn193(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/193", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn195 (\\d+)$"))
async def Xagn195(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/195", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn196 (\\d+)$"))
async def Xagn196(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/196", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn197 (\\d+)$"))
async def Xagn197(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/197", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn198 (\\d+)$"))
async def Xagn198(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/198", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn199 (\\d+)$"))
async def Xagn199(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/199", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn200 (\\d+)$"))
async def Xagn200(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/200", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn202 (\\d+)$"))
async def Xagn202(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/202", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn203 (\\d+)$"))
async def Xagn203(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/203", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn204 (\\d+)$"))
async def Xagn204(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/204", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn205 (\\d+)$"))
async def Xagn205(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn206 (\\d+)$"))
async def Xagn206(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/206", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn207 (\\d+)$"))
async def Xagn207(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/207", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn209 (\\d+)$"))
async def Xagn209(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/209", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn210 (\\d+)$"))
async def Xagn210(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/210", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn211 (\\d+)$"))
async def Xagn211(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn212 (\\d+)$"))
async def Xagn212(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn213 (\\d+)$"))
async def Xagn213(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn214 (\\d+)$"))
async def Xagn214(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn216 (\\d+)$"))
async def Xagn216(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn217 (\\d+)$"))
async def Xagn217(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/217", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn218 (\\d+)$"))
async def Xagn218(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/218", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn219 (\\d+)$"))
async def Xagn219(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn220 (\\d+)$"))
async def Xagn220(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn221 (\\d+)$"))
async def Xagn221(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn223 (\\d+)$"))
async def Xagn223(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn224 (\\d+)$"))
async def Xagn224(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn225 (\\d+)$"))
async def Xagn225(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/225", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn226 (\\d+)$"))
async def Xagn226(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/226", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn227 (\\d+)$"))
async def Xagn227(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/227", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn228 (\\d+)$"))
async def Xagn228(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/228", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn230 (\\d+)$"))
async def Xagn230(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/230", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn231 (\\d+)$"))
async def Xagn231(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/231", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn232 (\\d+)$"))
async def Xagn232(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/232", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn233 (\\d+)$"))
async def Xagn233(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/233", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn234 (\\d+)$"))
async def Xagn234(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/234", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xagn235 (\\d+)$"))
async def Xagn235(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("httpsVBMUSIC1VBMUSIC1/235", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^ammar (\\d+)$"))
async def ammar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("بتيجي في بالي 🎧", callback_data="Xamm1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طيب 🎧", callback_data="Xamm2 " + str(m.from_user.id))],
        [InlineKeyboardButton("برشامه منوم 🎧", callback_data="Xamm3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بساط 🎧", callback_data="Xamm4 " + str(m.from_user.id))],
        [InlineKeyboardButton("طفره 🎧", callback_data="Xamm5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ترام 🎧", callback_data="Xamm6 " + str(m.from_user.id))],
        [InlineKeyboardButton("هلوسه 🎧", callback_data="Xamm7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مسوخ 🎧", callback_data="Xamm8 " + str(m.from_user.id))],
        [InlineKeyboardButton("بلاش تغني 🎧", callback_data="Xamm9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اخر عازف ع الارض 🎧", callback_data="Xamm10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حدود 🎧", callback_data="Xamm11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("غامق 🎧", callback_data="Xamm12 " + str(m.from_user.id))],
        [InlineKeyboardButton("فاترينا 🎧", callback_data="Xamm13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جهنم 🎧", callback_data="Xamm14 " + str(m.from_user.id))],
        [InlineKeyboardButton("فستان 🎧", callback_data="Xamm15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ضي العين 🎧", callback_data="Xamm16 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا ليل اندهلي 🎧", callback_data="Xamm17 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني عمار حسني", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xamm1 (\\d+)$"))
async def Xamm1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/331", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm2 (\\d+)$"))
async def Xamm2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/332", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm3 (\\d+)$"))
async def Xamm3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/333", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm4 (\\d+)$"))
async def Xamm4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/334", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm5 (\\d+)$"))
async def Xamm5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/335", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm6 (\\d+)$"))
async def Xamm6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/336", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm7 (\\d+)$"))
async def Xamm7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/337", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm8 (\\d+)$"))
async def Xamm8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/338", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm9 (\\d+)$"))
async def Xamm9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/339", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm10 (\\d+)$"))
async def Xamm10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/340", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm11 (\\d+)$"))
async def Xamm11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/341", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm12 (\\d+)$"))
async def Xamm12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/342", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm13 (\\d+)$"))
async def Xamm13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/343", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm14 (\\d+)$"))
async def Xamm14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/344", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm15 (\\d+)$"))
async def Xamm15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/345", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm16 (\\d+)$"))
async def Xamm16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/346", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xamm17 (\\d+)$"))
async def Xamm17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/347", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^asala (\\d+)$"))
async def asala(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("60 دقيقه 🎧", callback_data="Xasa1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خانات الذكريات 🎧", callback_data="Xasa2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياعالم 🎧", callback_data="Xasa3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هو حبيبي 🎧", callback_data="Xasa4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قد الحروف 🎧", callback_data="Xasa5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اسفه 🎧", callback_data="Xasa6 " + str(m.from_user.id))],
        [InlineKeyboardButton("اكتر 🎧", callback_data="Xasa7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جابو سيرتو 🎧", callback_data="Xasa8 " + str(m.from_user.id))],
        [InlineKeyboardButton("روحي وخداني 🎧", callback_data="Xasa9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سؤال بسيط 🎧", callback_data="Xasa10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني اصاله 🔊\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xasa1 (\\d+)$"))
async def Xasa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/322", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa2 (\\d+)$"))
async def Xasa2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/321", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa3 (\\d+)$"))
async def Xasa3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/324", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa4 (\\d+)$"))
async def Xasa4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/323", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa5 (\\d+)$"))
async def Xasa5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/326", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa6 (\\d+)$"))
async def Xasa6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/325", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa7 (\\d+)$"))
async def Xasa7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/328", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa8 (\\d+)$"))
async def Xasa8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/327", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa9 (\\d+)$"))
async def Xasa9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/330", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xasa10 (\\d+)$"))
async def Xasa10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/329", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^bablo (\\d+)$"))
async def bablo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الجميزه 🎧", callback_data="Xbab1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فري 🎧", callback_data="Xbab2 " + str(m.from_user.id))],
        [InlineKeyboardButton("سندباد 🎧", callback_data="Xbab3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ابو مكة 🎧", callback_data="Xbab4 " + str(m.from_user.id))],
        [InlineKeyboardButton("افتر بارتي 🎧", callback_data="Xbab5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سكانيا 🎧", callback_data="Xbab6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ديناميت 🎧", callback_data="Xbab7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فولكلور 🎧", callback_data="Xbab8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني بابلو\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xbab1 (\\d+)$"))
async def Xbab1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/348", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab2 (\\d+)$"))
async def Xbab2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/349", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab3 (\\d+)$"))
async def Xbab3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/350", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab4 (\\d+)$"))
async def Xbab4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/351", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab5 (\\d+)$"))
async def Xbab5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/352", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab6 (\\d+)$"))
async def Xbab6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/353", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab7 (\\d+)$"))
async def Xbab7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/354", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xbab8 (\\d+)$"))
async def Xbab8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/h_o_sam/355", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^dyab (\\d+)$"))
async def dyab(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("قدام مرايتها 🎧", callback_data="Xdya1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يابلدرنا ياحلوه 🎧", callback_data="Xdya2 " + str(m.from_user.id))],
        [InlineKeyboardButton("تملي معاك 🎧", callback_data="Xdya3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يااجمل عيون 🎧", callback_data="Xdya4 " + str(m.from_user.id))],
        [InlineKeyboardButton("وماله 🎧", callback_data="Xdya5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هيعيش يفتكرني 🎧", callback_data="Xdya6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ده لو اتساب 🎧", callback_data="Xdya7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اول يوم في البعد 🎧", callback_data="Xdya8 " + str(m.from_user.id))],
        [InlineKeyboardButton("معاك قلبي 🎧", callback_data="Xdya9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وهي عامله ايه 🎧", callback_data="Xdya10 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكانك يف قلبي 🎧", callback_data="Xdya11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي مانتي 🎧", callback_data="Xdya12 " + str(m.from_user.id))],
        [InlineKeyboardButton("عم الطيب 🎧", callback_data="Xdya13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سهران 🎧", callback_data="Xdya14 " + str(m.from_user.id))],
        [InlineKeyboardButton("حلوة البدايات 🎧", callback_data="Xdya15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بالضحكه دي 🎧", callback_data="Xdya16 " + str(m.from_user.id))],
        [InlineKeyboardButton("جامده بس 🎧", callback_data="Xdya17 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdya1 (\\d+)$"))
async def Xdya1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/160", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya2 (\\d+)$"))
async def Xdya2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/161", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya3 (\\d+)$"))
async def Xdya3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/162", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya4 (\\d+)$"))
async def Xdya4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/163", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya5 (\\d+)$"))
async def Xdya5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/164", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya6 (\\d+)$"))
async def Xdya6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/165", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya7 (\\d+)$"))
async def Xdya7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/166", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya8 (\\d+)$"))
async def Xdya8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/167", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya9 (\\d+)$"))
async def Xdya9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/168", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya10 (\\d+)$"))
async def Xdya10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/169", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya11 (\\d+)$"))
async def Xdya11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/170", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya12 (\\d+)$"))
async def Xdya12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/171", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya13 (\\d+)$"))
async def Xdya13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/172", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya14 (\\d+)$"))
async def Xdya14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/173", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya15 (\\d+)$"))
async def Xdya15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/174", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya16 (\\d+)$"))
async def Xdya16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/175", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xdya17 (\\d+)$"))
async def Xdya17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/176", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^elesa (\\d+)$"))
async def elesa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("يا مرايتي ??", callback_data="Xeles1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("افتكرت 🎧", callback_data="Xeles2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكتوبه ليك 🎧", callback_data="Xeles3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاله حب 🎧", callback_data="Xeles4 " + str(m.from_user.id))],
        [InlineKeyboardButton("تعبت منك 🎧", callback_data="Xeles5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وانت قصادي 🎧", callback_data="Xeles6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مباحه ليك 🎧", callback_data="Xeles7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("في عيونك 🎧", callback_data="Xeles8 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا شبه نسيتك 🎧", callback_data="Xeles9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنحب الحياه 🎧", callback_data="Xeles10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حبه اهتمام 🎧", callback_data="Xeles11 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني اليسا\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xeles1 (\\d+)$"))
async def Xeles1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/118", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles2 (\\d+)$"))
async def Xeles2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/119", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles3 (\\d+)$"))
async def Xeles3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/120", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles4 (\\d+)$"))
async def Xeles4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles5 (\\d+)$"))
async def Xeles5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles6 (\\d+)$"))
async def Xeles6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles7 (\\d+)$"))
async def Xeles7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles8 (\\d+)$"))
async def Xeles8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles9 (\\d+)$"))
async def Xeles9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles10 (\\d+)$"))
async def Xeles10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/127", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xeles11 (\\d+)$"))
async def Xeles11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/128", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^hamaky (\\d+)$"))
async def hamaky(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هو ده حبيبي 🎧", callback_data="Xham1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قدام الناس 🎧", callback_data="Xham2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياستار 🎧", callback_data="Xham3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("راسمك في خيالي 🎧", callback_data="Xham4 " + str(m.from_user.id))],
        [InlineKeyboardButton("احلي حاجه فيكي 🎧", callback_data="Xham5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مابلاش 🎧", callback_data="Xham6 " + str(m.from_user.id))],
        [InlineKeyboardButton("م البدايه 🎧", callback_data="Xham7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليله باظت 🎧", callback_data="Xham8 " + str(m.from_user.id))],
        [InlineKeyboardButton("واحده واحده 🎧", callback_data="Xham9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("واعمل ايه 🎧", callback_data="Xham10 " + str(m.from_user.id))],
        [InlineKeyboardButton("من قلبي بغني 🎧", callback_data="Xham11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاجه مستخبيه 🎧", callback_data="Xham12 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني حماقي\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xham1 (\\d+)$"))
async def Xham1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/88", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham2 (\\d+)$"))
async def Xham2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/89", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham3 (\\d+)$"))
async def Xham3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/90", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham4 (\\d+)$"))
async def Xham4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/91", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham5 (\\d+)$"))
async def Xham5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/92", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham6 (\\d+)$"))
async def Xham6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/93", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham7 (\\d+)$"))
async def Xham7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/94", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham8 (\\d+)$"))
async def Xham8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/95", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham9 (\\d+)$"))
async def Xham9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/96", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham10 (\\d+)$"))
async def Xham10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/97", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham11 (\\d+)$"))
async def Xham11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/98", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xham12 (\\d+)$"))
async def Xham12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/99", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^helal (\\d+)$"))
async def helal(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("وبحس معاك 🎧", callback_data="Xhela1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اشرب شاي 🎧", callback_data="Xhela2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ليه اختارنا البعد 🎧", callback_data="Xhela3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دايما دموع 🎧", callback_data="Xhela4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ساعات 🎧", callback_data="Xhela5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محدش بينفع حد 🎧", callback_data="Xhela6 " + str(m.from_user.id))],
        [InlineKeyboardButton("متغيره 🎧", callback_data="Xhela7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وجمالها 🎧", callback_data="Xhela8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني حماده هلال", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xhela1 (\\d+)$"))
async def Xhela1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/34", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela2 (\\d+)$"))
async def Xhela2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/35", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela3 (\\d+)$"))
async def Xhela3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/36", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela4 (\\d+)$"))
async def Xhela4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/37", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela5 (\\d+)$"))
async def Xhela5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/38", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela6 (\\d+)$"))
async def Xhela6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/39", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela7 (\\d+)$"))
async def Xhela7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/40", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xhela8 (\\d+)$"))
async def Xhela18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/41", reply_to_message_id=mid)


#######################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^joker (\\d+)$"))
async def joker(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الكبت 🎧", callback_data="Xjok1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقع 🎧", callback_data="Xjok2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مناسك الالم 🎧", callback_data="Xjok3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فرصه تانيه 🎧", callback_data="Xjok4 " + str(m.from_user.id))],
        [InlineKeyboardButton("تسعيناتي 🎧", callback_data="Xjok5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قادرين 🎧", callback_data="Xjok6 " + str(m.from_user.id))],
        [InlineKeyboardButton("العقد 🎧", callback_data="Xjok7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الوصايا 🎧", callback_data="Xjok8 " + str(m.from_user.id))],
        [InlineKeyboardButton("دنيا 🎧", callback_data="Xjok9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حلم كبير 🎧", callback_data="Xjok10 " + str(m.from_user.id))],
        [InlineKeyboardButton("سكان الليل 🎧", callback_data="Xjok11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بعد النسيان 🎧", callback_data="Xjok12 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني الجوكر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xjok1 (\\d+)$"))
async def Xjok1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok2 (\\d+)$"))
async def Xjok2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/148", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok3 (\\d+)$"))
async def Xjok3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/149", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok4 (\\d+)$"))
async def Xjok4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/150", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok5 (\\d+)$"))
async def Xjok5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/151", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok6 (\\d+)$"))
async def Xjok6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/152", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok7 (\\d+)$"))
async def Xjok7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/153", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok8 (\\d+)$"))
async def Xjok8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok9 (\\d+)$"))
async def Xjok9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/155", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok10 (\\d+)$"))
async def Xjok10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/156", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok11 (\\d+)$"))
async def Xjok11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/157", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xjok12 (\\d+)$"))
async def Xjok12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/158", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^kamel (\\d+)$"))
async def kamel(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("انا مستنيك 🎧", callback_data="Xkam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تايجر خارج عن السيطره 🎧", callback_data="Xkam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("جاوبنا يا ليل 🎧", callback_data="Xkam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي نور 🎧", callback_data="Xkam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قصاد بابك 🎧", callback_data="Xkam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قولي غاب 🎧", callback_data="Xkam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("كان في طفل 🎧", callback_data="Xkam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كانسر 🎧", callback_data="Xkam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("مبقتش اخاف 🎧", callback_data="Xkam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("متزعليش 🎧", callback_data="Xkam10 " + str(m.from_user.id))],
        [InlineKeyboardButton("ولا بننسي 🎧", callback_data="Xkam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مش شرط 🎧", callback_data="Xkam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا ليل 🎧", callback_data="Xkam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تتجوزيني 🎧", callback_data="Xkam14 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني احمد كامل\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xkam1 (\\d+)$"))
async def Xkam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/101", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam2 (\\d+)$"))
async def Xkam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/102", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam3 (\\d+)$"))
async def Xkam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/103", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam4 (\\d+)$"))
async def Xkam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/104", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam5 (\\d+)$"))
async def Xkam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/105", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam6 (\\d+)$"))
async def Xkam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/106", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam7 (\\d+)$"))
async def Xkam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/107", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam8 (\\d+)$"))
async def Xkam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/108", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam9 (\\d+)$"))
async def Xkam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/109", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam10 (\\d+)$"))
async def Xkam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/110", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam11 (\\d+)$"))
async def Xkam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/111", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam12 (\\d+)$"))
async def Xkam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/112", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam13 (\\d+)$"))
async def Xkam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/113", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xkam14 (\\d+)$"))
async def Xkam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/114", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^marwan (\\d+)$"))
async def marwan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("البوصله ضاعت 🎧", callback_data="Xmar1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ابطال 🎧", callback_data="Xmar2 " + str(m.from_user.id))],
        [InlineKeyboardButton("النظام 🎧", callback_data="Xmar3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شيراتون 🎧", callback_data="Xmar4 " + str(m.from_user.id))],
        [InlineKeyboardButton("خربت 🎧", callback_data="Xmar5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نهاية العالم 🎧", callback_data="Xmar6 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني مروان موسي\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmar1 (\\d+)$"))
async def Xmar1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/102", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmar2 (\\d+)$"))
async def Xmar2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/103", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmar3 (\\d+)$"))
async def Xmar3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/104", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmar4 (\\d+)$"))
async def Xmar4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/105", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmar5 (\\d+)$"))
async def Xmar5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/106", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xmar6 (\\d+)$"))
async def Xmar6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/107", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^mosaeed (\\d+)$"))
async def mosaeed(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("لو 🎧", callback_data="Xsaed1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جواكي 🎧", callback_data="Xsaed2 " + str(m.from_user.id))],
        [InlineKeyboardButton("متغير 🎧", callback_data="Xsaed3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بيني وبينك 🎧", callback_data="Xsaed4 " + str(m.from_user.id))],
        [InlineKeyboardButton("مش بحكي 🎧", callback_data="Xsaed5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وحدي لكن 🎧", callback_data="Xsaed6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مفيش بديل 🎧", callback_data="Xsaed7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ياويلي 🎧", callback_data="Xsaed8 " + str(m.from_user.id))],
        [InlineKeyboardButton("بدون مواعيد 🎧", callback_data="Xsaed9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شتا 🎧", callback_data="Xsaed10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني محمد سعيد\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsaed1 (\\d+)$"))
async def Xsaed1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/53", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed2 (\\d+)$"))
async def Xsaed2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/54", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed3 (\\d+)$"))
async def Xsaed3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/55", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed4 (\\d+)$"))
async def Xsaed4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/56", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed5 (\\d+)$"))
async def Xsaed5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/57", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed6 (\\d+)$"))
async def Xsaed6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/58", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed7 (\\d+)$"))
async def Xsaed7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/59", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed8 (\\d+)$"))
async def Xsaed8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/116", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed9 (\\d+)$"))
async def Xsaed9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/61", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsaed10 (\\d+)$"))
async def Xsaed8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/62", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^sahby (\\d+)$"))
async def sahby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هلا والله 🎧", callback_data="Xsahb1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وداع يادنيا وداع 🎧", callback_data="Xsahb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("باتون ساليه 🎧", callback_data="Xsahb3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هاتلي فوديكا 🎧", callback_data="Xsahb4 " + str(m.from_user.id))],
        [InlineKeyboardButton("سكينه برازيلي 🎧", callback_data="Xsahb5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا حبيتك وجرحتيني 🎧", callback_data="Xsahb6 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا بيكا ماي لاف 🎧", callback_data="Xsahb7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عالم فاسد 🎧", callback_data="Xsahb8 " + str(m.from_user.id))],
        [InlineKeyboardButton("رب الكون ميزنا 🎧", callback_data="Xsahb9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شمس المجره 🎧", callback_data="Xsahb10 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنتخان 🎧", callback_data="Xsahb11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مساء النقص 🎧", callback_data="Xsahb12 " + str(m.from_user.id))],
        [InlineKeyboardButton("صاحبي دراعي 🎧", callback_data="Xsahb13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حب عمري نسيته وفاتني 🎧", callback_data="Xsahb14 " + str(m.from_user.id))],
        [InlineKeyboardButton("مساء النقص 🎧", callback_data="Xsahb15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شارب المرار 🎧", callback_data="Xsahb16 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة الاغاني الشعبي\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xsahb1 (\\d+)$"))
async def Xsahb1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb2 (\\d+)$"))
async def Xsahb2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb3 (\\d+)$"))
async def Xsahb3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/132", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb4 (\\d+)$"))
async def Xsahb4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/133", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb5 (\\d+)$"))
async def Xsahb5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/134", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb6 (\\d+)$"))
async def Xsahb6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/135", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb7 (\\d+)$"))
async def Xsahb7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb8 (\\d+)$"))
async def Xsahb8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb9 (\\d+)$"))
async def Xsahb9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/138", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb10 (\\d+)$"))
async def Xsahb10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/139", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb11 (\\d+)$"))
async def Xsahb11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/140", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb12 (\\d+)$"))
async def Xsahb12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb13 (\\d+)$"))
async def Xsahb13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/142", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb14 (\\d+)$"))
async def Xsahb14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb15 (\\d+)$"))
async def Xsahb15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/144", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xsahb16 (\\d+)$"))
async def Xsahb16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/145", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@app.on_callback_query(filters.regex("^tamer (\\d+)$"))
async def tamer(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مين ممكن 🎧", callback_data="Xtam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دا انا بابا 🎧", callback_data="Xtam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("كل ده علي ايه 🎧", callback_data="Xtam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي النيل 🎧", callback_data="Xtam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("العقده 🎧", callback_data="Xtam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نرجع 🎧", callback_data="Xtam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("في الحياه 🎧", callback_data="Xtam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حلو المكان 🎧", callback_data="Xtam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("نفس الحنين 🎧", callback_data="Xtam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لينا حياه بعدين 🎧", callback_data="Xtam10 " + str(m.from_user.id))],
        [InlineKeyboardButton("اختراع 🎧", callback_data="Xtam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بالف سلامه 🎧", callback_data="Xtam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("نفس النهايه 🎧", callback_data="Xtam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قولني كلام 🎧", callback_data="Xtam14 " + str(m.from_user.id))],
        [InlineKeyboardButton("فجأه افترقنا 🎧", callback_data="Xtam15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جرا اي يا عيني 🎧", callback_data="Xtam16 " + str(m.from_user.id))],
        [InlineKeyboardButton("ارجل 🎧", callback_data="Xtam17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خونتك 🎧", callback_data="Xtam18 " + str(m.from_user.id))],
        [InlineKeyboardButton("بتصعب عليا نفسي 🎧", callback_data="Xtam19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قلبي تعبان 🎧", callback_data="Xtam20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني تامر حسني\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xtam1 (\\d+)$"))
async def Xtam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/12", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam2 (\\d+)$"))
async def Xtam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/13", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam3 (\\d+)$"))
async def Xtam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/15", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam4 (\\d+)$"))
async def Xtam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/16", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam5 (\\d+)$"))
async def Xtam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/17", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam6 (\\d+)$"))
async def Xtam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/18", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam7 (\\d+)$"))
async def Xtam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/19", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam8 (\\d+)$"))
async def Xtam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/20", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam9 (\\d+)$"))
async def Xtam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/21", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam10 (\\d+)$"))
async def Xtam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/22", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam11 (\\d+)$"))
async def Xtam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/23", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam12 (\\d+)$"))
async def Xtam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/24", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam13 (\\d+)$"))
async def Xtam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/25", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam14 (\\d+)$"))
async def Xtam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/26", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam15 (\\d+)$"))
async def Xtam15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/27", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam16 (\\d+)$"))
async def Xtam16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/28", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam17 (\\d+)$"))
async def Xtam17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/29", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam18 (\\d+)$"))
async def Xtam18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/30", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam19 (\\d+)$"))
async def Xtam19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/31", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xtam20 (\\d+)$"))
async def Xtam20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musica568/32", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

@app.on_callback_query(filters.regex("^wegz (\\d+)$"))
async def wegz(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("نصين 🎧", callback_data="Xweg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سكرتي 🎧", callback_data="Xweg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("باظت 🎧", callback_data="Xweg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مش هقولك بيبي 🎧", callback_data="Xweg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("خربان 🎧", callback_data="Xweg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كدا كدا 🎧", callback_data="Xweg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("حواري 🎧", callback_data="Xweg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اي تي ام 🎧", callback_data="Xweg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("تي ان تي 🎧", callback_data="Xweg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دارت الغساله 🎧", callback_data="Xweg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("علي راحتي 🎧", callback_data="Xweg11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لقطه 🎧", callback_data="Xweg12 " + str(m.from_user.id))],
        [InlineKeyboardButton("دورك جاي 🎧", callback_data="Xweg13 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{app.username}?startgroup=new")],

    ])
    await m.message.edit_text("↢ اختر ماتريد من قائمة اغاني ويجز\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xweg1 (\\d+)$"))
async def Xweg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/88", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg2 (\\d+)$"))
async def Xweg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/89", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg3 (\\d+)$"))
async def Xweg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/90", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg4 (\\d+)$"))
async def Xweg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/91", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg5 (\\d+)$"))
async def Xweg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/92", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg6 (\\d+)$"))
async def Xweg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/93", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg7 (\\d+)$"))
async def Xweg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/94", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg8 (\\d+)$"))
async def Xweg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/95", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg9 (\\d+)$"))
async def Xweg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/96", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg10 (\\d+)$"))
async def Xweg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/97", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg11 (\\d+)$"))
async def Xweg11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/98", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg12 (\\d+)$"))
async def Xweg12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/99", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Xweg13 (\\d+)$"))
async def Xweg13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/ohyoco/100", reply_to_message_id=mid)
