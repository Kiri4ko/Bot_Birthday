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
    question=escape_md(Name_1),
    answer="Name 1",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_2 = Mystery(
    question=escape_md(Name_2),
    answer="Name 2",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_3 = Mystery(
    question=escape_md(Name_3),
    answer="Name 3",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_4 = Mystery(
    question=escape_md(Name_4),
    answer="Name 4",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_5 = Mystery(
    question=escape_md(Name_5),
    answer="Name 5",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_6 = Mystery(
    question=escape_md(Name_6),
    answer="Name 6",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_7 = Mystery(
    question=escape_md(Name_7),
    answer="Name 7",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_8 = Mystery(
    question=escape_md(Name_8),
    answer="Name 8",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_9 = Mystery(
    question=escape_md(Name_9),
    answer="Name 9",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_10 = Mystery(
    question=escape_md(Name_10),
    answer="Name 10",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_11 = Mystery(
    question=escape_md(Name_11),
    answer="Name 11",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_12 = Mystery(
    question=escape_md(Name_12),
    answer="Name 12",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_13 = Mystery(
    question=escape_md(Name_13),
    answer="Name 13",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)

q_14 = Mystery(
    question=escape_md(Name_14),
    answer="Name 14",
    choices=["Name 1", "Name 2", "Name 3", "Name 4"]
)
