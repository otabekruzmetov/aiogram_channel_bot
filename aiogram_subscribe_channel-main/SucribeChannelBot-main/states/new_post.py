from aiogram.dispatcher.filters.state import State,StatesGroup

class NewPost(StatesGroup):
    NewMessage = State()
    Confirm = State()