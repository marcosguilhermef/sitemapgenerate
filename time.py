import time
import application.EnviarLinkTelegram;

while True:
    print("init")
    time.sleep(2700)
    print("fire")
    T = application.EnviarLinkTelegram.EnviarLinkTelegram()
    print(T.run().json())
