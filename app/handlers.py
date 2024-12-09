from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.getTemp as gt

rt = Router()

class Reg(StatesGroup):
   place = State()

@rt.message(Reg.place)
async def getTemoNow(message: Message, state: FSMContext):
    print("In this")
    await state.update_data(place = message.text)
    data = await state.get_data()
    tuple_of_data = gt.TempToday(data["place"])
    await message.answer(f"{tuple_of_data[0]}\nTemperature:{tuple_of_data[1]}")
    await state.clear()

@rt.callback_query(F.data == "choosePlace")
async def choose_place(callback: CallbackQuery, state: FSMContext):
   await state.set_state(Reg.place)
   await callback.message.answer("Enter your city in Russian")

@rt.message(CommandStart())
async def start(message: Message):
  builder = InlineKeyboardBuilder()
  builder.add(InlineKeyboardButton(
        text="What is the weather like today?",
        callback_data="choosePlace")
  )
  await message.reply(
      f"Hello {message.from_user.username}, I'm SinopticBot \n I can help you get the information about your  location's temperature",
      reply_markup=builder.as_markup()
  )