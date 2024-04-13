import logging
import codecs
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ContentType

from states import BotStates
from admin import TOKEN, PASSWORD
from messages import MESSAGES
from keyboards import KEYBOARDS

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

class workWithFiles:
    def findGrades(chat_id, subject, surname, birth_date):
        try:
            filename = subject.lower() + ".txt"
            with codecs.open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 4:
                        file_last_name = parts[0]
                        file_birth_date = parts[2]
                        if file_last_name == surname and file_birth_date == birth_date:
                            grades = [int(grade) for grade in parts[3:]]
                            return grades
                return False
        except FileNotFoundError:
            return False

    def addGrade(last_name, subject, grade):
        try:
            filename = subject.lower() + ".txt"
            with codecs.open(filename, "r+", encoding="utf-8") as file:
                lines = file.readlines()
                found = False
                for i, line in enumerate(lines):
                    parts = line.split()
                    if len(parts) >= 1:
                        file_last_name = parts[0]
                        if file_last_name == last_name:
                            lines[i] = line.strip() + " " + grade + "\n"
                            found = True
                            break
                if not found:
                    return False
                file.seek(0)
                file.writelines(lines)
                return True
        except FileNotFoundError:
            return False

class HelpFunc:
    def createMessageWithGrades(subject, surname, grades):
        average = sum(grades) / len(grades)
        mess = f"Учащийся: {surname}\nОценки по предмету {subject}: {grades}\n"
        mess += f"Среднняя оценка: {average}"
        return (mess)

async def errorInvalidSurnameOrBirth (bot: Bot, id, mess):
    await bot.send_message(chat_id = id, text = mess)

@dp.message(Command("start"))
async def startMessage(message: types.Message, state: FSMContext):
    await state.set_state('*')
    if message.chat.type == 'private':
        await state.set_state(BotStates.CHOICE_ROLE)
        await message.answer(MESSAGES['start'], reply_markup=KEYBOARDS['ch_role'])

@dp.message(BotStates.CHOICE_ROLE, F.content_type == ContentType.TEXT)
async def choiceRole(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        if message.text == '🟢 Родитель':
            await state.set_state(BotStates.PARENT_1)
            await message.answer(MESSAGES['parent_choice'],reply_markup=KEYBOARDS['void'])
        elif message.text == '🔴 Преподаватель':
            await state.set_state(BotStates.TEACHER_1)
            await message.answer(MESSAGES['teacher_enter_password'],reply_markup=KEYBOARDS['void'])
        else:
            await message.answer(MESSAGES['error_choice'], reply_markup=KEYBOARDS['ch_role'])

@dp.message(BotStates.PARENT_1, F.content_type == ContentType.TEXT)
async def enterSurnameParent(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        mess_args = message.text.split()[:3]
        if workWithFiles.findGrades(message.chat.id, mess_args[2], mess_args[0], mess_args[1]):
            grades = workWithFiles.findGrades(message.chat.id, mess_args[2], mess_args[0], mess_args[1])
            await state.set_state(BotStates.PARENT_1)
            await message.answer(text = HelpFunc.createMessageWithGrades(mess_args[2], mess_args[0], grades))
        else:
            await message.answer(MESSAGES['invalid_surname_or_birth'])

@dp.message(BotStates.TEACHER_1, F.content_type == ContentType.TEXT)
async def enterPasswordTeacher(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        if message.text == PASSWORD:
            await state.set_state(BotStates.TEACHER_2)
            await message.answer(MESSAGES['teacher_work'])
        else:
            await message.answer(MESSAGES['incorrect_password'])

@dp.message(BotStates.TEACHER_2, F.content_type == ContentType.TEXT)
async def enterGradeTeacher(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        mess_args = message.text.split()[:3]
        if int(mess_args[2]) >= 2 and int(mess_args[2]) <= 5:
            if workWithFiles.addGrade(mess_args[0], mess_args[1], mess_args[2]):
                await state.set_state(BotStates.TEACHER_2)
                await message.answer(MESSAGES['add_grade'])
            else:
                await message.answer(MESSAGES['invalid_surname_or_birth'])
        else:
            await message.answer(MESSAGES['incorrect_grade'])

async def BotStarting():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(BotStarting())