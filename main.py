import config
import text
from aiogram import *
import logging
from sqlCommands import SQLighter


logging.basicConfig(level=logging.INFO)

#инициализация бота
bot = Bot(token=config.TOKKEN)
dp = Dispatcher(bot)

#инициализация базы данных
db = SQLighter('mitedb.db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.subscriber_exist(message.from_user.id):
        db.add_subscriber(message.from_user.id)
    await message.answer(text.srart_text, parse_mode='HTML')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text.help_text, )


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if not db.subscriber_exist(message.from_user.id):
        db.add_subscriber(message.from_user.id)
        await message.answer("Вы подписались на рассылку новостей.")
    else:
        db.update_subscription(message.from_user.id, True)
        await message.answer("Вы подписались на рассылку новостей.")


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if not db.subscriber_exist(message.from_user.id):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы не подписаны на рассылку новостей.")
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписались.")


@dp.message_handler(content_types=['photo'])
async def special(message: types.Message):
    if message.caption[:7] == "Special":
        text = message.caption[8:]
        photo = message.photo[0]
        subscriptions = db.get_subscriptions()
        for s in subscriptions:
            await bot.send_photo(s[1], caption=text, photo=photo["file_id"], disable_notification=True, parse_mode='html')


@dp.message_handler(commands=['specialHTML'])
async def specialHTML(message: types.Message):
    text = message.text.split('***')[0][13:]
    photo = message.text.split('***')[1]
    subscriptions = db.get_subscriptions()
    for s in subscriptions:
        await bot.send_photo(s[1], caption=text, photo=photo, disable_notification=True, parse_mode='html')

@dp.message_handler(commands=['testHTML'])
async def testHTML(message: types.Message):
    text = message.text.split('***')[0][10:]
    photo = message.text.split('***')[1]
    await bot.send_photo(message.from_user.id, caption=text, photo=photo, disable_notification=True, parse_mode='html')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,)