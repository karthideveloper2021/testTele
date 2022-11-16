from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getCommand(request):
    print(request.GET)
    print(request.POST)
    return JsonResponse({"text":"hi"})