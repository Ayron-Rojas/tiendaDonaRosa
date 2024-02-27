import telebot

TOKEN = "6826256087:AAHsXEr_yWAnZBjKNMTgvBZJ56_Hz5KExS8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, ¿en qué te puedo ayudar?")

@bot.message_handler(func = lambda m: True)
def escucha_todo(mensaje):
    bot.reply_to(mensaje, "procesando")

if __name__ == "__main__":
    bot.polling(none_stop=True)
