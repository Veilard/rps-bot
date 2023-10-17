from aiogram import F, Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from texts import win_replies, lose_replies, draw_replies




import sys
import asyncio
import logging
import random

TOKEN = '6401976116:AAF5Mm1IFHsIl6vs7aHaIbJguq_8APkptsE'
bot = Bot(token=TOKEN)
dp = Dispatcher()

max_score = 0

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="Начать игру")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard = True,
                                   input_field_placeholder="Да жми уже..")
    await message.answer(f"Привет, {message.from_user.full_name}! Я хочу поиграть с тобой в Камень-Ножницы-Бумага! \nПросто нажми \"Начать игру\" и мы приступим.", reply_markup=keyboard)



@dp.message(F.text.lower() == "начать игру")
async def round_count(message: Message):
    kb = [
        [
            types.KeyboardButton(text="3"),
            types.KeyboardButton(text="5"),
            types.KeyboardButton(text="10")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard = True,
                                   input_field_placeholder="Ты всё равно проиграешь🗿")
    await message.answer("До скольки играем?🤔", reply_markup=keyboard)


@dp.message(lambda message: message.text in ['3','5','10'])
async def start_game(message: Message):
    kb = [
        [
            types.KeyboardButton(text="Камень🗿"),
            types.KeyboardButton(text="Ножницы✂️"),
            types.KeyboardButton(text="Бумага📃")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,
                                   resize_keyboard = True,
                                   input_field_placeholder="Выбирай с умом😁")
    await message.answer("Выбирай 😁", reply_markup=keyboard)
    max_score = int(message.text)
    print(f'Max score set to {max_score}')


@dp.message(lambda message: message.text.lower() in ['камень🗿','ножницы✂️','бумага📃'])
async def initiate_round(message: Message):
    options = [1,2,3]
    user_win = bool
    bot_score = 0
    user_score = 0
    bot_choice = 0
    user_choice = 0

    if message.text.lower() in 'камень🗿':
        user_choice = options[0]
        bot_choice=random.choice(options)
    if message.text.lower() in 'бумага📃':
        user_choice = options[1]
        bot_choice=random.choice(options)
    if message.text.lower() in 'ножницы✂️':
        user_choice = options[2]
        bot_choice=random.choice(options)
    

    if bot_choice==1:
        await bot.send_message(message.from_user.id, "Камень🗿")
    if bot_choice==2:
        await bot.send_message(message.from_user.id, "Бумага📃")
    if bot_choice==3:
        await bot.send_message(message.from_user.id, "Ножницы✂️")
        
    if (user_choice==3 and bot_choice==1) or (user_choice==1 and bot_choice==2) or (user_choice==2 and bot_choice==3):
        user_win == False
        bot_score+=1
        # await asyncio.sleep(1)
        # await bot.send_message(message.from_user.id, "Бот победил.😢")
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, random.choice(win_replies))
    if (user_choice==3 and bot_choice==2) or (user_choice==1 and bot_choice==3) or (user_choice==2 and bot_choice==1):
        user_win == True
        user_score+=1
        # await asyncio.sleep(1)
        # await bot.send_message(message.from_user.id, "Вы победили!😎")
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, random.choice(lose_replies))
    if user_choice == bot_choice:
        # await asyncio.sleep(1)
        # await bot.send_message(message.from_user.id, "Ничья!🙃")
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, random.choice(draw_replies))

    print(user_score, bot_score)

# def end_game():
    

    # if user_score >= max_score:
    # # end_game()
    #    await bot.send_message(message.from_user.id, "Я проиграл битву, но не войну!")
    # if bot_score >= max_score:
    # # end_game()
    #     await bot.send_message(message.from_user.id, "Какой же ты мусор, братишка.")
    

async def main() -> None: 
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())