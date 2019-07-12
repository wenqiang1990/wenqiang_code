import os
import web

urls = (
    "/report","Report",
        )

app = web.application(urls,globals())

class report:
    def GET(self):
        #os.system("python E:/workspace/IM5.4.0_timing/ready1.py")#clear_group.pystart_run.py
        return "D:\workspace\API_living\testcase\report\index.html!"


if __name__=="__main__":
    app.run()