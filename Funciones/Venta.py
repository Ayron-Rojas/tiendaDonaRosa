import telebot

# Le estoy entregando: la conexion al bot
# la lista de los productos
# el nombre del producto que vendi
# la cantidad que vendi

def obtenerVenta(bot, lista, mensaje, log):
    if log == True:
        listaTemp = lista
        botTemp = bot

        palabras = mensaje.text.split()[1:]
        if len(palabras) != 2:
            bot.reply_to(mensaje, "Por favor, dame el nombre del articulo y la cantidad que vendiste.")
            return

        articulo = palabras[0]
        venta = int(palabras[1])

        consumirVenta = generarVenta(botTemp, listaTemp, articulo, venta)
        bot.reply_to(mensaje, consumirVenta)
    else:
        bot.reply_to(mensaje, "No iniciaste sesion.")

def generarVenta(bot, listaArticulos, enArticulo, venta):
    for codigo, articulo in listaArticulos.items():
        if articulo["articulo"].lower() == enArticulo.lower():
            if int(articulo["cantidad"]) >= venta:
                articulo["cantidad"] = int(articulo["cantidad"]) - venta
                return f"Venta realizada: Se vendio {venta} de {articulo["articulo"]}."
            else:
                return "Lo siento, no tengo la cantidad necesaria para cubrir su venta."
        else:
            return "Articulo no encontrado."