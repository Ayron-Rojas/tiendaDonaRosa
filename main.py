import telebot
import time

import Funciones.funcionAgregar as Agregar
import Funciones.help as Ayuda
import Funciones.listar as Listar
import Funciones.Editar as Editar
import Funciones.eliminar as Eliminar
import Actividades.verificarCantidades as VerificarCantidades
import Actividades.obtenerCHAT_ID as CHAT_ID
import Funciones.Venta as Venta

TOKEN = "6826256087:AAHsXEr_yWAnZBjKNMTgvBZJ56_Hz5KExS8"

#Genero la conexion al bot y almaceno dicha conexion en una variable
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def saludar(mensaje):
    bot.reply_to(mensaje, "Hola, ¿en qué te puedo ayudar?")

# Devuelve un mensaje de ayuda que contiene todos los comandos
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
    Editar.editarArticulo(bot, articulosTienda, mensaje)
    
@bot.message_handler(commands= ["eliminar"])    
def editar(mensaje):
    Eliminar.eliminarArticulo(bot, articulosTienda, mensaje)
    
@bot.message_handler(commands=["verificar_cantidades"])
def ejecutarActividadVerificarCantidades(mensaje):
    chat_ID = CHAT_ID.obtenerCHAT_ID(TOKEN)
    VerificarCantidades.verificar_cantidades(bot, articulosTienda, chat_ID)

@bot.message_handler(commands=["venta"])
def productoVendido(mensaje):
    Venta.obtenerVenta(bot, articulosTienda, mensaje)
    
@bot.message_handler(func = lambda m: True)
def escucha_todo(mensaje):
    bot.reply_to(mensaje, """No reconozco ese mensaje, solo estoy aqui para ayudarle con su tiendita. Si gusta puede escribir /help para saber de que formas le puedo ayudar.""")

if __name__ == "__main__":
    bot.polling(none_stop=True)

while True:
    chat_ID = CHAT_ID.obtenerCHAT_ID(TOKEN)
    VerificarCantidades.verificar_cantidades(bot, articulosTienda, chat_ID)
    time.sleep(3600)
    
