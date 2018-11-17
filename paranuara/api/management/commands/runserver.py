from django.core.management.base import BaseCommand
from django.contrib.staticfiles.handlers import StaticFilesHandler
from paranuara.wsgi import application
from wsgiserver import WSGIServer


class Command(BaseCommand):
    help = 'Loads people data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('port', default='8000', nargs='?', help="Port number to listen")
        pass

    def handle(self, *args, **options):
        port = int(options['port'])
        server = WSGIServer(StaticFilesHandler(application), port=port)
        server.start()
