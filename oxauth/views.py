import urllib.parse

from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings

def login(request):
    url = "/accounts/login/"

    next = request.GET.get("next", None)
    if next:
        url = "/accounts/login/?r={}".format(urllib.parse.quote(next))

    return redirect(url)


def logout(request):
    url = "/accounts/logout/"

    next = request.GET.get("next", None)
    if next:
        url = "/accounts/logout/?r={}".format(urllib.parse.quote(next))

    return redirect(url)
