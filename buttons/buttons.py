from questions.mystery import *

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
)

# buttons Inline

inline_surprise = InlineKeyboardButton(text='Хочу сюрприз 🎁', callback_data="button_surprise")
surprise_button = InlineKeyboardMarkup().add(inline_surprise)
inline_yes = InlineKeyboardButton(text='Да✅', callback_data="button_yes")
yes_button = InlineKeyboardMarkup().add(inline_yes)
inline_no = InlineKeyboardButton(text='Нет❌', callback_data="button_no")
no_button = InlineKeyboardMarkup().add(inline_no)

inline_right = InlineKeyboardButton(text='Да✅', callback_data="button_right")
right_button = InlineKeyboardMarkup().add(inline_right)
inline_wrong = InlineKeyboardButton(text='Нет❌', callback_data="button_wrong")
wrong_button = InlineKeyboardMarkup().add(inline_wrong)

inline_repeat = InlineKeyboardButton(text='Повторить 🔂', callback_data="button_repeat")
repeat_button = InlineKeyboardMarkup().add(inline_repeat)

inline_sorry = InlineKeyboardButton(text='Sorry 🙏', callback_data="button_sorry")
sorry_button = InlineKeyboardMarkup().add(inline_sorry)

inline_buttons_start = InlineKeyboardMarkup(row_width=1)
inline_buttons_start.add(inline_surprise)

inline_buttons_quiz = InlineKeyboardMarkup(row_width=2)
inline_buttons_quiz.add(
    inline_yes,
    inline_no,
)

inline_buttons_birthday = InlineKeyboardMarkup(row_width=2)
inline_buttons_birthday.add(
    inline_right,
    inline_wrong,
)

inline_buttons_repeat = InlineKeyboardMarkup(row_width=1)
inline_buttons_repeat.add(inline_repeat)

inline_buttons_sorry = InlineKeyboardMarkup(row_width=1)
inline_buttons_sorry.add(inline_sorry)

# buttons Keyboard

keyboard_name_q1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_1.choices:
    keyboard_name_q1.insert(name)

keyboard_name_q2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_2.choices:
    keyboard_name_q2.insert(name)

keyboard_name_q3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_3.choices:
    keyboard_name_q3.insert(name)

keyboard_name_q4 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_4.choices:
    keyboard_name_q4.insert(name)

keyboard_name_q5 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_5.choices:
    keyboard_name_q5.insert(name)

keyboard_name_q6 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_6.choices:
    keyboard_name_q6.insert(name)

keyboard_name_q7 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_7.choices:
    keyboard_name_q7.insert(name)

keyboard_name_q8 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_8.choices:
    keyboard_name_q8.insert(name)

keyboard_name_q9 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for name in q_9.choices:
    keyboard_name_q9.insert(name)

keyboard_name_q10 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for name in q_10.choices:
    keyboard_name_q10.insert(name)

keyboard_name_q11 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for name in q_11.choices:
    keyboard_name_q11.insert(name)

keyboard_name_q12 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for name in q_12.choices:
    keyboard_name_q12.insert(name)

keyboard_name_q13 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for name in q_13.choices:
    keyboard_name_q13.insert(name)

keyboard_name_q14 = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for name in q_14.choices:
    keyboard_name_q14.insert(name)

