from core.handlers.basic import *
from core.keyboards.inline import *
from core.settings import settings

from aiogram.fsm.context import FSMContext

messages_to_delete = {}


async def get_faq_inline_keyboard(call: CallbackQuery, bot: Bot):
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/faq.png', FAQ_MESSAGE,
                                                    back_to_menu_inline_keyboard)


async def get_privacy_policy_inline_keyboard(call: CallbackQuery, bot: Bot):
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/privacy.png', PRIVACY_MESSAGE,
                                                    back_to_menu_inline_keyboard)


async def get_terms_of_use_inline_keyboard(call: CallbackQuery, bot: Bot):
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/terms.png', TERMS_OF_USE,
                                                    back_to_menu_inline_keyboard)


async def try_to_delete_messages(bot: Bot, call: CallbackQuery):
    chat_id = call.from_user.id
    if chat_id in messages_to_delete:
        try:
            await bot.delete_messages(chat_id=chat_id, message_ids=messages_to_delete[chat_id])
        except Exception as delete_messages_error:
            print(f"Ошибка при удалении сообщений: {delete_messages_error}")

    try:
        await call.message.delete()
    except Exception as delete_call_message_error:
        print(f"Ошибка при удалении вызывающего сообщения: {delete_call_message_error}")

    if chat_id in messages_to_delete:
        messages_to_delete[chat_id].clear()


async def send_message_and_add_to_delete(call: CallbackQuery, bot: Bot, message_text: str, keyboard):
    await try_to_delete_messages(bot, call)
    message = await call.message.answer(text=message_text, reply_markup=keyboard)

    chat_id = call.from_user.id
    if chat_id not in messages_to_delete:
        messages_to_delete[chat_id] = []
    messages_to_delete[chat_id].append(message.message_id)


async def send_message_with_photo_and_add_to_delete(call: CallbackQuery, bot: Bot, photo_path: str, caption: str,
                                                    keyboard):
    await try_to_delete_messages(bot, call)
    photo = FSInputFile(photo_path)
    message = await call.message.answer_photo(photo=photo, caption=caption, reply_markup=keyboard)

    chat_id = call.from_user.id
    if chat_id not in messages_to_delete:
        messages_to_delete[chat_id] = []
    messages_to_delete[chat_id].append(message.message_id)


async def get_menu_inline_keyboard(call: CallbackQuery, bot: Bot):
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/menu.png', MENU_MESSAGE,
                                                    menu_inline_keyboard)


async def get_services_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/services.png', SERVICES_MESSAGE,
                                                    services_inline_keyboard)


async def get_country_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == 'send_note':
        await state.update_data(GET_SERVICE='Подать записку')
    elif call.data == 'light_candle':
        await state.update_data(GET_SERVICE='Поставить свечу')
    await send_message_and_add_to_delete(call, bot, COUNTRY_MESSAGE, countries_inline_keyboard)


async def get_russia_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    country = countries_dict[call.data]
    await state.update_data(COUNTRY=country)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, russia_inline_keyboard)


async def get_moscow_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, NOTE_TEMPLES_MESSAGE, moscow_inline_keyboard)


async def get_spb_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, NOTE_TEMPLES_MESSAGE, spb_inline_keyboard)


async def get_rostov_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, NOTE_TEMPLES_MESSAGE, rostov_inline_keyboard)


async def get_kazan_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, NOTE_TEMPLES_MESSAGE, kazan_inline_keyboard)


async def get_nizhniy_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, NOTE_TEMPLES_MESSAGE, nizhniy_novgorod_inline_keyboard)


async def get_belarus_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    country = countries_dict[call.data]
    await state.update_data(COUNTRY=country)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, belarus_inline_keyboard)


async def get_brest_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, brest_inline_keyboard)


async def get_polotsk_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, polotsk_inline_keyboard)


async def get_zhirovichy_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, zhirovichy_inline_keyboard)


async def get_kozhany_temples(call: CallbackQuery, bot: Bot, state: FSMContext):
    city = cities_dict[call.data]
    await state.update_data(CITY=city)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, kozhany_inline_keyboard)


async def get_greece_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    country = countries_dict[call.data]
    await state.update_data(COUNTRY=country)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, greece_inline_keyboard)


async def get_israel_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    country = countries_dict[call.data]
    await state.update_data(COUNTRY=country)

    await send_message_and_add_to_delete(call, bot, CITY_MESSAGE, israel_inline_keyboard)


