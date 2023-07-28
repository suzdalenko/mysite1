from django.http import HttpResponse, JsonResponse

def SuzdalenkoJsonResponse(x):
    jsonResponse = JsonResponse(x)
    jsonResponse["Access-Control-Allow-Origin"] = "*"
    # jsonResponse["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    # jsonResponse["Access-Control-Max-Age"] = "1000"
    # jsonResponse["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return jsonResponse