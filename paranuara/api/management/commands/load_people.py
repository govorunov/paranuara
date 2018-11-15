from django.core.management.base import BaseCommand, CommandError
# from api.models import Companies, People, Tags, Vegetables, Fruits
from api.serializers import PeopleImportSerializer
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class Command(BaseCommand):
    help = 'Loads people data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('filename', help="File containing people data")

    def handle(self, *args, **options):
        filename = options['filename']
        try:
            with open(filename, 'rb') as companies_file:
                data = JSONParser().parse(companies_file)
                serializer = PeopleImportSerializer(data=data, many=True)
                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                    return "Successfully loaded %s" % filename
                else:
                    return "File format is invalid: %s" % filename
        except OSError:
            raise CommandError('Cannot open file %s' % filename)
