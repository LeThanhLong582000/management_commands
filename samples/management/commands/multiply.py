from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Multiply two number'

    def add_arguments(self, parser):
        parser.add_argument('--first_number', type= int, default= 1)
        parser.add_argument('--second_number', type= int, default= 1)

    def handle(self, *args, **options):
        first_number = options.get('first_number')
        second_number = options.get('second_number')

        print(first_number * second_number)