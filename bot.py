#! /usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from config import TOKEN
from config import ID_TRENER

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
jurnal = [1,2]
trenermode = [1]

#-- Команди для тренєра
@dp.message_handler(commands=['trener'])
async def process_trener_command(message: types.Message):
    if(message.from_user.id==ID_TRENER) :
        trenermode_status = 'on'
        if(trenermode[0] == 0) :
            trenermode_status = 'off,\nМожна нажимать на /htoya'
        await bot.send_message(message.from_user.id, 'Trener mode: '+trenermode_status+'\n/trener_on\n/trener_off')

@dp.message_handler(commands=['trener_on'])
async def process_trener_on_command(message: types.Message):
    if(message.from_user.id==ID_TRENER) :
        trenermode[0] = 1
        print('Trener mode: on')
        trenermode_status = 'on'
        if(trenermode[0] == 0) :
            trenermode_status = 'off,\nМожна нажимать на /htoya'
        await bot.send_message(message.from_user.id, 'Trener mode: '+trenermode_status+'\n/trener_on\n/trener_off')

@dp.message_handler(commands=['trener_off'])
async def process_trener_off_command(message: types.Message):
    if(message.from_user.id==ID_TRENER) :
        trenermode[0] = 0
        print('Trener mode: off')
        trenermode_status = 'on'
        if(trenermode[0] == 0) :
            trenermode_status = 'off,\nМожна нажимать на /htoya'
        await bot.send_message(message.from_user.id, 'Trener mode: '+trenermode_status+'\n/trener_on\n/trener_off')

#-- Команди для плєбєїв
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    #if(trenermode[0] == 0 or message.from_user.id==449474491) :
    if(trenermode[0] == 0) :
        await bot.send_message(message.from_user.id, "htoya")

@dp.message_handler(commands=['htoya'])
async def process_htoya_command(message: types.Message):
    print(str(message.chat))
    if(trenermode[0] == 0) :
        count_img = 8 # Кількість фото
        array_nazvi = ['','Не Рижа Беркут','Лисий із бразерс','Рижа Мавпа','Порноактьор','Бог','Говяжий Анус','Ти тепер сліпий, апзахзп','Розплата Готема'] # Підписи під фото по номеру
        # Генеруємо Рандомне число від 1 до count_img
        number_img = 1+random.randrange(count_img)
        # Дивимося в jurnal чи не було такого числа недавно, обновляєм jurnal
        while True :
            if number_img in jurnal :
                number_img = random.randint(1,count_img)
                continue
            else :
                jurnal.append(number_img)
                if(len(jurnal) > 5) :
                    jurnal.pop(0)
                break
        title_img = array_nazvi[number_img]
        # Отправляєм пісьма в паравоз
        await message.reply("Кароче, ти...")
        await bot.send_photo(message.chat.id,'https://paravozzalupa.at.ua/'+str(number_img)+'.png', caption = title_img)
if __name__ == '__main__':
    executor.start_polling(dp)

# https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
