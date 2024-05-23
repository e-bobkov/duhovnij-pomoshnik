from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

go_to_menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🕊️ Меню 🕊️", callback_data="go_to_menu")]
    ]
)

back_to_menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🕊️ Меню 🕊️", callback_data="go_to_menu")]
    ]
)

menu_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text="🕊️ Услуги", callback_data="services"), ],
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="📃 Условия использования", callback_data="terms_of_use")],
        [InlineKeyboardButton(text="📜 Политика конфиденциальности", callback_data="privacy_policy")],
        [InlineKeyboardButton(text="🆘 Поддержка", url="https://t.me/jumangee_man")],
    ]
)

services_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подать записку 📝", callback_data="send_note")],
        [InlineKeyboardButton(text="Поставить свечу 🕯", callback_data="light_candle")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="go_to_menu")],
    ]
)

light_candle_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="За здравие 🧘🏻", callback_data="for_health")],
        [InlineKeyboardButton(text="За упокой 🪦", callback_data="for_repose")],
        [InlineKeyboardButton(text="За здравие и упокой ✨", callback_data="for_health_and_repose")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="services")],
    ]
)

notes_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Семейное благополучие 💑", callback_data="family_wellbeing")],
        [InlineKeyboardButton(text="Здоровье и дети 🤰👶", callback_data="health_and_children")],
        [InlineKeyboardButton(text="Успокоение души ☮️", callback_data="soul_calm")],
        [InlineKeyboardButton(text="Развитие - духовное и физическое 📚💪", callback_data="development")],
        [InlineKeyboardButton(text="Защита от бед и зла 🛡️", callback_data="protection")],
        [InlineKeyboardButton(text="Поддержка в сложных ситуациях 🤝", callback_data="support")],
        [InlineKeyboardButton(text="Наставничество в бизнесе и обучении 👨‍🏫📈", callback_data="mentorship")],
        [InlineKeyboardButton(text="Память о погибших 🕊️", callback_data="memory_of_the_dead")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="services")],

    ]
)

countries_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Россия 🇷🇺", callback_data="_rus")],
        [InlineKeyboardButton(text="Беларусь 🇧🇾", callback_data="_bel")],
        [InlineKeyboardButton(text="Греция 🇬🇷", callback_data="_gre")],
        [InlineKeyboardButton(text="Израиль 🇮🇱", callback_data="_isr")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="services")],

    ]
)

russia_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Москва", callback_data="_moscow")],
        [InlineKeyboardButton(text="Санкт-Петербург", callback_data="_spb")],
        [InlineKeyboardButton(text="Ростов-на-Дону", callback_data="_rostov")],
        [InlineKeyboardButton(text="Казань", callback_data="_kazan")],
        [InlineKeyboardButton(text="Нижний Новгород", callback_data="_nizhny_novgorod")],
        [InlineKeyboardButton(text="Дивеево", callback_data="rus_1")],
        [InlineKeyboardButton(text="Оптина пустынь", callback_data="rus_2")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="send_note")],
    ]
)

moscow_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Храм Христа Спасителя", callback_data="msc_1")],
        [InlineKeyboardButton(text="Собор Василия Блаженного", callback_data="msc_2")],
        [InlineKeyboardButton(text="Новодевичий монастырь", callback_data="msc_3")],
        [InlineKeyboardButton(text="Данилов монастырь", callback_data="msc_4")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_rus")],
    ]
)

spb_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Исаакиевский собор", callback_data="spb_1")],
        [InlineKeyboardButton(text="Казанский собор", callback_data="spb_2")],
        [InlineKeyboardButton(text="Собор Воскресения Христова", callback_data="spb_3")],
        [InlineKeyboardButton(text="Петропавловский собор", callback_data="spb_4")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_rus")],
    ]
)

rostov_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Собор Рождества Богородицы", callback_data="rstv_1")],
        [InlineKeyboardButton(text="Собор Святого Дмитрия Ростовского", callback_data="rstv_2")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_rus")],
    ]
)

kazan_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Троицкая церковь", callback_data="kzn_1")],
        [InlineKeyboardButton(text="Сергиевская церковь", callback_data="kzn_2")],
        [InlineKeyboardButton(text="Софийская церковь", callback_data="kzn_3")],
        [InlineKeyboardButton(text="Казанский собор", callback_data="kzn_4")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_rus")],
    ]
)

nizhniy_novgorod_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Собор Александра Невского", callback_data="nzn_1")],
        [InlineKeyboardButton(text="Собор Покрова на Ильинке", callback_data="nzn_2")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_rus")],
    ]
)

