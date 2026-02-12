import asyncio
import logging
import sys,os
from aiogram import Bot, Dispatcher,F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
load_dotenv()
API = "8469485602:AAF_GAv4Q7GlxatO2Llwa1aamrh4CQYAl10"
dp = Dispatcher()

menu=[
    'IT LIVE Haqida',
    "Kurslar",
    "Mentorlar",
    "Biz bilan bog`lanish",
    "Ishga joylashish",
    "Savol javob",
]
Menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=key)] for key in menu
    ]
)


@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",reply_markup=Menu)

@dp.message(F.text.in_(menu))
async def echo(message: Message) -> None:
    T=message.text
    if menu[0]==T: await message.answer("0")
    if menu[1]==T: await message.answer("1")
    if menu[2]==T: await message.answer("2")
    if menu[3]==T: await message.answer("3")
    if menu[4]==T: await message.answer("4")
@dp.message()
async def echo_handler(message: Message) -> None:
    T=message.text
    try:
        await message.answer(T)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
