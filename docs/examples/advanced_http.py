from nameko.web import http
from werkzeug.wrappers import Response

class Service(object):

    @http('GET', '/privileged')
    def forbidden(self):
        return 403, "Forbidden"

    @http('GET', '/google')
    def redirect(self):
        return 201, {'Location': 'https://www.example.com/widget/1'}, ""

    @http('GET', '/custom')
    def custom(self):
        return Response("payload")
