#Что это ? Это улучшенная версия main.py
#Что изменилось ? В данной версии бот отвечает ТОЛЬКО если человек подписан на канал.
#Еще не тестировалась

import logging # библиотека для логировагия
import os # не помню зачем
import sys #не помню зачем 
import telebot # библиотека для взаимодействия с тг

# Конфигурируем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

token = "<Ваш токен>" # Замените на ваш токен, пример : 7947018177:AAEb-B5nbQoaTGYrf_4UkjP5BH0IYqmGGJL

CHANNEL_ID = '@your_channel'  # Замените на ID вашего канала

def check_subscription(user_id):
    """
    Функция для проверки подписки пользователя на канал.
    Возвращает True, если пользователь подписан, иначе False.
    """
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status != 'left'
    except Exception as e:
        logger.error(f"Ошибка при проверке подписки: {e}")
        return False

bot = telebot.TeleBot(token) #Создаем объект бота и передаем параметр token 

# Динамическая загрузка обработчиков команд
handlers_path = os.path.join(os.path.dirname(__file__), "handlers")
sys.path.append(handlers_path) # Добавляем путь к папке с обработчиками в sys.path

for filename in os.listdir(handlers_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3] # Убираем ".py"
        try:
            module = __import__(module_name) # Импортируем модуль
            if hasattr(module, 'register_handlers'):
                module.register_handlers(bot)
        except Exception as e:
            logger.error(f"Ошибка при загрузке обработчика {filename}: {e}")

bot.polling() # что бы бот работал а не останавливался после запуска
