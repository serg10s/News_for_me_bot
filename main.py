from aiogram import executor
from parser import *
from keyboard import *
from admin import *
from aiogram.dispatcher.filters import Command
from database import *


new = News()
new.create_tabla()

dp.register_message_handler(proces_text, Command("add"))


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer("Hello, choose button", reply_markup=keyboard)


@dp.message_handler(commands=["new"])
async def add_new(message: types.Message):
    await message.answer(await new.get_news())


@dp.message_handler(commands=["News"])
async def process_news(message: types.Message):
    button1 = InlineKeyboardButton("❤️", callback_data="like_0")
    button2 = InlineKeyboardButton("🤮", callback_data="dislike_0")
    button3 = InlineKeyboardButton("Next", callback_data="next_0")
    inline_keyboard = InlineKeyboardMarkup().add(button1, button2).add(button3)
    news = parser_news()
    news_all = news[0]
    await bot.send_photo(chat_id=message.from_user.id, photo=news_all["img"],
                         caption=news_all["text"] + " Link of news: " + f"{news_all['link']}",
                         reply_markup=inline_keyboard)


@dp.callback_query_handler(text_startswith="next")
async def proces_next_news(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    all_news = parser_news()
    index_el = int(callback.data.split("_")[-1])
    try:
        next_news = all_news[index_el+1]
    except IndexError:
        await callback.message.answer(text="News is over, that return to back click /News")
    button1 = InlineKeyboardButton("❤️", callback_data=f"like_{index_el+1}")
    button2 = InlineKeyboardButton("🤮", callback_data=f"dislike_{index_el+1}")
    button3 = InlineKeyboardButton("Next", callback_data=f"next_{index_el+1}")
    inline_keyboard = InlineKeyboardMarkup().add(button1, button2).add(button3)
    await callback.bot.send_photo(chat_id=callback.from_user.id, photo=next_news["img"],
                                  caption=next_news["text"] + f" Link of news: {next_news['link']}",
                                  reply_markup=inline_keyboard)


@dp.callback_query_handler(text_startswith="like")
async def process_like(callback: types.CallbackQuery):
    await callback.answer(text="You like this news")


@dp.callback_query_handler(text_startswith="dislike")
async def process_dislike(callback: types.CallbackQuery):
    await callback.answer(text="You dislike this news")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
