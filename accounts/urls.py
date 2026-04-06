from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("🔥 Accounts homepage working!")

urlpatterns = [
    path('', home),
]



from django.urls import path
from .views import migrate_view

urlpatterns = [
    path('run-migrations/', migrate_view),
]