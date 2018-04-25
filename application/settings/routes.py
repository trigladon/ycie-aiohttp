import os

from application.views import application as application_views


def setup_routes(app):
    # application
    app.router.add_view('/', application_views.Index, name='application_index')
    app.router.add_static('/static/', path='/'.join([os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static']), name='static')