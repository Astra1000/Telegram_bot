import telebot 
import logging

def register_handlers(bot):
  @bot.message_handler(commands=['minfo'])
  def ms_info(message):
    bot.send_message(message.chat.id, f"❕Список параметров 'message'.\n❗Ответ : {message}")
    logging.info(f"Команда распознана: {message.text}")
    #Вообще эта команда была создана чисто для себя, что бы смотреть какие параметры в "message" у телеграммма 
    #но вы можете оставить и посмотреть, если не хотите то удаляйте. 
