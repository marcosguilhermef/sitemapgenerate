import time
import application.EnviarLinkTelegram;

while True:
    print("init")

    T = application.EnviarLinkTelegram.EnviarLinkTelegram()

    print(T.run())
    time.sleep(3600)

    print("fire")
    #T = application.EnviarLinkTelegram.EnviarLinkTelegram()
    #print(T.run().json())
