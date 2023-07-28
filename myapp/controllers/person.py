from django.shortcuts import render
from django.http import HttpResponse
from ..myresponse import SuzdalenkoJsonResponse
from ..models import Person, LastVisit
import datetime

class PersonController:
    # /userLogin -> email, uid, password
    def userLogin(request):
        PERSON_TUPLE             = Person.objects.get_or_create(email=request.GET.get('email'))
        PERSON_TUPLE[0].lang     = request.META.get('HTTP_ACCEPT_LANGUAGE', ['en-US', ])
        PERSON_TUPLE[0].password = request.GET.get('password')
        PERSON_TUPLE[0].uid      = request.GET.get('uid')
        PERSON_TUPLE[0].save()
        
        VISIT_TUPLE     = LastVisit.objects.get_or_create(user_id=PERSON_TUPLE[0].id)
        VISIT_OBJ       = VISIT_TUPLE[0]
        VISIT_OBJ.time  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if VISIT_OBJ.visit: VISIT_OBJ.visit += 1 
        else: VISIT_OBJ.visit = 1
        VISIT_OBJ.save()
        
        response_data = {}
        response_data['user_id'] = PERSON_TUPLE[0].id
        response_data['email']   = PERSON_TUPLE[0].email
        response_data['time']    = VISIT_OBJ.time
        response_data['visit']   = VISIT_OBJ.visit

        return SuzdalenkoJsonResponse(response_data)
    


def say_hello(request):
    return HttpResponse("say hello")

def say_html(request):
    return render(request, 'hello.html')


"""
    2023-07-23 17:33:17
    jsonRes      = serializers.serialize('json', [VISIT_OBJ])
    return HttpResponse(json.dumps(response_data), content_type="application/json")
"""