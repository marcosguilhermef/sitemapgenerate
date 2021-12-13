import application.SiteMapGenerate
import application.EnviarLinkTelegram;
import sys

arg = sys.argv
if arg[1] == "-w":
    A = application.SiteMapGenerate.SiteMapGenerate()
    A.xml_wirite()
elif arg[1] == "-s":
    T = application.EnviarLinkTelegram.EnviarLinkTelegram()
    print(T.run())
