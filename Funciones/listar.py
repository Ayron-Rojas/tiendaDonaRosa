import telebot

def listarProductos(bot: telebot, mensaje, articulos):
    if not articulos:
        bot.reply_to(mensaje, "No hay articulos almacenados")
    else:
        respuesta = ""
        for codigo, datos in articulos.items():
            respuesta += f"Codigo: {codigo}, Articulo: ´{datos["articulo"]}, Precio: {datos["precio"]}, Cantidad: {datos["cantidad"]}\n"
            bot.reply_to(mensaje, respuesta)