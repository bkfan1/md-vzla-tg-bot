from telebot.types import BotCommand

bot_commands = [
    BotCommand('/iniciar, /start', 'Iniciar el bot.'),
    BotCommand(
        '/precios', 'Consultar el precio del dolar en todos los monitores disponibles.'),
    BotCommand(
        '/precio', ' Consultar el precio del dolar en un monitor en específico.'),
    BotCommand('/ayuda, /help',
               'Obtener información útil sobre el uso y funcionamiento del bot.')
]
