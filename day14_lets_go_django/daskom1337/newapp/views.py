from django.template import Context
from django.shortcuts import render

name = 'fakhri [fai] [f4r4w4y]'
profession = 'Programmer, Developer'
hobbies = 'Playing computer or other kind of electronic devices'

# Create your views here.
def index(request):
    return render(request, 'profile.html', {
            "name": name,
            "profession": profession,
            "hobbies": hobbies
        }
    )