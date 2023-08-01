from myapp.models import CollectionLines
from myapp.myresponse import SuzdalenkoJsonResponse, OrderingPackagesByTruck


class Api:

    def test_one(request):
        OrderingPackagesByTruck(52, 1, 1)



        return SuzdalenkoJsonResponse({"route":"deleted"}) 