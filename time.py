import time
import application.EnviarLinkTelegram;

while True:
    print("init")

    T = application.EnviarLinkTelegram.EnviarLinkTelegram()

    print(T.run2())
    time.sleep(6400)
    print("fire")

