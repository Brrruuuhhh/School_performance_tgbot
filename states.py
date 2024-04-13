from aiogram.fsm.state import StatesGroup, State

class BotStates(StatesGroup):
    CHOICE_ROLE = State()

    PARENT_1 = State()
    PARENT_2 = State()

    TEACHER_1 = State()
    TEACHER_2 = State()
