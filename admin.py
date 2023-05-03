from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from loader import *
from database import *

base = News()
base.create_tabla()

ID = 629990425


class AddNews(StatesGroup):
    photo = State()
    text = State()
    link = State()


@dp.message_handler(commands=["add"])
async def add_news(message: types.Message):
    if message.from_user.id == ID:
        await AddNews.photo.set()
        await message.reply("Send photo of news")


@dp.message_handler(content_types=["photo"], state=AddNews.photo)
async def proces_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await AddNews.next()
    await message.reply("Send text of news")


@dp.message_handler(content_types=["text"], state=AddNews.text)
async def proces_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text
    await AddNews.next()
    await message.reply("Send link of news")


@dp.message_handler(state=AddNews.link)
async def proces_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["link"] = message.text

    #async with state.proxy() as data:
    #    await message.reply(str(data))
    await base.add_info(state)
    await state.finish()

