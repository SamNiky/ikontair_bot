from telegram_bot.bot import Bot

bot = Bot("5812939803:AAFEkqZt6og8H97RcWsHBEP5LyF28QjGSPI")


@bot.message_handler(commands=["start"])
def command_handle_hello(message):
    bot.start_message(message)


@bot.message_handler(commands=["help"])
def command_handle_help(message):
    bot.help_message(message)


@bot.message_handler(commands=["generate_uuid4"])
def command_handle_uuid4(message):
    bot.default_generation(message)


@bot.message_handler(commands=["generate_md5"])
def command_handle_md5(message):
    bot.generate_by_MD5(message)


@bot.message_handler(commands=["generate_sha256"])
def command_handle_sha256(message):
    bot.generate_by_SHA256(message)


@bot.message_handler(regexp="[a-zA-Zа-яА-Я]")
def message_handle(message):
    if message.text == "UUID4":
        bot.default_generation(message)
    elif message.text == "MD5":
        bot.generate_by_MD5(message)
    elif message.text == "SHA256":
        bot.generate_by_SHA256(message)
    else:
        bot.not_valid_message(message)


if __name__ == "__main__":
    bot.infinity_polling()
