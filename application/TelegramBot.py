import tools.Request
from dotenv import dotenv_values,find_dotenv

config = dotenv_values(find_dotenv())


class TelegramBot:

    def __init__(self):
        self.data = None
        self.request = None
        self.url = "https://api.telegram.org/bot" + config["TOKEN_API_TELEGRAM"]

    def getMe(self):
        self.request = tools.Request.Request(self.url + "/getMe").make_request()
        return self

    def sendMessage(self, data):
        if self.data:
            self.request = tools.Request.Request(self.url + "/sendMessage", data=self.data).make_request_post()
        else:
            self.request = tools.Request.Request(self.url + "/sendMessage", data=data).make_request_post()
        return self

    def getResponse(self):
        return self.request.getResponse()
