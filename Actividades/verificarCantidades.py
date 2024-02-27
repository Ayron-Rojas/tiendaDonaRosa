import telebot



def verificar_cantidades(bot, listaArticulos, chat_id):
    for codigo, articulo in listaArticulos.items():
        cantidad = articulo["cantidad"]
        if cantidad < 10:
            mensaje = f"¡Atencion! La cantidad de {articulo['nombre']} es inferior al 10%. Cantidad actual: {cantidad}"
            bot.send_message(chat_id, mensaje)