import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from button import sherik
from states import malumot
from config import bot_token, admin


dp = Dispatcher()
bot = Bot(token=bot_token)



@dp.message(CommandStart())
async def command_start_handler(message: Message , state: FSMContext) -> None:
    await message.answer(f"Assalomu alaykum,{html.bold(message.from_user.full_name)}\nUstoz Shogirt botiga xush kelibsiz!" , reply_markup=sherik)
    await state.set_state(malumot.Fname)
    
        
@dp.message(malumot.Fname)
async def echo_handler(message:Message, state: FSMContext) -> None:
    await message.reply(f"Hozir sizga birnecha savollar beriladi.\nHar biriga javob bering\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.")
    await message.answer("Ismingizni to'liq qilib kiriting!")
    text = message.text
    await state.update_data(
        {"yonalish": text}
    )
    if text == "Sherik kerak":
        
        await state.update_data(
            {"tur": "Sherik"}
        )
    elif text == "Ustoz kerak":
        await state.update_data(
            {"tur": "Shogird"}
        )
    elif text == "Shogird kerak":
        await state.update_data(
            {"tur": "Ustoz"}
        )
    elif text == "Ish joyi kerak":
        state.update_data(
            {
                "tur": "Hodim"
            }
        )
        
    await state.set_state(malumot.age)
    
@dp.message(malumot.age)
async def gage(message: Message, state: FSMContext):
    await message.answer(
        text="Yoshingini kiriting: "
    )
    await state.update_data(
        {"fname": message.text}
    )
    await state.set_state(malumot.Texno)
    
@dp.message(malumot.Texno)
async def gage(message: Message, state: FSMContext):
    await message.answer(
        text="tillarni kiriting: "
    )
    await state.update_data(
        {"age": message.text}
    )
    await state.set_state(malumot.Tel)
    
@dp.message(malumot.Tel)
async def gage(message: Message, state: FSMContext):
    data = await state.get_data()
    y = data.get("yonalish")
    t = data.get("tur")
    n = data.get("fname")
    a = data.get("age")
    await message.answer(
        text=f"""{y}
        
{t}: {n}
Yoshi: {a}
Tillar: {message.text}"""
    )
    await bot.send_message(
        chat_id=admin,
        text="bu xabar faqat adminga yuboriladi"
    )
    await state.clear()
    

    
        
async def main() -> None:
    
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())







    



































# import asyncio
# import logging
# import sys
# from os import getenv

# from aiogram import Bot, Dispatcher, html,F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from config import bot_token
# from aiogram.types import Message


# logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# dp = Dispatcher()


# @dp.message(CommandStart("start"))
# async def cmd_start(message: Message):
#     fullname = message.from_user.id
#     await message.answer(f"Assalomu alayakum\n<a href = {'urls'}>{fullname}</a>")


# @dp.message(F.text)
# async def eco_bot(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


# async def main() -> None:
#     await dp.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())