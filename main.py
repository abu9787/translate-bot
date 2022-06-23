import json
import requests
from aiogram import Bot, Dispatcher,executor,types
from bot_traslate import API_TOKEN

app_id  = "6c47c119"
app_key  = "bcde8784b37068900a30dfadf8b9903d"

bt=Bot(token=API_TOKEN)
bo=Dispatcher(bt)

@bo.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Salom translate botga xush kelibsiz {message.from_user.first_name}!\nInglizcha so'z kirting ruschaga tarjima qilaman.")

@bo.message_handler()
async def echo(message: types.Message):
    word_id = message.text
    url = "https://od-api.oxforddictionaries.com/api/v2/translations/en/ru/" + word_id.lower() +"?strictMatch=false"
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}).json()
    ans = r['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['translations'][0]['text']
    await message.answer(ans)


if __name__ == "__main__":
    executor.start_polling(bo)