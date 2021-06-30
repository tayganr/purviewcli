from .endpoint import Endpoint, decorator

class Graph(Endpoint):
    def __init__(self):
        Endpoint.__init__(self)
        self.app = 'graph'

    @decorator
    def graphReadMe(self, args):
        self.method = 'GET'
        self.endpoint = '/v1.0/me'

    @decorator
    def graphReadMePeople(self, args):
        self.method = 'GET'
        self.endpoint = '/v1.0/me/people'
