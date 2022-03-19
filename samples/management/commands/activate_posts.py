from django.core.management.base import BaseCommand
from samples.models import Post

class Command(BaseCommand):
    help = 'Activate all samples'

    def handle(self, *args, **options):
        for obj in Post.objects.filter(activated= False):
            obj.activated = True
            obj.save()