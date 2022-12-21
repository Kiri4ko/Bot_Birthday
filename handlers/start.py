"""Handler start. """

from aiogram.types import (
    CallbackQuery,
    Message,
    ReplyKeyboardRemove,
    InputFile,
)

from buttons.buttons import *

from aiogram import Dispatcher

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Text

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram_calendar import dialog_cal_callback, DialogCalendar


class Authorization(StatesGroup):
    auth_user = State()


async def command_auth_handler(message: Message):
    await message.delete()
    await message.answer_sticker('CAACAgIAAxkBAAEF4AFjJ4JWO1pIKtf5I4jDPPXNz7eZgAAChwIAAladvQpC7XQrQFfQkCkE')
    await message.answer(
        f"HI, *{message.from_user.first_name}*✌\!\n"
        "I will calculate how old you are, for this, indicate the date of your birth \- using the calendar 🗓",
        reply_markup=await DialogCalendar().start_calendar()
    )


async def command_auth_handler_call(call: CallbackQuery):
    await call.message.answer_sticker('CAACAgIAAxkBAAEF4AFjJ4JWO1pIKtf5I4jDPPXNz7eZgAAChwIAAladvQpC7XQrQFfQkCkE')
    await call.message.answer(
        f"HI, *{call.from_user.first_name}*✌\!\n"
        "I will calculate how old you are, for this, indicate the date of your birth \- using the calendar 🗓",
        reply_markup=await DialogCalendar().start_calendar()
    )


async def process_dialog_calendar(call: CallbackQuery, callback_data: {}, state: FSMContext):
    selected, date = await DialogCalendar().process_selection(call, callback_data)
    if selected:
        await state.update_data(user_date=str(date.strftime("%d/%m/%Y")))
        await call.message.answer(
            f'*Date of Birth*: {date.strftime("%d/%m/%Y")} \- correct❓',
            reply_markup=inline_buttons_birthday
        )


async def command_start_handler(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()
    if date.get('user_date') != "21/04/1989": # authorization by date
        await call.message.answer_sticker('CAACAgEAAxkBAAEGNlBjWiIi-UPJBPb3kSAl7j7GBqEcpwACKAADOA6CEeJAhB3GAAE0IioE')
        await call.message.answer(
            f"Oops\.\.\. For you *{call.from_user.first_name}*, congratulations not found\!\n",
            reply_markup=inline_buttons_repeat
        )
        await state.finish()
        return
    else:
        await call.message.answer_sticker('CAACAgIAAxkBAAEGMShjV6AxD4c7gnOqPBsAAZ_PSa9zzvMAAosCAAJWnb0K97RiJg2PO_MqBA')
        photo = InputFile('static/media/birthday.jpg')
        await call.message.answer_photo(photo=photo, caption=
        f"HI, *Name*✌\! 😍\n"
        "*HAPPY BIRTHDAY* 🎂\n"
        "I am your personal holiday boot 🤖\.\n"
        "Your closest and beloved \- not without my help, prepared a surprise 🎁\.\n"
        "To get it you have to play a quiz with me 🎮\.\n"
        f"If you are ready, press \|*I want a surprise* 🎁\| and flew 🚀🌔👇",
                                        reply_markup=inline_buttons_start
                                        )
        await state.finish()


async def cmd_cancel_handler(message: Message, state: FSMContext):
    await message.answer("Current action \- cancel 🛑", reply_markup=ReplyKeyboardRemove())
    await message.bot.delete_message(message.chat.id, message.message_id)
    await state.finish()


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_auth_handler, commands="start", state="*")
    dp.register_callback_query_handler(process_dialog_calendar, dialog_cal_callback.filter())
    dp.register_message_handler(cmd_cancel_handler, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel_handler, Text(equals="cancel", ignore_case=True), state="*")
    dp.register_callback_query_handler(command_start_handler, state=Authorization.auth_user)
