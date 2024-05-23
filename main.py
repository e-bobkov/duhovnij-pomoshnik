import asyncio
import logging

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram import F

from core.settings import settings
from core.handlers.callbacks import *
from core.handlers.basic import *


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot started!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot has stopped!!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command('start'))

    dp.callback_query.register(get_menu_inline_keyboard, F.data.startswith('go_to_menu'))

    dp.callback_query.register(get_services_inline_keyboard, F.data.startswith('services'))
    dp.callback_query.register(get_faq_inline_keyboard, F.data.startswith('faq'))
    dp.callback_query.register(get_terms_of_use_inline_keyboard, F.data.startswith('terms_of_use'))
    dp.callback_query.register(get_privacy_policy_inline_keyboard, F.data.startswith('privacy_policy'))
    dp.callback_query.register(get_profile_inline_keyboard, F.data.startswith('profile'))

    # Услуги
    dp.callback_query.register(get_country_inline_keyboard, F.data.startswith('send_note'))
    dp.callback_query.register(get_country_inline_keyboard, F.data.startswith('light_candle'))

    # Россия
    dp.callback_query.register(get_russia_inline_keyboard, F.data.startswith('_rus'))

    dp.callback_query.register(get_moscow_temples, F.data.startswith('_moscow'))
    dp.callback_query.register(get_spb_temples, F.data.startswith('_spb'))
    dp.callback_query.register(get_rostov_temples, F.data.startswith('_rostov'))
    dp.callback_query.register(get_kazan_temples, F.data.startswith('_kazan'))
    dp.callback_query.register(get_nizhniy_temples, F.data.startswith('_nizhny_novgorod'))

    dp.callback_query.register(get_service_types, F.data.startswith('msc_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('msc_2'))
    dp.callback_query.register(get_service_types, F.data.startswith('msc_3'))
    dp.callback_query.register(get_service_types, F.data.startswith('msc_4'))

    dp.callback_query.register(get_service_types, F.data.startswith('spb_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('spb_2'))
    dp.callback_query.register(get_service_types, F.data.startswith('spb_3'))
    dp.callback_query.register(get_service_types, F.data.startswith('spb_4'))

    dp.callback_query.register(get_service_types, F.data.startswith('rstv_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('rstv_2'))

    dp.callback_query.register(get_service_types, F.data.startswith('kzn_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('kzn_2'))
    dp.callback_query.register(get_service_types, F.data.startswith('kzn_3'))
    dp.callback_query.register(get_service_types, F.data.startswith('kzn_4'))

    dp.callback_query.register(get_service_types, F.data.startswith('nzn_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('nzn_2'))

    dp.callback_query.register(get_service_types, F.data.startswith('rus_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('rus_2'))

    # Беларусь
    dp.callback_query.register(get_belarus_inline_keyboard, F.data.startswith('_bel'))

    dp.callback_query.register(get_brest_temples, F.data.startswith('_brest'))
    dp.callback_query.register(get_zhirovichy_temples, F.data.startswith('_zhirovichy'))
    dp.callback_query.register(get_polotsk_temples, F.data.startswith('_polotsk'))
    dp.callback_query.register(get_kozhany_temples, F.data.startswith('_kozhany'))

    dp.callback_query.register(get_service_types, F.data.startswith('brest_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('zhirovichy_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('polotsk_1'))
    dp.callback_query.register(get_service_types, F.data.startswith('kozhany_1'))

    # Греция
    dp.callback_query.register(get_greece_inline_keyboard, F.data.startswith('_gre'))

    dp.callback_query.register(get_service_types, F.data.startswith('grc_1'))

    # Израиль
    dp.callback_query.register(get_israel_inline_keyboard, F.data.startswith('_isr'))

    dp.callback_query.register(get_service_types, F.data.startswith('isr_1'))

    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('for_health'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('for_repose'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('for_health_and_repose'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('family_wellbeing'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('health_and_children'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('soul_calm'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('development'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('protection'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('support'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('mentorship'))
    dp.callback_query.register(get_period_inline_keyboard, F.data.startswith('memory_of_the_dead'))

    dp.callback_query.register(create_order, F.data.startswith('once'))
    dp.callback_query.register(create_order, F.data.startswith('month'))
    dp.callback_query.register(create_order, F.data.startswith('half_year'))
    dp.callback_query.register(create_order, F.data.startswith('year'))

    dp.callback_query.register(pay_order, F.data.startswith('pay'))
    dp.callback_query.register(get_menu_inline_keyboard, F.data.startswith('cancel'))
    dp.pre_checkout_query.register(process_pre_checkout_query)
    dp.message.register(success_payment, F.successful_payment)

    dp.callback_query.register(get_orders_inline_keyboard, F.data.startswith('orders_history'))
    dp.callback_query.register(get_waiting_orders, F.data.startswith('waiting'))
    dp.callback_query.register(get_completed_orders, F.data.startswith('completed'))
    dp.callback_query.register(get_in_progress_orders, F.data.startswith('in_process'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
