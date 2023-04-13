from django.http import HttpResponse
from .models import Answer


def index(request):
    x = request.GET.get("x", "")
    return HttpResponse(fib(int(x)))


def fib(num: int):
    try:
        ans = Answer.objects.get(num=num)
        return ans.value
    except Answer.DoesNotExist:
        if not num:
            return 0
        if num == 1:
            return 1

        ans = fib(num - 1) + fib(num - 2)
        temp = Answer(num=num, value=ans)
        temp.save()
        return ans
