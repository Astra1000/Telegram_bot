import telebot

def register_handlers(bot):
    @bot.message_handler(commands=['start']) #непосредственно команда 
    def start(message):
        bot.send_message(message.chat.id, "❤‍🔥Приветствую тебя в тестовом боте 'Oreon'!\n❕Мои команды в статье : (тут вставте статью если нужно)")

