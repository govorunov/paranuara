from django.core.management.base import BaseCommand, CommandError
from .models import Companies, People, Tags, Vegetables, Fruits
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class Command(BaseCommand):
    help = 'Loads companies data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('filename', help="File containing companies data")

    def handle(self, *args, **options):
        try:
            with open(args.filename, 'r') as companies_file:
        except OSError:
            raise CommandError('Cannot open file %s' % args.filename)
