from django.http import HttpResponse


def index(request):
    x = request.GET.get("x", "")
    return HttpResponse(fib(int(x)))


def fib(num: int):
    if not num:
        return 0
    if num == 1:
        return 1

    return fib(num - 1) + fib(num - 2)
