import csv
import os
import requests
import json
from ..myresponse import SuzdalenkoJsonResponse
from ..models import Collection, CollectionLines, Person



def handle_uploaded_file(f):
    with open('mysite/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

""" upload file to server
    delete old and create new collection lines
    i am looking for the order coordinates
"""
class CollectionController:
    # /uploadFileCollection POST user_id uid csv_file ...
    def uploadFileCollection(request):
        rec_file_name = request.FILES['file'].name
        file_extension = rec_file_name.split('.')[1]
        if file_extension.lower() != 'csv': 11 / 0

        handle_uploaded_file(request.FILES['file'])

        coll = Collection.objects.get_or_create(user_id=request.POST.get('user_id'), uid=request.POST.get('uid'), week=request.POST.get('week'))[0]
        collection = Collection.objects.get(id=coll.id)
        collection.file_name = rec_file_name
        collection.user_id   = request.POST.get('user_id')
        collection.uid       = request.POST.get('uid')
        collection.date      = request.POST.get('date')
        collection.week      = request.POST.get('week')
        collection.save()
        int_palets = 0
        int_kilos  = 0

        CollectionLines.objects.filter(user_id=collection.user_id, colection_id=coll.id).delete()

        for line in open('mysite/static/upload/'+rec_file_name, 'r', encoding='latin', errors='ignore'):
            csv_row = line.split(';')
            line_collection = CollectionLines(user_id=collection.user_id, colection_id=collection.id, order_id=int(csv_row[0]), client_name=str(csv_row[1]), delivery_date=str(csv_row[2]))
            line_collection.palets  = csv_row[3]; int_palets += int(csv_row[3])
            line_collection.kilos   = csv_row[4]; int_kilos += int(csv_row[4])
            line_collection.country = csv_row[5].strip()
            line_collection.region  = csv_row[6].strip()
            line_collection.city    = csv_row[7].strip()
            line_collection.save()

        collection.pallets = int_palets
        collection.kilos   = int_kilos
        collection.save()


        list_lines = CollectionLines.objects.filter(user_id=collection.user_id)
        for line_l in list_lines:
            address    = line_l.country+'+'+line_l.region+'+'+line_l.city
            address    = address.strip().lower().replace(' ', '+').replace('++', '+')
            url_path   = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key=AIzaSyCoxqAOQdGqxOOGz6jumPpV-3eziosg7gw'
            result     = requests.get(url_path)
            parsed     = json.loads(result.content)
            first      = parsed['results'][0]
            second     = first['geometry']['location']
            line_l.lat = second['lat']
            line_l.lng = second['lng']
            line_l.save()

        try:
            os.remove('mysite/static/upload/'+rec_file_name)
        except:
            pass

        return SuzdalenkoJsonResponse({'file upload':'ok'})


    # /getAllCollection GET user_id
    def getAllCollection(request):
        collections   = Collection.objects.filter(user_id=request.GET.get('user_id')); print(collections)
        response_data = {}
        inner_array   = []
        for item in collections.iterator():
            interObj = {}
            interObj['id']        = item.id
            interObj['date']      = item.date
            interObj['pallets']   = item.pallets
            interObj['kilos']     = item.kilos
            interObj['file_name'] = item.file_name
            interObj['week']      = item.week
            inner_array.append(interObj)
        response_data['data'] = inner_array
        response_data = SuzdalenkoJsonResponse(response_data)
        return response_data


    # /deleteCollection
    def deleteCollection(request):
        try:
            real_user  = Person.objects.get(id=request.POST.get('user_id'), uid=request.POST.get('uid'))
            collection = Collection.objects.get(id=request.POST.get('collection_id'),  uid=request.POST.get('uid'))
            CollectionLines.objects.filter(colection_id=collection.id).delete()
            collection.delete()
        except Person.DoesNotExist:
            pass

        return SuzdalenkoJsonResponse({"route":"deleted"})

"""
x = Person.objects.filter(name="baby").first()

with open('mysite/static/upload/'+rec_file_name, "r") as f:
           reader = csv.reader(f, delimiter="\t")
           for i, line in enumerate(reader):
               print('-----------'+str(i)+'-----')
               print(line[0].split(';'))
               csv_row = line[0].split(';')

"""
