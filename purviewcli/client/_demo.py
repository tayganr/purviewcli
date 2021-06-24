import subprocess
from purviewcli.client import settings

class Demo():
    def demoGenerate(self, args):
        print(settings.PURVIEW_NAME)
        # data = subprocess.run(["pv", "glossary"])
        # print(data)
        response = { 'hello': 'world' }
        return response
