from telebot import TeleBot, types
from generator.generator import SecurePassword


class Bot(TeleBot):
    hello = "Привет, давай я сгенерирую тебе пароль"
    description = "Я могу сделать пароль по алгоритму UUID4, MD5 или SHA256 - на твой вкус"
    keyboard_description = "Выбирай или нажми /"
    generate_by_UUID4_reply = "Твой пароль на основе UUID4"
    generate_by_MD5_reply = "Твой пароль на основе MD5"
    generate_by_SHA256_reply = "Твой пароль на основе SHA256"
    dont_understand_reply = "Я тебя не понял"

    @property
    def base_keyboard(self):
        keyboard = types.ReplyKeyboardMarkup()
        key_1 = types.KeyboardButton("UUID4")
        key_2 = types.KeyboardButton("MD5")
        key_3 = types.KeyboardButton("SHA256")
        keyboard.row(key_1, key_2, key_3)
        return keyboard

    def start_message(self, message):
        print("log-start-message")
        self.reply_to(message, self.hello)
        self.send_message(message.chat.id, self.description)
        self.send_message(message.chat.id, self.keyboard_description, reply_markup=self.base_keyboard)

    def default_generation(self, message):
        print("log-default-generation")
        self.reply_to(message, self.generate_by_UUID4_reply)
        password = SecurePassword.generate()
        self.send_message(message.chat.id, password)

    def generate_by_MD5(self, message):
        print("log-generation-by_md5")
        self.reply_to(message, self.generate_by_MD5_reply)
        password = SecurePassword.generate_by_MD5()
        self.send_message(message.chat.id, password)

    def generate_by_SHA256(self, message):
        print("log-generation-by-sha256")
        self.reply_to(message, self.generate_by_SHA256_reply)
        password = SecurePassword.generate_by_sha256()
        self.send_message(message.chat.id, password)

    def help_message(self, message):
        print("log-help")
        self.send_message(message.chat.id, self.description)
        self.send_message(message.chat.id, self.keyboard_description, reply_markup=self.base_keyboard)

    def not_valid_message(self, message):
        print("log-not-valid")
        self.reply_to(message, self.dont_understand_reply)
        self.help_message(message)
