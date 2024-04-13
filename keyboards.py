from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

parent_ch_button = KeyboardButton(text='🟢 Родитель')
teacher_ch_button = KeyboardButton(text='🔴 Преподаватель')

void_RKM = ReplyKeyboardRemove()
ch_role_RKM = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[parent_ch_button, teacher_ch_button]])

KEYBOARDS = {
    'void': void_RKM,
    'ch_role': ch_role_RKM,
}