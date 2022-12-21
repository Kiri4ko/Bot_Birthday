# **Bot Birthday v.1.0.0. After passing the quiz: question-answer, displays a congratulatory message.**
# **This is a functional telegram bot. The aiogram library was used.**


### What the bot can do:
1. User verification by date of birth..
2. Launches a question and answer quiz
3. Displays a congratulatory message. 


***Directory files***:\
**./buttons/buttons.py** - Inline buttons registration and keyboard answer options\
**./handlers/callback.py** - Each command this is a separate handlers\
**./handlers/quiz.py** - Quiz structure\
**./handlers/start.py** - Start message, command registration\
**./filters/filters.py** - Word ban functionality\
**./filters/cens.json** - List filter of banned words (Russian and English)\
**./questions/congratulations.py** - Text congratulations\
**./questions/mystery.py** - Quiz Template\
**./static/** - Static files\
**./requirements.txt** - Dependency\
**./Makefile** - Commands: run and install requirements\
**./config.py** - Your values are indicated: TOKEN - your bot\
**./HB_Bot.py** - Bot launch
