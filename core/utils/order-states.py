from aiogram.fsm.state import State, StatesGroup


class OrderState(StatesGroup):
    GET_SERVICE = State()

    GET_PERIOD = State()

    CITY = State()
    COUNTRY = State()
    TEMPLE = State()

    TYPE = State()

    TOTAL = State()
    SERVICE_ID = State()

