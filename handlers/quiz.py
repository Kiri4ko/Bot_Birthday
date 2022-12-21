"""Handler quiz. """

from aiogram.types import ReplyKeyboardRemove, InputFile

from buttons.buttons import *

from aiogram import Dispatcher, types

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram.utils.markdown import escape_md


class Quiz(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    question_6 = State()
    question_7 = State()
    question_8 = State()
    question_9 = State()
    question_10 = State()
    question_11 = State()
    question_12 = State()
    question_13 = State()
    question_14 = State()
    question_finish = State()


async def quiz_handler(message: types.Message, state: FSMContext):
    await message.answer(
        "Rules ☝️:\n"
        "I send a text of congratulations 🎁, and you guess \- who is the author❓\n"
        "Are you ready? 🤓👇",
        reply_markup=inline_buttons_quiz)

    await message.delete()
    await state.finish()


async def quiz_handler_call(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        "Rules ☝️:\n"
        "I send a text of congratulations 🎁, and you guess \- who is the author❓\n"
        "Are you ready? 🤓👇",
        reply_markup=inline_buttons_quiz
    )

    await state.finish()


async def q_1_handler(call: types.CallbackQuery, state: FSMContext):
    if call.data == "button_no":
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
        await call.message.answer_sticker('CAACAgEAAxkBAAEGM9JjWN3QrSC0bji6ck7NRSxVrnuJDQACKwADOA6CEaBt42BLtEN3KgQ')
        await call.message.answer(
            escape_md(
                "Please say yes✅\n"
                "I want to take the quiz with you 😇"),
            reply_markup=inline_buttons_quiz
        )
        return

    await call.message.answer_sticker('CAACAgEAAxkBAAEGM_BjWOqmUfNekev9sHNiOp0T9tEXgwACJQADOA6CEVpUi-04WXgFKgQ')
    await call.message.answer("*CONGRATULATIONS* \- 14 📬\n")
    await call.message.answer(f"*CONGRATULATION* 💌\-1:\n_{q_1.question}_", reply_markup=keyboard_name_q1)

    await state.set_state(Quiz.question_2.state)


async def q_2_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_1.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_1.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-2:\n_{q_2.question}_",
                         reply_markup=keyboard_name_q2)

    await state.set_state(Quiz.question_3.state)


async def q_3_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_2.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_2.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-3:\n_{q_3.question}_",
                         reply_markup=keyboard_name_q3)

    await state.set_state(Quiz.question_4.state)


async def q_4_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_3.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_3.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-4:\n_{q_4.question}_",
                         reply_markup=keyboard_name_q4)

    await state.set_state(Quiz.question_5.state)


async def q_5_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_4.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_4.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-5:\n_{q_5.question}_",
                         reply_markup=keyboard_name_q5)

    await state.set_state(Quiz.question_6.state)


async def q_6_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_5.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_5.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-6:\n_{q_6.question}_",
                         reply_markup=keyboard_name_q6)

    await state.set_state(Quiz.question_7.state)


async def q_7_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_6.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_6.answer} 🥳||")

    gif = InputFile('static/media/daddy.gif')
    await message.answer_animation(animation=gif, caption=f"*CONGRATULATION* 💌\-7:\n_{q_7.question}_",
                                   reply_markup=keyboard_name_q7)

    await state.set_state(Quiz.question_8.state)


async def q_8_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_7.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_7.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-8:\n_{q_8.question}_",
                         reply_markup=keyboard_name_q8)

    await state.set_state(Quiz.question_9.state)


async def q_9_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_8.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_8.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-9:\n_{q_9.question}_",
                         reply_markup=keyboard_name_q9)

    await state.set_state(Quiz.question_10.state)


async def q_10_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_9.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_9.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-10:\n_{q_10.question}_",
                         reply_markup=keyboard_name_q10)

    await state.set_state(Quiz.question_11.state)


async def q_11_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_10.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_10.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-11:\n_{q_11.question}_",
                         reply_markup=keyboard_name_q11)

    await state.set_state(Quiz.question_12.state)


async def q_12_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_11.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_11.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-12:\n_{q_12.question}_",
                         reply_markup=keyboard_name_q12)

    await state.set_state(Quiz.question_13.state)


async def q_13_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_12.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_12.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-13:\n_{q_13.question}_",
                         reply_markup=keyboard_name_q13)

    await state.set_state(Quiz.question_14.state)


async def q_14_handler(message: types.Message, state: FSMContext):
    if message.text[3:] == q_13.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_13.answer} 🥳||")

    await message.answer(f"*CONGRATULATION* 💌\-14:\n_{q_14.question}_",
                         reply_markup=keyboard_name_q14)

    await state.set_state(Quiz.question_finish.state)


async def q_handler_finish(message: types.Message, state: FSMContext):
    if message.text[3:] == q_14.answer:
        await message.answer_sticker('CAACAgEAAxkBAAEGM_RjWOyAAXD8tDeliBsgWszb0K6FuAACIgADOA6CEd4wNMezt3dkKgQ')
        await message.answer(escape_md("Yes✅, GOOD 😇"))
    else:
        await message.answer_sticker('CAACAgEAAxkBAAEGMVtjV7mzcmwQWp1MA0-M7CPafRlfAAMhAAM4DoIRwQjaTnufRQ4qBA')
        await message.answer(escape_md("Oops...Here's the answer 👉 ") + f"||{q_14.answer} 🥳||")

    await state.finish()
    await message.answer_sticker('CAACAgEAAxkBAAEGM_ZjWO7y5RqMlQItYItpWTkhyWczWgACLQADOA6CETXosuhOHHccKgQ')
    await message.answer(
        'Surprise 👉: [click me](https://yourwebsite)🎁',
        reply_markup=ReplyKeyboardRemove(), disable_web_page_preview=True
    )


def register_handlers_quiz(dp: Dispatcher):
    dp.register_callback_query_handler(q_1_handler, state=Quiz.question_1)
    dp.register_message_handler(q_2_handler, state=Quiz.question_2)
    dp.register_message_handler(q_3_handler, state=Quiz.question_3)
    dp.register_message_handler(q_4_handler, state=Quiz.question_4)
    dp.register_message_handler(q_5_handler, state=Quiz.question_5)
    dp.register_message_handler(q_6_handler, state=Quiz.question_6)
    dp.register_message_handler(q_7_handler, state=Quiz.question_7)
    dp.register_message_handler(q_8_handler, state=Quiz.question_8)
    dp.register_message_handler(q_9_handler, state=Quiz.question_9)
    dp.register_message_handler(q_10_handler, state=Quiz.question_10)
    dp.register_message_handler(q_11_handler, state=Quiz.question_11)
    dp.register_message_handler(q_12_handler, state=Quiz.question_12)
    dp.register_message_handler(q_13_handler, state=Quiz.question_13)
    dp.register_message_handler(q_14_handler, state=Quiz.question_14)
    dp.register_message_handler(q_handler_finish, state=Quiz.question_finish)
