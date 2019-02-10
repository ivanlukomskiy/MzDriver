import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from mzdriver.models import HOLDER


def index(request):
    template = loader.get_template('mzdriver/index.html')
    context = {
        "currentVY": HOLDER.vy
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def set_speed(request):
    if request.method == "PUT":
        value = json.loads(request.body)["value"]
        HOLDER.set_vy(value)

    if request.method == "GET" or request.method == "PUT":
        return JsonResponse({'value': HOLDER.vy})
    else:
        raise Exception("Unsupported method")
