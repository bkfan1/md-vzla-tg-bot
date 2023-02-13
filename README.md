# Monitor Dolar Venezuela Bot
@md_vzla_bot is a Telegram bot to get the current prices of the dollar from various financial sources. Made with Python


# How it works

1. The fetch_data function inside scraper.py file scrapes the web site: https://monitordolarvenezuela.com/
2. Each time the commands /precios or /precio are used, the bot sends a message with the fetched data in a readable format.
3. Steps 1 and 2 keeps repeating while the bot is on.
