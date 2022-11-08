from random import shuffle
from aiogram.utils.markdown import escape_md
from .congratulations import *


class Mystery:

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        self.choices = choices
        shuffle(self.choices)
        self.list_choices()

    def list_choices(self):
        for i in range(len(self.choices)):
            self.choices.insert(i, f"{i + 1}. {self.choices[i]}")
            self.choices.pop(i + 1)


q_1 = Mystery(
    question=escape_md(Rita_Zanko),
    answer="Рита Занько",
    choices=["Андрей Голузов", "Рита Занько", "Волошин Андрей", "Света Полоцкая"]
)

q_2 = Mystery(
    question=escape_md(Andrey_Goluzov),
    answer="Андрей Голузов",
    choices=["Маша Голузова", "Андрей Голузов", "Роман Мишкевич", "Виталий Казацкий"]
)

q_3 = Mystery(
    question=escape_md(Masha_Goluzova),
    answer="Маша Голузова",
    choices=["Лера Волошина", "Семья Понасюк", "Маша Голузова", "Дмитрий Киричко"]
)

q_4 = Mystery(
    question=escape_md(Andrey_Voloshin),
    answer="Андрей Волошин",
    choices=["Лера Волошина", "Тимофей Волошин", "Папа", "Андрей Волошин"]
)

q_5 = Mystery(
    question=escape_md(Lera_Voloshina),
    answer="Лера Волошина",
    choices=["Папа", "Лера Волошина", "Мама", "Муж"]
)

q_6 = Mystery(
    question=escape_md(Timofey_Voloshin),
    answer="Тимофей Волошин",
    choices=["Муж", "Тимофей Волошин", "Миша Пузевич", "Вадим Кричко"]
)

q_7 = Mystery(
    question=escape_md(Daddy),
    answer="Папа",
    choices=["Семья Зуевых", "Семья Понасюк", "Оксана Ковалёва", "Папа"]
)

q_8 = Mystery(
    question=escape_md(Husband),
    answer="Муж",
    choices=["Семья Понасюк", "Муж", "Семья Зуевых", "Оксана Ковалёва"]
)

q_9 = Mystery(
    question=escape_md(Ponasyuk_family),
    answer="Семья Понасюк",
    choices=["Наташа Киричко", "Дмитрий Киричко", "Семья Понасюк", "Семья Зуевых"]
)

q_10 = Mystery(
    question=escape_md(Natasha_Kirichko),
    answer="Наташа Киричко",
    choices=["Наташа Киричко", "Миша Пузевич", "Татьяна Кричко", "Оксана Ковалёва"]
)

q_11 = Mystery(
    question=escape_md(Oksana_Kovaleva),
    answer="Оксана Ковалёва",
    choices=["Оксана Ковалёва", "Света Полоцкая", "Анатолий Казацкий", "Семья Зуевых"]
)

q_12 = Mystery(
    question=escape_md(Zuevs_family),
    answer="Семья Зуевых",
    choices=["Татьяна Кричко", "Дмитрий Киричко", "Семья Зуевых", "Роман Мишкевич"]
)

q_13 = Mystery(
    question=escape_md(Misha_Puzevich),
    answer="Миша Пузевич",
    choices=["Миша Пузевич", "Анатолий Казацкий", "Виталий Казацкий", "Вадим Кричко"]
)

q_14 = Mystery(
    question=escape_md(Dima_Kirichko),
    answer="Дмитрий Киричко",
    choices=["Мирон Киричко", "Татьяна Кричко", "Дмитрий Киричко", "Марк Киричко"]
)
