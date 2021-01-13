from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
random.seed(random.random())

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "htoya")

@dp.message_handler(commands=['htoya'])
async def process_htoya_command(message: types.Message):
    await message.reply("Кароче, ти...")
    count_img = 8
    array_nazvi = ['typo zero','Не Рижа Беркут','Лисий із бразерс','Рижа Мавпа','Порноактьор','Бог','Говяжий Анус','Ти тепер сліпий, апзахзп','Розплата Готема']
    number_img = random.randint(1,count_img)
    title_img = array_nazvi[number_img]
    await bot.send_photo(message.chat.id,'https://paravozzalupa.at.ua/'+str(number_img)+'.png', caption = title_img)

if __name__ == '__main__':
    executor.start_polling(dp)