async def get_service_types(call: CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    if data['GET_SERVICE'] == 'Подать записку':
        await state.update_data(TEMPLE=temples_dict[call.data])

        db = Db()
        temple_id = await db.get_temple_id_by_name(temples_dict[call.data])
        services = await db.get_services_by_temple_id(temple_id)

        text = 'Прейскурант цен на услугу <i>"Поставить свечу"</i> в данном храме:\n\n'

        price_descriptions = {
            "note_once_price": "Разовая услуга",
            "note_month_price": "Месяц (каждую неделю - 4 раза)",
            "note_half_year_price": "Полгода (каждую неделю - 24 раза)",
            "note_year_price": "Год (каждую неделю - 48 раз)"
        }

        service_keys = [
            "note_once_price", "note_month_price", "note_half_year_price", "note_year_price"
        ]

        for service_info in services:
            for i, key in enumerate(service_keys, start=2):
                price = service_info[i]
                if price > 0:
                    text += f'<i>{price_descriptions[key]} - {price / 100}₽</i>\n'

        await send_message_and_add_to_delete(call, bot, text, notes_inline_keyboard)


    elif data['GET_SERVICE'] == 'Поставить свечу':
        await state.update_data(TEMPLE=temples_dict[call.data])
        db = Db()
        temple_id = await db.get_temple_id_by_name(temples_dict[call.data])
        services = await db.get_services_by_temple_id(temple_id)

        text = 'Прейскурант цен на услугу <i>"Поставить свечу"</i> в данном храме:\n\n'

        price_descriptions = {
            "candle_once_price": "Разовая услуга",
            "candle_month_price": "Месяц (каждую неделю - 4 раза)",
            "candle_half_year_price": "Полгода (каждую неделю - 24 раза)",
            "candle_year_price": "Год (каждую неделю - 48 раз)"
        }

        service_keys = [

            "candle_once_price", "candle_month_price", "candle_half_year_price", "candle_year_price"
        ]

        for service_info in services:
            for i, key in enumerate(service_keys, start=6):  # начинаем с индекса 2, предполагая первые два поля не цены
                price = service_info[i]
                if price > 0:
                    text += f'<i>{price_descriptions[key]} - {price / 100}₽</i>\n'

        await send_message_and_add_to_delete(call, bot, text, light_candle_inline_keyboard)


async def get_period_inline_keyboard(call: CallbackQuery, bot: Bot, state: FSMContext):
    type_ = types_dict[call.data]
    await state.update_data(TYPE=type_)
    await send_message_and_add_to_delete(call, bot, PERIOD_MESSAGE, periods_inline_keyboard)


async def create_order(call: CallbackQuery, bot: Bot, state: FSMContext):
    period = periods_dict[call.data]
    await state.update_data(PERIOD=period)

    new_data = await state.get_data()

    temple = new_data['TEMPLE']
    type_ = new_data['TYPE']
    country = new_data['COUNTRY']
    city = new_data['CITY'] if 'CITY' in new_data else None
    service = new_data['GET_SERVICE']

    print(f'{temple}, {type_}, {country}, {city}, {service}, {period}')

    db = Db()
    order_total = await db.get_order_total(temple, call.data, service)
    await state.update_data(TOTAL=order_total)
    total_price = order_total // 100
    if city is None:
        text_message = f"Ваш заказ:\n\nУслуга: <i>{service}</i>\nОписание: <i>{type_}</i>\nПериод: <i>{period}</i>\nСтрана: <i>{country}</i>\nХрам: <i>{temple}</i>\nСтоимость: <i>{total_price},00 руб.</i>"
    else:
        text_message = f"Ваш заказ:\n\nУслуга: <i>{service}</i>\nОписание: <i>{type_}</i>\nПериод: <i>{period}</i>\nСтрана: <i>{country}</i>\nГород: <i>{city}</i>\nХрам: <i>{temple}</i>\nСтоимость: <i>{total_price},00 руб.</i>"

    await bot.send_message(chat_id=call.from_user.id, text=text_message, reply_markup=payment_inline_keyboard)


async def pay_order(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    amount = data.get('TOTAL')
    service = data.get('GET_SERVICE')
    _type = data.get('TYPE')
    temple = data.get('TEMPLE')
    country = data.get('COUNTRY')
    city = data.get('CITY')
    if city is None:
        text = f"{country}, {temple}"
    else:
        text = f"{country}, {city}, {temple}"
    await call.bot.send_invoice(

        chat_id=call.from_user.id,
        title=f"{service}, {_type}",
        description=text,
        provider_token=settings.bots.provider_token,
        payload='payload',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Оплата услуги',
                amount=amount
            )
        ],
        start_parameter='duhovnyjpomoshnikbot',
        provider_data=None,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        request_timeout=60
    )


async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    print(pre_checkout_query)


