from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(renderer='home.pt')
class CustmanViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.pt')
    def home(request):
        return {}
