from selenium import webdriver
import time
from telegram.ext import Updater, CommandHandler
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('initiating the cum')
    driver = webdriver.Firefox()

    while True:
        driver.get("https://www.google.com/search?client=firefox-b-d&q=btc+to+usd")
        price = driver.find_element_by_css_selector(".SwHCTb").text
        price = price.replace(".", "")
        price = price.replace(",", "")
        price = float(price)

        while True:
            driver.get("https://www.google.com/search?client=firefox-b-d&q=btc+to+usd")
            current = driver.find_element_by_css_selector(".SwHCTb").text
            current = current.replace(".", "")
            current = current.replace(",", "")
            current = float(current)
            if current > price + price*(2/10000):
                update.message.reply_text("BTC is up by %0.002. Current price is", str(current))
                break
            if current < price - price*(2/10000):
                update.message.reply_text("BTC price is down by %0.002. Current price is", str(current))
                break
            else:
                print("no change")
                time.sleep(60)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1798195848:AAH6Ol6kWRaO7-p7EUDGPmf7Ls0YXvenQbA", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))



    # log all errors
    dp.add_error_handler(logging.error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