async def success_payment(message: Message, bot: Bot, state: FSMContext):
    try:
        db = Db()
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = await state.get_data()
        user_id = await db.get_user_id_by_chat_id(message.from_user.id)
        temple_id = await db.get_temple_id_by_name(data.get('TEMPLE'))
        service = data.get('GET_SERVICE')
        _type = data.get('TYPE')
        period = data.get('PERIOD')
        amount = message.successful_payment.total_amount // 100
        phone = message.successful_payment.order_info.phone_number
        email = message.successful_payment.order_info.email

        await db.create_order(user_id, phone, email, amount, temple_id, service, _type, period, current_date)

        await bot.send_message(message.from_user.id, text=f'<i>Оплата на сумму {amount},00 руб. прошла успешно!</i>\n\n'
                                                          f'<i>Отследить статус вашего заказа, можно в личном кабинете, '
                                                          f'Хорошего дня!</i>',
                               reply_markup=go_to_profile_inline_keyboard)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


async def get_profile_inline_keyboard(call: CallbackQuery, bot: Bot):
    db = Db()
    date = await db.get_user_reg_date_by_chat_id(call.from_user.id)
    username = call.from_user.username if call.from_user.username else 'Не указано'
    last_name = call.from_user.last_name if call.from_user.last_name else 'Не указано'
    await send_message_with_photo_and_add_to_delete(call, bot, 'assets/img/profile.png',
                                                    profile_message.format(call.from_user.first_name,
                                                                           last_name,
                                                                           username,
                                                                           call.from_user.id,
                                                                           date),
                                                    profile_inline_keyboard)


async def get_orders_inline_keyboard(call: CallbackQuery, bot: Bot):
    await send_message_and_add_to_delete(call, bot, ORDERS_MESSAGE, orders_history_inline_keyboard)


async def get_waiting_orders(call: CallbackQuery, bot: Bot):
    db = Db()
    user_id = await db.get_user_id_by_chat_id(call.from_user.id)
    orders = await db.get_users_orders_status_waiting(user_id)
    if orders:
        response = ""
        for order in orders:
            temple_info = await db.get_temple_info_by_id(order[6])
            temple_name = temple_info[0]
            country = temple_info[1]
            city = temple_info[2] if temple_info[2] != '-' else ''
            status = 'В ожидании' if order[5] == 'waiting' else order[5]
            response += f"{country} - {city} - {temple_name} - {order[7]} - {order[8]} - {order[10]} - {status}\n\n"
        await bot.send_message(call.from_user.id, text=response, reply_markup=go_to_profile_inline_keyboard)
    else:
        await bot.send_message(call.from_user.id, text='У вас нет ожидающих заказов.',
                               reply_markup=go_to_profile_inline_keyboard)


async def get_in_progress_orders(call: CallbackQuery, bot: Bot):
    db = Db()
    user_id = await db.get_user_id_by_chat_id(call.from_user.id)
    orders = await db.get_user_orders_status_in_progress(user_id)
    if orders:
        response = ""
        for order in orders:
            temple_info = await db.get_temple_info_by_id(order[6])
            temple_name = temple_info[0]
            country = temple_info[1]
            city = temple_info[2] if temple_info[2] != '-' else ''
            status = 'Выполняется' if order[5] == 'in_progress' else order[5]
            response += f"{country} - {city} - {temple_name} - {order[7]} - {order[8]} - {order[10]} - {status}\n\n"
        await bot.send_message(call.from_user.id, text=response, reply_markup=go_to_profile_inline_keyboard)
    else:
        await bot.send_message(call.from_user.id, text='У вас нет заказов в статусе выполнения.',
                               reply_markup=go_to_profile_inline_keyboard)


async def get_completed_orders(call: CallbackQuery, bot: Bot):
    db = Db()
    user_id = await db.get_user_id_by_chat_id(call.from_user.id)
    orders = await db.get_user_orders_status_completed(user_id)
    if orders:
        response = ""
        for order in orders:
            temple_info = await db.get_temple_info_by_id(order[6])
            temple_name = temple_info[0]
            country = temple_info[1]
            city = temple_info[2] if temple_info[2] != '-' else ''
            status = 'Выполнен' if order[5] == 'completed' else order[5]
            response += f"{country} - {city} - {temple_name} - {order[7]} - {order[8]} - {order[10]} - {status}\n\n"
        await bot.send_message(call.from_user.id, text=response, reply_markup=go_to_profile_inline_keyboard)
    else:
        await bot.send_message(call.from_user.id, text='У вас нет завершенных заказов.',
                               reply_markup=go_to_profile_inline_keyboard)
