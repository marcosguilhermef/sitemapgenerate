import application.TelegramBot
import application.UrlMake


class EnviarLinkTelegram:
    def __init__(self):
        pass

    def run(self):
        URL = application.UrlMake.UrlMake()
        message = {
            "chat_id": "-1001593526027",
            "text": URL.generate_one_url(),
            "disable_web_page_preview": False
        }
        T = application.TelegramBot.TelegramBot().sendMessage(message).getResponse()
        return T
