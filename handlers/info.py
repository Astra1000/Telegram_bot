import telebot
import logging
from telebot import types

def get_user_info(value, default_message="❗Ошибка получения данных!"):
    return value if value else default_message

def register_handlers(bot):
    @bot.message_handler(commands=['info'])
    def why_i(message):
        logging.info(f"Команда распознана: {message.text}")
        
        name = get_user_info(message.from_user.first_name, "❗Ошибка получения имени!")
        famili = get_user_info(message.from_user.last_name, "❗Ошибка получения фамилии!")
        us = get_user_info(message.from_user.username, "❗Ошибка получения username!")
        userid = message.from_user.id
        language = get_user_info(message.from_user.language_code, "❗Ошибка получения языка!")
        is_bot = "Да" if message.from_user.is_bot else "Нет"

        markup = types.InlineKeyboardMarkup()
        copy_id_button = types.InlineKeyboardButton(text="Скопировать ID", callback_data=f"copy_id_{userid}")
        copy_username_button = types.InlineKeyboardButton(text="Скопировать юзернейм", callback_data=f"copy_username_{us}")
        markup.add(copy_id_button, copy_username_button)

        bot.send_message(message.chat.id, f"[🔎]Данные которые я получил[🔎]\n\n⤷ 😃 Имя : {name}\n⤷ 😀 Фамилия : {famili}\n\n⤷ ❕Юзернейм : {us}\n⤷ 🆔 ID: {userid}\n⤷ 🌐 Язык: {language}\n⤷ 🤖 Бот: {is_bot}\n\n❗Если возникла ошибка при получении параметра, возможно, он не заполнен.\n❕Данные берутся из Telegram по их API.", reply_markup=markup)

        photos = bot.get_user_profile_photos(userid)
        if photos.total_count > 0:
            bot.send_photo(message.chat.id, photos.photos[0][-1].file_id, caption="Ваш аватар:")
        else:
            bot.send_message(message.chat.id, "У вас нет аватара.")

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        if call.data.startswith("copy_id_"):
            user_id = call.data.split("_")[2]
            bot.answer_callback_query(call.id, f"ID скопирован: {user_id}")
        elif call.data.startswith("copy_username_"):
            username = call.data.split("_")[2]
            bot.answer_callback_query(call.id, f"Юзернейм скопирован: @{username}")