belarus_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Брест", callback_data="_brest")],
        [InlineKeyboardButton(text="Жировичи", callback_data="_zhirovichy")],
        [InlineKeyboardButton(text="Полоцк", callback_data="_polotsk")],
        [InlineKeyboardButton(text="Кожаны", callback_data="_kozhany")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="send_note")],
    ]
)

brest_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Свято-Николаевская Братская церковь", callback_data="brest_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_bel")],
    ]
)

zhirovichy_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Жировичский монастырь", callback_data="zhirovichy_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_bel")],
    ]
)

polotsk_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Спасо-Ефросиньевский монастырь", callback_data="polotsk_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_bel")],
    ]
)

kozhany_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Церковь Святого Николая", callback_data="kozhany_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="_bel")],
    ]
)

greece_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Монастырь Святого Павла", callback_data="grc_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="send_note")],
    ]
)

israel_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Храм Гроба Христа Господня", callback_data="isr_1")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="send_note")],
    ]
)

periods_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Разовый", callback_data="once")],
        # [InlineKeyboardButton(text="Недельный", callback_data="weekly")],
        [InlineKeyboardButton(text="Месячный", callback_data="month")],
        [InlineKeyboardButton(text="Полгода", callback_data="half_year")],
        [InlineKeyboardButton(text="Год", callback_data="year")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="services")],

    ]
)

payment_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить", callback_data="pay")],
        [InlineKeyboardButton(text="Отменить", callback_data="cancel")],
    ]
)

profile_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="История заказов", callback_data="orders_history")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="go_to_menu")],
    ]
)

orders_history_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="В ожидании", callback_data="waiting")],
        [InlineKeyboardButton(text="В процессе", callback_data="in_process")],
        [InlineKeyboardButton(text="Завершенные", callback_data="completed")],
        [InlineKeyboardButton(text="Назад ⬅️", callback_data="profile")],
    ]
)
go_to_profile_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")]
    ]
)
cities_dict = {
    "_moscow": "Москва",
    "_spb": "Санкт-Петербург",
    "_rostov": "Ростов-на-Дону",
    "_kazan": "Казань",
    "_nizhny_novgorod": "Нижний Новгород",
    "_brest": "Брест",
    "_zhirovichy": "Жировичи",
    "_polotsk": "Полоцк",
    "_kozhany": "Кожаны",
}

temples_dict = {
    "msc_1": "Храм Христа Спасителя",
    "msc_2": "Собор Василия Блаженного",
    "msc_3": "Новодевичий монастырь",
    "msc_4": "Данилов монастырь",
    "spb_1": "Исаакиевский собор",
    "spb_2": "Казанский собор",
    "spb_3": "Собор Воскресения Христова",
    "spb_4": "Петропавловский собор",
    "rstv_1": "Собор Рождества Богородицы",
    "rstv_2": "Собор Святого Дмитрия Ростовского",
    "kzn_1": "Троицкая церковь",
    "kzn_2": "Сергиевская церковь",
    "kzn_3": "Софийская церковь",
    "kzn_4": "Казанский собор",
    "nzn_1": "Собор Александра Невского",
    "nzn_2": "Собор Покрова на Ильинке",
    "rus_1": "Дивеево",
    "rus_2": "Оптина пустынь",
    "brest_1": "Свято-Николаевская Братская церковь",
    "zhirovichy_1": "Жировичский монастырь",
    "polotsk_1": "Спасо-Ефросиньевский монастырь",
    "kozhany_1": "Церковь Святого Николая",
    "grc_1": "Монастырь Святого Павла",
    "isr_1": "Храм Гроба Христа Господня",

}
periods_dict = {
    "once": "Разовый",
    "month": "Месячный",
    "half_year": "Полгода",
    "year": "Год",
}
countries_dict = {
    "_rus": "Россия",
    "_bel": "Беларусь",
    "_gre": "Греция",
    "_isr": "Израиль",
}

types_dict = {
    "for_health": "За здравие",
    "for_repose": "За упокой",
    "for_health_and_repose": "За здравие и упокой",
    "family_wellbeing": "Семейное благополучие",
    "health_and_children": "Здоровье и дети",
    "soul_calm": "Успокоение души",
    "development": "Развитие - духовное и физическое",
    "protection": "Защита от бед и зла",
    "support": "Поддержка в сложных ситуациях",
    "mentorship": "Наставничество в бизнесе и обучении",
    "memory_of_the_dead": "Память о погибших",
}
