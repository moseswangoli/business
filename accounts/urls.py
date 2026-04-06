from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("🔥 Accounts homepage working!")

urlpatterns = [
    path('', home),
]


