import pywhatkit as kit

def send_whatsapp_message(phone_number: str, message: str):
    """
    Envía un mensaje de WhatsApp inmediatamente usando WhatsApp Web.
    """
    print(f"Enviando mensaje a {phone_number} ahora mismo...")
    kit.sendwhatmsg_instantly(
        phone_no=phone_number,
        message=message,
        wait_time=15,    # tiempo para que cargue WhatsApp Web
        tab_close=True,
        close_time=3     # segundos después de enviar
    )
