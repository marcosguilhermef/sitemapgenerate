import application.TelegramBot
import application.UrlMake


class EnviarLinkTelegram:
    def __init__(self):
        pass

    def run(self):
        URL = application.UrlMake.UrlMake()
        chat_id = ["-1001593526027", "-1001703894032"]
        T = []
        url = URL.get_url_whatsapp()
        for i in chat_id:
            message = {
                "chat_id": i,
                "text": url,
                "disable_web_page_preview": False
            }
            T.append(application.TelegramBot.TelegramBot().sendMessage(message).getResponse().json())
        return T
