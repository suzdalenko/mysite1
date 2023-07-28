from django.urls import path, include
from .controllers import person, collection, lines_collection


urlpatterns = [
    # path('hello/', person.say_hello),
    # path('html/', person.say_html),

    path('userLogin/', person.PersonController.userLogin),

    path('uploadFileCollection/', collection.CollectionController.uploadFileCollection ),
    path('getAllCollection/', collection.CollectionController.getAllCollection),
    path('deleteCollection/', collection.CollectionController.deleteCollection),

    path("lines_collection/<str:actionget>/", lines_collection.LinesCollectionController.dataget),
    path("post_parameters/<str:post_actions>/", lines_collection.LinesCollectionController.dataupdate),

]