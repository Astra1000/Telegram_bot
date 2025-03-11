#ВНИМАНИЕ ЭТО ОБНАВЛЕННАЯ ВЕРСИЯ main.py ДЛЯ ТЕХ КТО ХОЧЕТ ЧТО БЫ БОТ РАБОТАЛ ТОЛЬКО ДЛЯ НЕГО 
import logging  # библиотека для логирования
import os  # для работы с файловой системой
import sys  # для работы с путями
import telebot  # библиотека для взаимодействия с Telegram

# Конфигурируем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список разрешённых пользователей
ALLOWED_USERS = {123456789, 987654321}  # Замените на ID пользователей

# Middleware для проверки доступа
def check_access(bot, message):
    if message.from_user.id not in ALLOWED_USERS:
        bot.send_message(message.chat.id, "❕Соболнзную !\n⛔ У вас нет доступа к этому боту.")
        return False  # Прерываем дальнейшую обработку
    return True  # Продолжаем обработку

token = ""  # Замените на ваш токен, пример: 7947018177:AAEb-B5nbQoaTGYrf_4UkjP5BH0IYqmGGJL
bot = telebot.TeleBot(token)  # Создаем объект бота и передаем параметр token

# Подключаем middleware
bot.set_update_listener(check_access)

# Динамическая загрузка обработчиков команд
handlers_path = os.path.join(os.path.dirname(__file__), "handlers")
sys.path.append(handlers_path)  # Добавляем путь к папке с обработчиками в sys.path

for filename in os.listdir(handlers_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # Убираем ".py"
        try:
            module = __import__(module_name)  # Импортируем модуль
            if hasattr(module, 'register_handlers'):
                module.register_handlers(bot)
        except Exception as e:
            logging.error(f"Ошибка при загрузке обработчика {filename}: {e}")

bot.polling()  # Чтобы бот работал и не останавливался после запуска 


