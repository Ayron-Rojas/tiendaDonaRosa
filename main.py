import telebot
import Funciones.funcionAgregar as Agregar
import Funciones.help as Ayuda
import Funciones.listar as Listar
import Funciones.Editar as Editar

TOKEN = "6826256087:AAHsXEr_yWAnZBjKNMTgvBZJ56_Hz5KExS8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, ¿en qué te puedo ayudar?")

# CUANDO EJECUTE COMANDO /HELP, DEVOLVERA UN LISTADO DE LOS COMANDOS QUE PUEDE UTILIZAR CON EL BOT
@bot.message_handler(commands= ["help"])
def helpe(mensaje):
    Ayuda.helper(bot, mensaje)
   
articulosTienda = {} # Aqui almacenaremos los datos esta vacia para poder llenarla

@bot.message_handler(commands= ["ver"])
def agregar(mensaje):
    Listar.listarProductos(bot, mensaje, articulosTienda)

# Almacenamos los datos de las frutas y verduras en el diccionario de arriba
@bot.message_handler(commands= ["agregar"])
def mostrar(mensaje):
    Agregar.agregarArticulo(bot, articulosTienda, mensaje)
    
@bot.message_handler(commands= ["editar"])    
def editar(mensaje):
    Editar.editarProducto(bot, articulosTienda, mensaje)
    
@bot.message_handler(commands= ["eliminar"])    
def editar(mensaje):
    (bot, articulosTienda, mensaje)   
    
    


    

@bot.message_handler(func = lambda m: True)
def escucha_todo(mensaje):
    bot.reply_to(mensaje, """No reconozco ese mensaje, solo estoy aqui para ayudarle con su tiendita. Si gusta puede escribir /help para saber de que formas le puedo ayudar.""")

if __name__ == "__main__":
    bot.polling(none_stop=True)