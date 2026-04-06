from django.http import HttpResponse
from django.core.management import call_command

def migrate_view(request):
    call_command('migrate')  # Runs all migrations
    return HttpResponse("Migrations applied!")