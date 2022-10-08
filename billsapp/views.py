from re import L

from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {"metadata":{}, "content": "Welcome to bills app"}
    return JsonResponse(data)