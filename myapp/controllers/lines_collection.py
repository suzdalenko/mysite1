from ..models import CollectionLines, Person
from ..myresponse import SuzdalShortJson, SuzdalenkoJsonResponse


class LinesCollectionController:

    def dataget(request, actionget):
        match actionget:
            # /lines_collection/colection_user/ user_id, colection_id
            case "colection_user":
                ressult_query = CollectionLines.objects.filter(user_id=request.GET.get("user_id"), colection_id=request.GET.get("colection_id"))

            

        return SuzdalShortJson(ressult_query)
    







    def dataupdate(request, post_actions):
        user = Person.objects.get(uid=request.POST.get('uid'), id=request.POST.get('id'))
        response_data = {}
        return SuzdalenkoJsonResponse({'file upload' : post_actions})
        