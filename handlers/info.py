import telebot
import logging

def register_handlers(bot):
    @bot.message_handler(commands=['info']) #сама команда 
    def why_i(message):
        logging.info(f"Команда распознана: {message.text}")
        name = message.from_user.first_name if message.from_user.first_name else "❗Ошибка получения имени!"
        famili = message.from_user.last_name if message.from_user.last_name else "❗Ошибка получения фамилии!"
        us = message.from_user.username if message.from_user.username else "❗Ошибка получения username!"
        userid = message.from_user.id

        bot.send_message(message.chat.id, f"[🔎]Данные которые я получил[🔎]\n\n⤷ 😃 Имя : {name}\n⤷ 😀 Фамилия : {famili}\n\n⤷ ❕Юзернейм : {us}\n⤷ 🆔 ID: {userid}\n\n❗Если возникла ошибка при получение параметра то возможно он не заполнен.\n❕Данные берутся из телеграмма по их API.")

        logging.info(f"Команда распознана: {message.text}\nРезультат:\nИмя: {name}\nФамилия: {famili}\nUsername: {us}\nID: {userid}")
#Почему обработка ошибок добавленна только в юзернейм ; имени ; фамилии ? 
#Потому что данные параметры могут вернуть None например если там пусто, и что бы команда нормально обрабатывлась добавлено if ; else
