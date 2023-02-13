# Monitor Dolar Venezuela Bot
@md_vzla_bot is a Telegram bot to get the current prices of the dollar from various financial sources. Created with Python (PyTelegramBotAPI, Requests, BeautifulSoup4).


# How it works

1. Bot is initialized by executing: python3 main.py.
2. Each time the user sends a valid command, the bot replies with a message 
    - If the command sent is /precios or /precio the bot will send scraped data from the website: https://monitordolarvenezuela.com/ formatted in a readable way.
3. Steps 1 and 2 keeps repeating while the bot is on.
