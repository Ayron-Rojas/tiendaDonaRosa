import telebot
 
class COMANDOS:
    Agregar = "/agregar"
    Editar = "/editar"
    Eliminar = "/eliminar"
    Ver = "/ver"

def helper(bot, mensaje):
     bot.reply_to(mensaje, f"""🤖 Hola, soy el Bot Tiendita rosita le ayudara con su tienda.\n
    Se puede comunicar conmigo a traves de los siguentes comandos:\n
    {COMANDOS.Agregar} (Con esto agregas tus articulos, aqui un ejemplo: \n
        agregar 1 lechuga 5 1000).\n
    {COMANDOS.Editar} (Con esto editaras un articulo.).\n
    {COMANDOS.Eliminar} (Con esto eliminaras un articulo).\n
    {COMANDOS.Ver} (Con esto veras todos los articulos que tienes en tu tiendita.).
    """)