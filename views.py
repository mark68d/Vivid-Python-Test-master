from django.http import HttpResponse
import random

def index(request):
  start = int(request.GET.get('start', 1))
  end = int(request.GET.get('end', 1000))
  r1 = random.randint(start, end)
  return HttpResponse(r1)