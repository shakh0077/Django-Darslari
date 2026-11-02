from django.http import HttpResponse


def home(request):
    return HttpResponse("Assalomu alaykum! \n Men Django dasturchisi bo‘lishni o‘rganyapman.")


def about(request):
    return HttpResponse("Salom About  Pagega hush kelibsiz !")