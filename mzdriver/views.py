import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from mzdriver.models import HOLDER


def index(request):
    template = loader.get_template('mzdriver/index.html')
    context = {
        "currentVY": HOLDER.vy,
        "velocityOptions": range(-100, 120, 25)
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def set_speed(request):
    if request.method == "PUT":
        value = json.loads(request.body.decode('utf-8'))["value"]
        HOLDER.set_vy(value)

    if request.method == "GET" or request.method == "PUT":
        return JsonResponse({'value': HOLDER.vy})
    else:
        raise Exception("Unsupported method")
