import telebot

def verificar_cantidades(bot, listaArticulos, CHAT_ID):
    for codigo, articulo in listaArticulos.items():
        cantidad = articulo["cantidad"]
        if cantidad < 10:
            mensaje = f"¡Atencion! La cantidad de {articulo['nombre']} es inferior al 10%. Cantidad actual: {cantidad}"
            bot.send_message(CHAT_ID, mensaje)