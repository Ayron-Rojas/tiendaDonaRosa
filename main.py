import telebot
import funcionAgregar
from Comandos import Comando


TOKEN = "6826256087:AAHsXEr_yWAnZBjKNMTgvBZJ56_Hz5KExS8"

bot = telebot.TeleBot(TOKEN)

articulosTienda = {} # Aqui almacenaremos los datos esta vacia para poder llenarla

# Almacenamos los datos de las frutas y verduras en el diccionario de arriba
@bot.message_handler(commands= Comando.Agregar)
def agregar(mensaje):
    funcionAgregar.agregarArticulo(bot, articulosTienda, mensaje)

@bot.message_handler(commands=["start"])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, ¿en qué te puedo ayudar?")
    
@bot.message_handlers(commands=["Hola", "hola", "hi", "Hi"])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, ¿en qué te puedo ayudar?")

@bot.message_handler(func = lambda m: True)
def escucha_todo(mensaje):
    bot.reply_to(mensaje, "Actualmente solo estoy funcionando con los comandos '/start y /hola'")

if __name__ == "__main__":
    bot.polling(none_stop=True)