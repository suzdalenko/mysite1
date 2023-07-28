from django.http import HttpResponse, JsonResponse
from django.core import serializers


def SuzdalenkoJsonResponse(x):
    jsonResponse = JsonResponse(x)
    jsonResponse["Access-Control-Allow-Origin"] = "*"
    # jsonResponse["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    # jsonResponse["Access-Control-Max-Age"] = "1000"
    # jsonResponse["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return jsonResponse


def SuzdalShortJson(qeurySet):
    jsonResponse = serializers.serialize('json', qeurySet)
    mi_response = HttpResponse(jsonResponse, content_type="application/json")
    mi_response["Access-Control-Allow-Origin"] = "*"
    return mi_response