from django.core.management.base import BaseCommand
from django.core import management

# Management Command Automation
class Command(BaseCommand):
    help = 'Automation commands'

    def handle(self, *args, **kwargs):
        management.call_command('deactivate_posts')