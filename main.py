import telebot

TOKEN = "6826256087:AAHsXEr_yWAnZBjKNMTgvBZJ56_Hz5KExS8"

bot = telebot.TeleBot(TOKEN)

articulosTienda = {} # Aqui almacenaremos los datos esta vacia para poder llenarla

# Almacenamos los datos de las frutas y verduras en el diccionario de arriba
@bot.message_handler(commands="agregar")
def agregarArticulo(mensaje):
    # Vamos a dividir el mensaje en en palabras para que en un solo mensaje envie codigo, producto, precio, cantidad
    palabras = mensaje.text.split()[1:]
    
    # Verificamos si entregaron los 4 datos para evitar errores mas adelante
    if len(palabras) != 4:
        bot.reply_to(mensaje, "Por favor, proporciona el codigo, nombre, precio, cantidad")
        return
    
    # Como ya verificamos ahora si agregamos // Ojo que ahi son variables que le paso las palabras
    codigo = palabras[0]
    producto = palabras[1]
    precio = palabras[2]
    cantidad = palabras[3]
    
    # Este es un constructor de articulos
    articulosTienda[codigo] = {"producto": producto, "precio": precio, "cantidad": cantidad}
    bot.reply_to(mensaje, f"Articulo agregado: {producto}")


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