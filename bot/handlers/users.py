from aiogram import types

from bot.loader import dp
from jira_api.data_fetcher import get_last_created_issue


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Hi, i'm intrusion bot, fuck u =)")


@dp.message_handler(commands=["last_issue"])
async def get_last_issue(message: types.Message):
    issue = get_last_created_issue()
    await message.answer(issue)


@dp.message_handler()
async def other(message: types.Message):
    await message.answer("ok")
