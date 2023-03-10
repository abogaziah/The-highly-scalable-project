from django.http import HttpResponse


def index(request):
    x= request.GET.get("x", "")
    return HttpResponse(x)
