from ..models import CollectionLines, Person
from ..myresponse import OrderingPackagesByTruck, SuzdalShortJson, SuzdalenkoJsonResponse, UserLoginCorrectry
from django.db import connection

class LinesCollectionController:


    def dataget(request, actionget):
        match actionget:
            # /lines_collection/colection_user/ user_id, colection_id
            case "colection_user":
                ressult_query = CollectionLines.objects.filter(colection_id=request.GET.get("collection_id")).order_by("client_name")
                return SuzdalShortJson(ressult_query)
            
            # /lines_collection/orders_by_route/
            case "orders_by_route":
                pass
                slq_req =   """SELECT c.id, c.order_id, c.client_name, c.truck_name, p.lat AS plat, p.lng AS plng, c.palets, c.kilos, c.lat AS clat, c.lng AS clng, c.city, c.truck
                                FROM colectionlines c
                                INNER JOIN person p ON c.user_id = p.id
                                WHERE colection_id = """+request.GET.get("collection_id")+""" AND truck = """+request.GET.get("truck_id")+""" ORDER BY by_order ASC"""
                cursor = connection.cursor()
                cursor.execute(slq_req)
                slq_req = cursor.fetchall()
                cursor.close()
                array_data = []; print(slq_req)
                for line in slq_req:
                    empty_obj = {"id": line[0],"order_id":line[1],"client_name":line[2],"truck_name":line[3],"plat":line[4],"plng":line[5],"palets":line[6],"kilos":line[7],"clat":line[8],"clng":line[9],"city":line[10],"truck":line[11]}
                    array_data.append(empty_obj)
                return SuzdalenkoJsonResponse({'result':array_data})
    

    def dataupdate(request, actionpost):
        if UserLoginCorrectry(request) != True:
            return SuzdalenkoJsonResponse({'user':'dont login'})
        
        cursor = connection.cursor()

        # /post_parameters/create_new_track
        RQ_COLLECTION_ID = request.POST.get("collection_id")
        USERID           = request.POST.get("user_id")
        match actionpost:
            case "create_new_track":
                LIST_LINES_IDS   = request.POST.get('list_lines_id').split(',')
                TRACK_DATA       = request.POST.get("track_data")
                TYPE_TRACK       = request.POST.get("type_track")

                if TYPE_TRACK == 'number':
                    TRACK_NUMBER = int(TRACK_DATA)
                    try:
                        exist_name   = CollectionLines.objects.filter(colection_id=RQ_COLLECTION_ID, truck=TRACK_NUMBER).exclude(truck_name=None).first()
                        TRACK_DATA   = exist_name.truck_name
                    except:
                        TRACK_DATA   = None               
                else:
                    track_in_use     = 'SELECT DISTINCT truck FROM colectionlines WHERE truck > 0 AND colection_id = '+RQ_COLLECTION_ID+' ORDER BY truck ASC'
                    cursor.execute(track_in_use)    
                    track_in_use = cursor.fetchall()                       
                    if len(track_in_use) > 0:
                        for testNumber in range(1111):      
                            testNumber += 1                
                            this_track_exist = False
                            for number_track in track_in_use:
                                if int(number_track[0]) == testNumber:
                                    this_track_exist = True
                                    break
                            if this_track_exist == False:
                                TRACK_NUMBER = testNumber
                                break
                    else:
                        TRACK_NUMBER = 1

                if TRACK_DATA == "": TRACK_DATA = None

                for line_id in LIST_LINES_IDS:
                        if line_id == '': continue
                        CollectionLines.objects.filter(id=line_id, truck=None).update(truck=TRACK_NUMBER, truck_name=TRACK_DATA)
                       
                OrderingPackagesByTruck(RQ_COLLECTION_ID, TRACK_NUMBER, USERID)

            case 'release_orders':
                CollectionLines.objects.filter(colection_id=RQ_COLLECTION_ID).update(truck=None, truck_name=None, by_order=None, meters=None)
                pass    
               
        
        cursor.close()
        return SuzdalenkoJsonResponse({'actionpost' : actionpost})
        