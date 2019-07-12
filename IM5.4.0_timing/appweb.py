import os
import web

urls = (
    "/push_apk","Puah_apk",
        )

app = web.application(urls,globals())

class Puah_apk:
    def GET(self):
        os.system("python E:/workspace/IM5.4.0_timing/ready1.py")#clear_group.pystart_run.py
        return "succee!"


if __name__=="__main__":
    app.run()