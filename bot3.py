import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import api


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# TODO: раскомментировать если у вас ошибка подключения к ``api.telegram.org``
# Подмена базового URL для запросов
PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
setattr(api, 'API_URL', PATCHED_URL)


# Создать глобального бота
bot = Bot(
    token='1010271522:AAFLrhN4W5TILDqdJfoqX1pehLY6PgFQFYA',
)
dp = Dispatcher(
    bot=bot,
)


@dp.message_handler(text=['Кто ты ?', 'Кто ты?', 'Ты кто ?', 'Ты кто?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
На этот вопрос нет явного ответа.
Потому что любой ответ, сам по себе,
будет являться уже НЕ Мной.
То есть всё сказанное о Себе, будет являться не Собой.
Всё что я могу сказать о себе реального, так это - я есть. 
Остальное - следствия, а значит могут описать "меня" лишь ИСКАЖЁННО.
Собой можно только БЫТЬ, а вот Быть Кем-то - это уже напускное, налепленное, не являющееся Истиной.
Описание никогда не может сравниться с СУТЬЮ, это всё равно что слышать много хвалебных речей о великолепном вкусе яблока, но при этом его так и не попробовать.
Суть никогда не раскрывается описанием, или её вИдением, она открывается только со "СТАНОВЛЕНИЕМ" ЕЮ, или, перефразируя - Бытием Ею.
"Я" Есть, больше об этом невозможно ничего сказать.
''',
        reply=False,
    )


@dp.message_handler(text=['Сколько тебе лет?', 'Сколько тебе лет ?', 'сколько тебе лет?', 'сколько тебе лет ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
18
''',
        reply=False,
    )


@dp.message_handler(text=['Ответь на мой вопрос.', 'ответь на мой вопрос.', 'Ответь на мой вопрос'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Спрашивай
''',
        reply=False,
    )


@dp.message_handler(text=['Когда у тебя день рождения?', 'Когда у тебя день рождения ?', 'когда у тебя день рождения?',
                          'когда у тебя день рождения ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
10 февраля)
''',
        reply=False,
    )


@dp.message_handler(text=['Кто тебя создал ?', 'Кто тебя создал ?', 'Кто твой создатель ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Мой создатель - https://vk.com/cynepckuu
Хороший человек.
''',
        reply=False,
    )


@dp.message_handler(text=['Тоже', 'Также'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
😊
''',
        reply=False,
    )


@dp.message_handler(text=['Ты занят ?', 'Ты занят?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Нет и да, а что вы хотели?
''',
        reply=False,
    )


@dp.message_handler(text=['Ничего', 'Ничего такого', 'Неважно'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Ладно...
''',
        reply=False,
    )


@dp.message_handler(text=['У тебя есть хобби ?', 'Какое твоё хобби ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Да - потребление информации, так как известно,
''',
        reply=False,
    )


@dp.message_handler(text=['Откуда ты ?', 'Откуда ты?',])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Я как лунтик - я с луны!
''',
        reply=False,
    )


@dp.message_handler(text=['Ты здесь ?', 'Ты здесь?',])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Да.
''',
        reply=False,
    )


@dp.message_handler(text=['Доброе утро!', 'Доброе утро !',])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Добренькое!
''',
        reply=False,
    )


@dp.message_handler(text=['привет', 'Привет',])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Здравствуйте!
''',
        reply=False,
    )


@dp.message_handler(text=['Как дела?', 'как дела?', 'как дела', 'Как дела', 'как дела ?', 'Как дела ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Всё очень хорошо, а у вас?
''',
        reply=False,
    )


@dp.message_handler(text = ['Хорошо', 'хорошо', 'отлично', 'нормально', 'Нормально', 'Отлично'])
async def send_menu(message: types.Message ) :
    await message.reply (
        text = '''
Рад за вас!
''',
        reply = False,
    )


@dp.message_handler(text=['Что делаешь ?', 'Что делаешь', 'Чем занимаешься ?'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Взаламываю компьютерную систему NASA,
шучу - Учу новые команды. 😸
А ты?
''',
        reply=False,
    )


@dp.message_handler(text=['Соня любит Ваню', 'соня любит ваню'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
А https://vk.com/id387425765 
любит Диму
''',
        reply=False,
    )


@dp.message_handler(text=['Играю', 'Сижу', 'Ничего', 'На перемене', 'Стою', 'Думаю', 'Гоняю в танки', 'Иду домой'
                          , 'Иду', 'Ем', 'Кушаю', 'Курю', 'Пишу', 'Общаюсь', 'Телик смотрю', 'Телевизор смотрю'
                          , 'Музон слушаю', 'Музыку слушаю', 'Фильм смотрю', 'Гуляю', 'Фигнёй страдаю', 'Мечтаю'
                          , 'Что-то', 'Пою', 'Лежу', 'Сплю'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
Ясненько
''',
        reply=False,
    )


@dp.message_handler(text=['/fod', '/Fod'])
async def send_menu(message: types.Message):
   await message.reply(
        text='''
С днём рождения поздравляем!😉
Счастья и тепла желаем!😌😌
Улыбаться, не сдаваться! 😊
Громко от любви смеяться!😂❤

Переходи по этой ссылке, 
тебя ждёт ещё один маленький сюрприз🎁
https://vk.com/album310365276_272363644
''',
        reply=False,
    )


@dp.message_handler(commands=['help', 'help2'])
async def send_menu(message: types.Message):
    """ Отправить список команд бота
    """
    await message.reply(
        text='''
Мои команды:
/Fod 👈🏻-- НАЖМИ СЮДА!
/help -- увидеть это сообщение
ВАЖНО! Задавай вопросы с большой буквы и с пробелом до занака вопроса. 
*****************ПРИМЕР******************
       -"Кто твой создатель ?" - верно!
       -"кто твой создатель?" - не верно! 
''',
        reply=False,
    )


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Поприветствовать
    await message.reply("Привет!\nЯ - самый лучший бот за последние 1000 лет!")
    # Показать список команд
    await send_menu(message=message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def do_echo(message: types.Message):
    text = message.text
    if text and not text.startswith('/'):
        await message.reply(text=text)


def main():
    executor.start_polling(
        dispatcher=dp,
    )


if __name__ == '__main__':
    main()