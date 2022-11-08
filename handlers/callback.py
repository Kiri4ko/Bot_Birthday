"""Register handler callback. """

from handlers.quiz import quiz_handler_call, q_1_handler

from handlers.start import command_start_handler, command_auth_handler_call

from aiogram import Dispatcher


def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_handler_call, text='button_surprise')
    dp.register_callback_query_handler(q_1_handler, text='button_yes')
    dp.register_callback_query_handler(q_1_handler, text='button_no')
    dp.register_callback_query_handler(command_start_handler, text='button_right')
    dp.register_callback_query_handler(command_auth_handler_call, text='button_wrong')
    dp.register_callback_query_handler(command_auth_handler_call, text='button_repeat')
    dp.register_callback_query_handler(command_auth_handler_call, text='button_sorry')
